def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        last = previous + current
        last %= 10
        previous = current
        current = last

    return last


n = int(input())
print(get_fibonacci_last_digit_naive(n))
