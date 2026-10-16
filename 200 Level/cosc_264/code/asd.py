def connection_setup_delay(cable_length_km, light_speed_kmps, message_length_b, data_rate_bps, processing_time_s):
    d = cable_length_km
    c = light_speed_kmps
    m = message_length_b
    r = data_rate_bps
    p = processing_time_s
    
    return 4 * (p + (m/r) + d/c )

def packet_transfer_time(link_length_km, light_speed_kmps, processing_delay_s, data_rate_bps, user_data_bits, overhead_bits):
    d = link_length_km
    c = light_speed_kmps
    p = processing_delay_s
    r = data_rate_bps
    s = user_data_bits
    o = overhead_bits

    return (d/c + (s + o)/r + p)* 2


print(f"{packet_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100):.4f}")