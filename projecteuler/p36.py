def is_palindrome(n):
    decimal = str(n)
    binary = bin(n)[2:]
    return decimal == decimal[::-1] and binary == binary[::-1] and binary[0] != '0' and binary[-1] != '0'


print(sum(filter(is_palindrome, range(1000000))))
