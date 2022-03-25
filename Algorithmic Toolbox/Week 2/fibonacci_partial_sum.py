def fibo(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c - 1

def fibonacci_partial_sum_naive(m, n):
    if n <= 1:
        return n

    lesser_n = (n + 2) % 60
    lesser_m = (m + 1) % 60
    
    if lesser_n <= 1:
        a = lesser_n - 1
    else:
        a = fibo(lesser_n)
        
    if lesser_m <= 1:
        b = lesser_m - 1
    else:
        b = fibo(lesser_m)
    
    return a - b if a >= b else a - b + 10

from_, to = map(int, input().split())
print(fibonacci_partial_sum_naive(from_, to))
