def gcd_naive(a, b):
    if b == 0:
        return a
    
    d = a % b
    return gcd_naive(b, d)


a, b = map(int, input().split())
print(gcd_naive(a, b))