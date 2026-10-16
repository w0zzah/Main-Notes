def helper(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")
    

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    
    # initial mask saying all numbers are prime bar 1 and 2
    primes_mask = [True] * (limit + 1)
    primes_mask[0] = primes_mask[1] = False

    # A number is prime if it is not divisible by any number less than its sqrt
    for divisor in range(2, int(limit**0.5) + 1):
        # If this divisor is prime
        if primes_mask[divisor]:
            
            # Cycle through all multiples of the devisor, starting with the square
            for i in range(divisor * divisor, limit + 1, divisor):
                # Set all multiples of this divisor as False, all of those values are not prime
                primes_mask[i] = False
    
    return [num for num, is_prime in enumerate(primes_mask) if is_prime]

def check_primes_in_range():

    lowerbound = helper("Choose a lower bound: ")
    upperbound = helper("Choose an upper bound: ")

    all_primes = sieve_of_eratosthenes(upperbound)

    total = [p for p in all_primes if p >= lowerbound]
    # print(total)
    print(f"There is a total of {len(total)} primes between: {lowerbound} - {upperbound}")

check_primes_in_range()

