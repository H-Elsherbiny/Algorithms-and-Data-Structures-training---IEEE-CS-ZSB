def pages():
    n, p, k = map(int, input().split())
    
    if p - k > 1:
        print("<<", end=(" "))
        
    for i in range(-k, k + 1):
        if p + i < 1:
            continue
        elif p + i > n:
            break
        
        if i == 0:
            print(f"({p})", end=(" "))
        
        else:
            print(p + i, end=(" "))
            
    if p + k < n:
        print(">>")
        

pages()