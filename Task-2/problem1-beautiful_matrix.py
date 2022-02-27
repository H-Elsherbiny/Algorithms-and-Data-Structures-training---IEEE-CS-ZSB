def moves():
    matrix = []
    
    for i in range(5):
        matrix.append(list(map(int, input().split())))
        
        try:
            num = abs(i - 2) + abs(matrix[i].index(1) - 2)
        except:
            continue
        
    return(num)
    
print(moves())