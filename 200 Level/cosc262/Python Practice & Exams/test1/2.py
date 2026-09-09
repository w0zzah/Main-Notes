def decodedate(x):
    
    day = (0x0F800000 & x) >> 23
    month = (0xF0000000 & x) >> 28
    year = (0x1FFFFF & x)
    out = f"{day}.{month}.{year}"
    return out

print(decodedate(2298488591))
print(decodedate(1375733729))