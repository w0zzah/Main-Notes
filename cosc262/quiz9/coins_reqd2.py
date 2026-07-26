def coins_reqd(value, coinage):
    num_coins = [0] * (value + 1)
    # This list will store which coin denomination was used for each amount
    last_coin_used = [0] * (value + 1)
    
    for amt in range(1, value + 1):
        minimum = None
        best_coin = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[amt - c]
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    best_coin = c  # Remember which coin gave us this minimum
        
        num_coins[amt] = 1 + minimum
        last_coin_used[amt] = best_coin

    # --- Backtracking Phase ---
    counts = {}
    current_amt = value
    while current_amt > 0:
        coin = last_coin_used[current_amt]
        counts[coin] = counts.get(coin, 0) + 1
        current_amt -= coin
    
    # Convert dictionary to a list of sorted tuples (decreasing order)
    result = sorted(counts.items(), key=lambda x: x[0], reverse=True)
    return result

coinage = [1, 10, 25]
amount = 30
coinage_copy = coinage[:]
answer = coins_reqd(amount, coinage)
ok, error = check_answer(amount, coinage, coinage_copy, answer)
if ok:
    print("OK")
else:
    print(error)