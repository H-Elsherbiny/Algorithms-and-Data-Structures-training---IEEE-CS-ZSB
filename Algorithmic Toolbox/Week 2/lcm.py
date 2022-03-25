def gcd_naive(a, b):
    if b == 0:
        return a
    
    d = a % b
    return gcd_naive(b, d)



def lcm_naive(a, b):
    
    return a * b // gcd_naive(a, b) 


a, b = map(int, input().split())
print(lcm_naive(a, b))

