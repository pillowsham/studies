# -*- coding: utf-8 -*-

def is_palindrome(n):
    return n == int(str(n)[::-1])

# bruteforce
def p4():
    return max(a*b for a in range(1000) for b in range(1000) if is_palindrome(a*b))
    
print(p4())