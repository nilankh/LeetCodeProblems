#checkrough page no 15 17 18

def permutation(inputS, result, count, level):
    
    if(level == len(inputS)):
        #print the result
        for i in range(len(result)):
            print(result[i], end = "")
        print()
        return
    else:
        for i in range(len(inputS)):
            if count[i] == 0:
                continue
            else:
                result[level] = inputS[i]
                count[i] -= 1
                permutation(inputS, result, count, level + 1)
                count[i] += 1



inputS = input()
result = [0 for i in range(len(inputS))]
count = [1 for i in range(len(inputS))]
permutation(inputS, result, count, 0)









