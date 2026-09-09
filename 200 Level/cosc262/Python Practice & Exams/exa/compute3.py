# every word in the sequence is from the given set of words;
# no word in the sequence is repeated (i.e. a word appears at most once); and
# for every two consecutive words in the sequence, the last letter of the first word is the same as the first letter of the next word.`
# 

def word_chains(words, min_length, max_length):
    out = []
    words = list(words)
    # Go back through every word
    def back_track(chain, used):
        # If the length of the current chain is less than or greater than the boundaries
        if min_length <= len(chain) <= max_length:
            # Add then chain to out
            out.append(list(chain))
            
        if len(chain) == max_length:
            return
        # For each word in the set of words
        for word in words:
            # If the word has not yet been used
            if word not in used:
                # If the chain has just begun or the conditions have been met:
                # Add the word onto the chain, add it to used so we dont call it again,
                # Then call the function again from the start
                if len(chain) == 0 or chain[-1][-1] == word[0]:
                    chain.append(word)
                    used.add(word)
                    back_track(chain, used)
                    chain.pop()
                    used.remove(word)
    back_track([], set())
    return out


words = {"apple", "banana", "apricot", "tab"}

output = word_chains(words, 2, 10)
output.sort()
print(output)
