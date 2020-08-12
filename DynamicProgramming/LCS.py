#1ST WAY BY RECURSION SO MUCH OVERLAPPING

def LCS(str1, str2, i, j):

    #basecase
    if i == len(str1) or j == len(str2):
        return 0


    if str1[i] == str2[j]:
        ans = 1 + LCS(str1, str2, i + 1, j + 1)
    else:
        ans1 = LCS(str1, str2, i + 1, j)
        ans2 = LCS(str1, str2, i, j + 1)
        ans = max(ans1, ans2)

    return ans


str1 = "abedgjc"
str2 = "bmdgsc"

#str1 = "bdgec"
#str2 = "bfdmgjc"
ans = LCS(str1, str2, 0, 0)
print(ans)






























