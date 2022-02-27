def birds():
    num = int(input())
    wires = list(map(int, input().split()))
    t = int(input())
    
    for i in range(t):
        temp = list(map(int, input().split()))
        if temp[0] == 1:
            try:
                wires[temp[0]] += wires[temp[0] - 1] - temp[1]
            except:
                print("0")
                return
            
        elif temp[0] == num:
            wires[temp[0] - 2] += temp[1] - 1
            
        else:
            wires[temp[0]] += wires[temp[0] - 1] - temp[1]
            wires[temp[0] - 2] += temp[1] - 1
            
        wires[temp[0] - 1] = 0
        
    print(*wires, sep=("\n"))
    

birds()