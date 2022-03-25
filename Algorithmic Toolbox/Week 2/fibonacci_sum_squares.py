def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    lesser = (n + 2) % 60
    if lesser <= 1:
        return abs(lesser - 1)
    
    a, b = 0, 1
    for _ in range(2, lesser + 1):
        c = a + b
        c %= 10
        _sum = a ** 2 + b ** 2 
        _sum %= 10
        b, a = c, b
        
    if _sum != 0:
        return _sum - 1
    else:
        return 9
    

n = int(input())
print(fibonacci_sum_squares_naive(n))