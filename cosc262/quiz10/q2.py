def change_greedy(amount, coinage):
    # Sort the coinage list in descending order to always pick the largest coin first
    sorted_coinage = sorted(coinage, reverse=True)
    
    result = []
    remaining = amount
    
    for coin in sorted_coinage:
        if remaining == 0:
            break
            
        # Determine how many coins of this value can fit into the remaining amount
        count = remaining // coin
        
        if count > 0:
            result.append((count, coin))
            remaining %= coin  # Update the remaining amount
            
    # If the greedy approach couldn't reduce the amount to exactly 0, return None
    if remaining > 0:
        return None
        
    return result