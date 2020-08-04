#125
#71 rough

def validPalindrome(s):
    if len(s) <= 1: return True
    start = 0
    end = len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if start < end and s[start].lower() != s[end].lower() :
            return False
        start += 1
        end -= 1
    return True

s = input()
print(validPalindrome(s))

            
                                                 
    
