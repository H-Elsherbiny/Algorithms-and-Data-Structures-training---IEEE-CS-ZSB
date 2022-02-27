def amazing():
    t = int(input())
    lst = list(map(int, input().split()))
    worst = best = lst[0]
    counter = 0
    
    for i in range(1, t):
        if lst[i] > best:
            best = lst[i]
            counter += 1
            
        elif lst[i] < worst:
            worst = lst[i]
            counter += 1
            
    print(counter)
    
    
amazing()