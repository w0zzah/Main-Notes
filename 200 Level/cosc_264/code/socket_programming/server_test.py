#To test, type in terminal: (port nums must be matching)
#python3 server.py {port num 1} {port num 2} {port num 3}
#python3 server_test.py {port num 1} {port num 2} {port num 3}

#!/usr/bin/env python3
"""
Raw UDP test harness for server.py (DateTime UDP protocol, COSC264 2026).

How to use:
    Terminal 1:  python3 server.py <eng_port> <mao_port> <ger_port>
    Terminal 2:  python3 test_server.py <eng_port> <mao_port> <ger_port>

This bypasses your client entirely and talks raw UDP to your server, so it
tests server.py in isolation. For each case it tells you whether a response
should arrive at all, and (for the valid cases) checks the response fields.

IMPORTANT: this script can't read your server's console, so for each case it
also prints the status/error message your server SHOULD be printing at that
moment. Keep an eye on terminal 1 while this runs and compare by eye - the
assignment marks you on those exact strings, and that's the one thing this
script can't verify for you automatically.
"""

import socket
import struct
import sys
from datetime import datetime

MAGIC = 0x36FB


def build_request(magic=MAGIC, ptype=0x0001, rtype=0x0001):
    return struct.pack(">HHH", magic, ptype, rtype)


def send_and_wait(sock, addr, packet, timeout=1.5):
    sock.settimeout(timeout)
    sock.sendto(packet, addr)
    try:
        data, _ = sock.recvfrom(256)
        return data
    except socket.timeout:
        return None


def describe_response(data):
    if data is None:
        return "no response"
    if len(data) < 13:
        return f"SHORT response ({len(data)} bytes): {data!r}"
    magic, ptype, lang, year, month, day, hour, minute, length = struct.unpack(
        ">HHHHBBBBB", data[:13])
    text = data[13:13 + length]
    try:
        text = text.decode("utf-8")
    except UnicodeDecodeError:
        text = f"<undecodable: {data[13:]!r}>"
    return (f"magic={hex(magic)} ptype={hex(ptype)} lang={lang} "
            f"date={year}-{month:02d}-{day:02d} time={hour:02d}:{minute:02d} "
            f"len={length} text={text!r}")


def run_case(name, addr, packet, expect_response, expected_server_msg=""):
    print(f"\n--- {name} ---")
    print(f"  sending {len(packet)} bytes: {packet!r}")
    if expected_server_msg:
        print(f"  server terminal should show: {expected_server_msg}")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data = send_and_wait(s, addr, packet)
    result = describe_response(data)
    got_response = data is not None
    ok = got_response == expect_response
    print(f"  {'PASS' if ok else 'FAIL'}: expected_response={expect_response}, got: {result}")
    return ok


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 test_server.py <eng_port> <mao_port> <ger_port>")
        sys.exit(1)
    eng, mao, ger = (int(p) for p in sys.argv[1:4])
    eng_addr = ("localhost", eng)
    mao_addr = ("localhost", mao)
    ger_addr = ("localhost", ger)

    results = []

    # --- Valid requests, one per language ---
    results.append(run_case(
        "Valid date request (English)", eng_addr,
        build_request(rtype=0x0001), True,
        "English received date request from 127.0.0.1"))

    results.append(run_case(
        "Valid time request (Maori)", mao_addr,
        build_request(rtype=0x0002), True,
        "Māori received time request from 127.0.0.1"))

    results.append(run_case(
        "Valid date request (German)", ger_addr,
        build_request(rtype=0x0001), True,
        "German received date request from 127.0.0.1"))

    # --- Malformed packets: server must drop ALL of these silently ---
    results.append(run_case(
        "Too short (4 bytes)", eng_addr,
        build_request()[:4], False,
        "ERROR: Packet length incorrect for a DT_Request, dropping packet"))

    results.append(run_case(
        "Too long (8 bytes, otherwise valid)", eng_addr,
        build_request() + b"\x00\x00", False,
        "ERROR: Packet length incorrect for a DT_Request, dropping packet "
        "-- if this FAILs, check your length test is '!= 6' (not '< 6') and "
        "your recvfrom buffer is bigger than 6 bytes"))

    results.append(run_case(
        "Bad magic number", eng_addr,
        struct.pack(">HHH", 0x1234, 0x0001, 0x0001), False,
        "ERROR: Packet magic number is incorrect, dropping packet"))

    results.append(run_case(
        "Wrong packet type (a Response-type value sent as a request)", eng_addr,
        struct.pack(">HHH", MAGIC, 0x0002, 0x0001), False,
        "ERROR: Packet is not a DT_Request, dropping packet"))

    results.append(run_case(
        "Invalid request type (0x0003)", eng_addr,
        build_request(rtype=0x0003), False,
        "ERROR: Packet has invalid type, dropping packet"))

    results.append(run_case(
        "Invalid request type (0x0000)", eng_addr,
        build_request(rtype=0x0000), False,
        "ERROR: Packet has invalid type, dropping packet"))

    # --- Robustness: server must NOT die after a bad packet ---
    print("\n--- Robustness: bad packet followed immediately by a good one ---")
    run_case(
        "Bad packet (should be dropped, server must not crash)", eng_addr,
        struct.pack(">HHH", 0xDEAD, 0x0001, 0x0001), False)
    ok = run_case(
        "Good packet sent right after (server must still be alive)", eng_addr,
        build_request(rtype=0x0002), True)
    results.append(ok)
    if not ok:
        print("  !! If the earlier valid-request tests passed but this one "
              "failed, your server is very likely crashing on the bad "
              "packet instead of catching the error and looping back to "
              "'Waiting for requests...'. Wrap the recieve_packet() call in "
              "main() with a try/except.")

    # --- Field correctness check against wall clock ---
    print("\n--- Field correctness check ---")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data = send_and_wait(s, eng_addr, build_request(rtype=0x0001))
    if data and len(data) >= 13:
        magic, ptype, lang, year, month, day, hour, minute, length = struct.unpack(
            ">HHHHBBBBB", data[:13])
        now = datetime.now()
        checks = {
            "magic == 0x36FB": magic == MAGIC,
            "ptype == 0x0002": ptype == 0x0002,
            "lang == 1 (English)": lang == 1,
            "year matches now": year == now.year,
            "month matches now": month == now.month,
            "day matches now": day == now.day,
        }
        for desc, ok in checks.items():
            print(f"  {'PASS' if ok else 'FAIL'}: {desc}")
    else:
        print("  FAIL: no usable response received for field check")

    n_pass = sum(1 for r in results if r)
    print(f"\n{n_pass}/{len(results)} response-presence checks passed "
          f"(remember to also eyeball the server terminal messages).")


if __name__ == "__main__":
    main()