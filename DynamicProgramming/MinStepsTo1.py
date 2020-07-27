import sys
#1st way
def minStepsTo1(n):
    if n == 1:
        return 0
    ans1 = minStepsTo1(n - 1)
    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minStepsTo1(n//2)
    ans3 = sys.maxsize
    if n % 3 == 0:
        ans3 = minStepsTo1(n // 3)
    ans = min(ans1, min(ans2, ans3)) + 1;
    return ans




##n = int(input())
##ans = minStepsTo1(n)
##print(ans)




def minStepsTo1M(n, dp):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if dp[n - 1] == -1:
        ans1 = minStepsTo1M(n - 1, dp)
        dp[n - 1] = ans1
    else:
        ans1 = dp[n - 1]

    
    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1M(n//2)
            dp[n//2] = ans2
        else:
            ans2 = dp[n // 2]
            
    ans3 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans3 = minStepsTo1M(n // 3)
            dp[n // 3] = ans3
        else:
            ans3 = dp[n //3]
            
    ans = min(ans1, min(ans2, ans3)) + 1;
    return ans




##n = int(input())
##dp = [-1 for i in range(n + 1)]
##ans = minStepsTo1M(n, dp)
##print(ans)


def minStepsTo1I(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    maxNum = sys.maxsize
    for i in range(2, n + 1):
        op1 = dp[i - 1]
        op2 = dp[i // 2] if i % 2 == 0 else maxNum
        op3 = dp[i // 3] if i % 3 == 0 else maxNum
        dp[i] = 1 + min(op1, op2, op3)
    return dp[n]
    



n = int(input())
ans = minStepsTo1I(n)
print(ans)


def length(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count

def appendLastNToFirst(head, n) :
    count = length(head) - n
    curr = head
    i = 1
    while i < count:
        curr = curr.next
    	i+= 1
    head2 = curr.next
    curr.next = None
    tail = head2
    while tail.next != None:
        tail = tail.next
	tail.next = head
    return head2
















































