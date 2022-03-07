def berOS():
    s = input()
    lst = []
    
    lst.append(s[0])
    for i in range(1, len(s)):
        if s[i] == s[i - 1] and s[i] == '/':
            continue
        
        else:
            lst.append(s[i])
            
    if len(lst) > 1 and lst[-1] == '/':
        lst.pop(-1)
        
    print(*lst, sep=(""))
            
            
berOS()