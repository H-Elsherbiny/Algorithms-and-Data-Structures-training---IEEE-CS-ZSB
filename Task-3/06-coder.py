from math import ceil

def coder():
    t = int(input())
    
    num = ceil(t ** 2 / 2)
    print(num)
    
    lst = ["C", "."]
    lst = lst * t
    
    for i in range(1, t + 1):
        if i % 2 != 0:
            print(*lst[:t], sep=(""))
            
        else:
            print(*lst[1: t + 1], sep=(""))
        
        
        
coder()