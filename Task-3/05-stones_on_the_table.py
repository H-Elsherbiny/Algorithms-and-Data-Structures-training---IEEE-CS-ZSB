def stones():
    t = int(input())
    lst = input()
    
    counter = 0
    
    for i in range(t - 1):
        if lst[i] == lst[i + 1]:
            counter += 1
            
    
    print(counter)
    

stones()