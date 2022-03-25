def mod(m):
    previous, current = 0, 1
    fib = [0, 1]
    fib_mod = [0, 1]
    
    for i in range(0, m * m):
        fib.append(fib[i] + fib[i + 1])
        fib_mod.append((fib[i] + fib[i + 1]) % m)
        
        previous, current \
        = current, (previous + current) % m
        
        if (previous == 0 and current == 1):
            return fib_mod[:-2]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    lst = mod(m)
    
    return lst[n % len(lst)]
    

n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
