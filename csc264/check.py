def conv(value: float, from_unit: str, to_unit: str) -> float:
    bit_factors = {
        'b': 1, 'B': 8, 'Bytes': 8, 'Kb': 1e3, 'KB': 8 * 1e3,
        'Mb': 1e6, 'MB': 8 * 1e6, 'Gb': 1e9, 'GB': 8 * 1e9,
        'Tb': 1e12, 'TB': 8 * 1e12,
    }

    f_unit = from_unit.strip()
    t_unit = to_unit.strip()

    if f_unit not in bit_factors or t_unit not in bit_factors:
        valid_units = ", ".join(bit_factors.keys())
        raise ValueError(f"Invalid unit. Choose from: {valid_units}")

    bits = value * bit_factors[f_unit]
    return bits / bit_factors[t_unit]

def convert_dist(d: float, u: str) -> float:
    dist_types = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}
    return d * dist_types[u.strip()]

def calculate_delay():
    calc_type = input("Which Delay Are You Calculating? \n(Propagation, Transmission, Queueing)\n").strip()

    if calc_type not in {"Propagation", "Transmission", "Queueing"}:
        print(f"\nNah idk how to do {calc_type}")
        return

    match calc_type:
        case "Propagation":
            try:
                dist = float(input("Enter distance: "))
                dist_unit = input("Enter distance units (mm, cm, m, km): ").strip()
                distance = convert_dist(dist, dist_unit)
                
                speed = float(input("Enter speed: "))
                speed_unit = input("Enter speed units (mm, cm, m, km): ").strip()
                fspeed = convert_dist(speed, speed_unit)

                delay_seconds = distance / fspeed
                delay_ms = delay_seconds * 1000
                print(f"\nPropagation Delay: {delay_seconds} s or {delay_ms:.2f} ms")
                
            except ValueError as e:
                print(f"\nError: {e}")

        case "Transmission":
            try:
                packet_length = float(input("Enter packet length: "))
                packet_length_type = input("Enter packet unit: ").strip()
                
                rate = float(input("Enter data rate: "))
                rate_type = input("Enter rate unit: ").strip()
                
                packet_length_bits = conv(packet_length, packet_length_type, 'b')
                rate_bps = conv(rate, rate_type, 'b')
                
                delay_seconds = packet_length_bits / rate_bps
                delay_ms = delay_seconds * 1000
                print(f"\nTransmission Delay: {delay_ms:.4f} ms")
                
            except ValueError as e:
                print(f"\nError: {e}")

        case "Queueing":
            try:
                rate = float(input("Enter data rate: "))
                rate_type = input("Enter rate unit: ").strip()
                
                packet_length = float(input("Enter packet length: "))
                packet_length_type = input("Enter packet unit: ").strip()
                
                num_packets = int(input("Enter number of packets in queue: "))
                
                rate_bps = conv(rate, rate_type, 'b')
                packet_length_bits = conv(packet_length, packet_length_type, 'b')
                
                total_bits_in_queue = num_packets * packet_length_bits
                delay_seconds = total_bits_in_queue / rate_bps
                
                delay_ms = delay_seconds * 1000
                print(f"\nQueueing Delay: {delay_ms:.4f} ms")

            except ValueError as e:
                print(f"\nError: {e}")

calculate_delay()