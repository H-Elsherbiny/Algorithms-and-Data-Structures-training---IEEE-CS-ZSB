from math import log

def numbers_of_primes():
    num = int(input())
    first = num / log(num)
    last = 1.25506 * num / log(num)
    
    print("{:.1f}".format(first), end=(" "))
    print("{:.1f}".format(last))
    

numbers_of_primes()