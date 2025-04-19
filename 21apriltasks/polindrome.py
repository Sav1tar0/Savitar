def polindrome(s):
    a = s[::-1]
    if a == s:
        return True
    else:
        return False
    
print(polindrome("almaamla"))