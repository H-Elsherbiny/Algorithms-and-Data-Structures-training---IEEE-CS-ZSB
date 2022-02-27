def socks():
    num = int(input())
    lst = list(map(int, input().split()))
    
    temp = []
    counter = 0
    
    for i in range(2 * num):
        if lst[i] in temp:
            temp.remove(lst[i])
        
        else:
            temp.append(lst[i])
            
        counter = max(counter, len(temp))
        
    print(counter)
    
socks()