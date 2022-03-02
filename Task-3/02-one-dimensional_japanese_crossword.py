def hidden_numbers():
    t = int(input())
    blocks = input()
    
    temp = 0
    lst = []
    
    for i in range(t):
        if blocks[i] == "B":
            temp += 1
                
        else:
            if temp:
                lst.append(temp)
                temp = 0
                
    if temp:
        lst.append(temp)
        
        
    print(len(lst))
    if lst:
        print(*lst, sep=(" "))
        


hidden_numbers()