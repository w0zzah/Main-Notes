def decodedate(x):

    day = (0x0F800000 & x) >> 23
    month = (0xF0000000 & x) >> 28
    year = (0x1FFFFF & x)
    out = f"{day}.{month}.{year}"
    return out

def encodedate(day, month, year):

    if not (1 <= month <= 12):
        raise ValueError("invalid month")
        

    if not (1 <= day <= 31):
        raise ValueError("invalid day")
        
    if not (0 <= year <= (1 << 23) - 1):
        raise ValueError("invalid year")
        
    encoded_value = (month << 28) | (day << 23) | year
    
    return encoded_value

print(encodedate(4, 5, 2017))