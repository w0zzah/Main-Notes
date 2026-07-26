# Collatz Theorm, " if n // 2, then n/2 elif odd 3n+1. After x times, n = 1. " Find x
def sequence_length(n):
    # Base case 
    if n == 1:
        return 1
    # Check if even
    elif n % 2 == 0:
        return 1 + sequence_length(n//2)
    # Check if odd
    else:
        return 1 + sequence_length(3*n+1)

print(sequence_length(22))