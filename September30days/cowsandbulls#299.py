#299
#page 99

import collections
def getHint(secret, guess):
    bulls = cows = 0
    for idx, num in enumerate(guess):
            if secret[idx] == num:
                bulls += 1
            else:
                continue
    count_secret = collections.ChainMapCounter(secret)
    for num in guess:
        if num in count_secret:
            if count_secret[num] > 0:
                cows += 1
                count_secret[num] -= 1
            else:
                continue
        else:
            continue
    cows = cows - bulls
            
    return(str(bulls) + "A" + str(cows) + "B")


secret = [int(c) for c in input().split()]
guess = [int(f) for f in input().split()]
print(getHint(secret, guess))























