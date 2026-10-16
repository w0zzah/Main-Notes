#To test, type in terminal:
#python3 test_client.py python3 client.py

#!/usr/bin/env python3
"""
To run: save in same folder as client.py and run: python3 test_client.py client.py

Fake-server test harness for client.py (DateTime UDP protocol, COSC264 2026).

For each response-handling test case this script:
  1. Opens a throwaway UDP socket ("fake server") on a free port.
  2. Runs `python3 client.py <date|time> localhost <port>` as a subprocess.
  3. Waits for the client's request, then sends back a hand-crafted
     (often deliberately broken) DT-Response packet.
  4. Captures the client's stdout and checks it contains the expected text.

There are also standalone argument-validation cases that never touch the
network, since your client should reject bad arguments before it even opens
a socket.

Usage:
    python3 test_client.py /path/to/client.py
"""

import random
import socket
import struct
import subprocess
import sys

MAGIC = 0x36FB


def bind_in_range(sock, lo=1024, hi=32767, attempts=50):
    """Bind to a random port within the assignment's allowed range, since
    letting the OS pick an ephemeral port (the default) can land above
    32767 and trip the client's own port-range validation."""
    for _ in range(attempts):
        port = random.randint(lo, hi)
        try:
            sock.bind(("localhost", port))
            return port
        except OSError:
            continue
    raise RuntimeError("Could not find a free port in range after many attempts")


def valid_response(lang=1, text="Today's date is July 1, 2026"):
    body = text.encode("utf-8")
    header = struct.pack(">HHHHBBBBB", MAGIC, 0x0002, lang, 2026, 7, 1, 8, 5, len(body))
    return header + body


def run_case(client_path, name, response_bytes_fn, request_type="date",
             expected_substrings=(), unexpected_substrings=()):
    print(f"\n--- {name} ---")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as fake_server:
        port = bind_in_range(fake_server)
        fake_server.settimeout(3)

        proc = subprocess.Popen(
            [sys.executable, client_path, request_type, "localhost", str(port)],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        try:
            data, addr = fake_server.recvfrom(2048)
        except socket.timeout:
            proc.kill()
            out, _ = proc.communicate()
            print("  FAIL: client never sent a request. Output so far:")
            print("  " + out.replace("\n", "\n  "))
            return False

        response = response_bytes_fn()
        if response is not None:
            fake_server.sendto(response, addr)
        # if response is None we deliberately stay silent, to test the
        # client's "ERROR: Receiving timed out" path

        try:
            out, _ = proc.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, _ = proc.communicate()
            print("  FAIL: client hung / did not exit in time. Output so far:")
            print("  " + out.replace("\n", "\n  "))
            return False

    print("  client output:")
    print("  " + out.replace("\n", "\n  "))

    ok = True
    for s in expected_substrings:
        if s not in out:
            print(f"  FAIL: expected to see {s!r} in output")
            ok = False
    for s in unexpected_substrings:
        if s in out:
            print(f"  FAIL: did NOT expect to see {s!r} in output")
            ok = False
    print("  PASS" if ok else "  (see failures above)")
    return ok


def run_arg_case(client_path, name, args, expected_substrings):
    """Pure argument-validation case - no fake server involved."""
    print(f"\n--- {name} ---")
    try:
        proc = subprocess.run(
            [sys.executable, client_path] + args,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=5)
        out = proc.stdout
    except subprocess.TimeoutExpired as e:
        out = e.stdout or ""
        print("  FAIL: client did not exit within 5s (hung waiting on something it "
              "shouldn't have opened a socket for?)")

    print("  client output:")
    print("  " + out.replace("\n", "\n  "))
    ok = True
    for s in expected_substrings:
        if s not in out:
            print(f"  FAIL: expected to see {s!r} in output")
            ok = False
    print("  PASS" if ok else "  (see failures above)")
    return ok


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_client.py /path/to/client.py")
        sys.exit(1)
    client_path = sys.argv[1]

    results = []

    # --- Argument validation (no networking should happen) ---
    results.append(run_arg_case(
        client_path, "Wrong number of arguments",
        ["date", "localhost"],
        ["ERROR: Incorrect number of command line arguments"]))

    results.append(run_arg_case(
        client_path, "Invalid request type",
        ["tomorrow", "localhost", "12345"],
        ["ERROR: Request type 'tomorrow' is not valid"]))

    results.append(run_arg_case(
        client_path, "Port is not an integer",
        ["date", "localhost", "abc"],
        ["ERROR: Given port 'abc' is not an integer"]))

    results.append(run_arg_case(
        client_path, "Port out of range (too low)",
        ["date", "localhost", "80"],
        ["ERROR: Given port '80' is not in the range [1024, 32767]"]))

    results.append(run_arg_case(
        client_path, "Port out of range (too high)",
        ["date", "localhost", "40000"],
        ["ERROR: Given port '40000' is not in the range [1024, 32767]"]))

    results.append(run_arg_case(
        client_path, "Unresolvable hostname",
        ["date", "this.host.should.not.exist.invalid", "12345"],
        ["ERROR: Hostname resolution failed"]))

    # --- Response validation (needs the fake server) ---
    results.append(run_case(
        client_path, "Valid English date response",
        lambda: valid_response(lang=1, text="Today's date is July 1, 2026"),
        request_type="date",
        expected_substrings=["English response received:",
                              "Text: Today's date is July 1, 2026",
                              "Date: 1/7/2026", "Time: 08:05"]))

    results.append(run_case(
        client_path, "Too short (12 bytes)",
        lambda: valid_response()[:12],
        expected_substrings=["ERROR: Packet is too small to be a DT_Response"]))

    results.append(run_case(
        client_path, "Bad magic number",
        lambda: struct.pack(">HHHHBBBBB", 0x1234, 0x0002, 1, 2026, 7, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet magic number is incorrect"]))

    results.append(run_case(
        client_path, "Wrong packet type",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0001, 1, 2026, 7, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet is not a DT_Response"]))

    results.append(run_case(
        client_path, "Invalid language code (0)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 0, 2026, 7, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid language"]))

    results.append(run_case(
        client_path, "Invalid language code (4)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 4, 2026, 7, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid language"]))

    results.append(run_case(
        client_path, "Invalid year (>= 2100)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2100, 7, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid year"]))

    results.append(run_case(
        client_path, "Invalid month (0)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 0, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid month"]))

    results.append(run_case(
        client_path, "Invalid month (13)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 13, 1, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid month"]))

    results.append(run_case(
        client_path, "Invalid day (0)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 0, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid day"]))

    results.append(run_case(
        client_path, "Invalid day (32)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 32, 8, 5, 0),
        expected_substrings=["ERROR: Packet has invalid day"]))

    # hour/minute are unsigned bytes (0-255), so >23 / >59 are the only
    # reachable invalid values - 0 is always in range for both.
    results.append(run_case(
        client_path, "Invalid hour (24)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 1, 24, 5, 0),
        expected_substrings=["ERROR: Packet has invalid hour"]))

    results.append(run_case(
        client_path, "Invalid minute (60)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 1, 8, 60, 0),
        expected_substrings=["ERROR: Packet has invalid minute"]))

    results.append(run_case(
        client_path, "Length field lies (says 10 bytes of text, sends 0)",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 1, 8, 5, 10),
        expected_substrings=["ERROR: Packet text length is incorrect"]))

    results.append(run_case(
        client_path, "Text is invalid UTF-8",
        lambda: struct.pack(">HHHHBBBBB", MAGIC, 0x0002, 1, 2026, 7, 1, 8, 5, 2) + b"\xff\xfe",
        expected_substrings=["ERROR: Packet has invalid text"]))

    results.append(run_case(
        client_path, "No response at all (server silent)",
        lambda: None,
        expected_substrings=["ERROR: Receiving timed out"]))

    n_pass = sum(1 for r in results if r)
    print(f"\n{n_pass}/{len(results)} cases passed")


if __name__ == "__main__":
    main()