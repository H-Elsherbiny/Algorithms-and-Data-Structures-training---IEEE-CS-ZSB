def problems():
    
    t = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    
    for i in range(t[0]):
        if lst[i] > t[1]:
            left = i
            break
        
    else:
        print(t[0])
        return
    
    for i in range(t[0] - 1, -1, -1):
        if lst[i] > t[1]:
            right = i
            break
        
    if left == right:
        print(t[0] - 1)
        return
    else:
        print(t[0] - (right - left + 1))
        return
    

problems()