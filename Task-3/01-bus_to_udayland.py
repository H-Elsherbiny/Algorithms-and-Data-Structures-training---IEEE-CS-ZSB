def seats():
    lst = []
    status = False
    
    t = int(input())
    
    for i in range(t):
        temp = input()
        
        if not status:
            
            if temp[:2] == "OO":
                status = True
                temp = "++" + temp[2:]
                
            elif temp[3:] == "OO":
                status = True
                temp = temp[:3] + "++"
            
        lst.append(temp)
        
    if status:
        print("YES")
        print(*lst, sep=("\n"))
        
    else:
        print("NO")
        
        
seats()