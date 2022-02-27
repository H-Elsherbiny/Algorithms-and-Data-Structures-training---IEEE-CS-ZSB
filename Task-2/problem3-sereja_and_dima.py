def points():
    _ = input()
    lst = list(map(int, input().split()))
    
    sereja = dema = 0
    while lst:
        sereja += max(lst[0], lst[-1])
        lst.remove(max(lst[0], lst[-1]))
        
        try:
            dema += max(lst[0], lst[-1])
            lst.remove(max(lst[0], lst[-1]))
            
        except:
            pass
        
    print(sereja, dema)
    
points()