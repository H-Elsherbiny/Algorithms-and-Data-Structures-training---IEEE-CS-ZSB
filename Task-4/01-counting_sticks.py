def sticks():
    lst = list(map(str, input()))
    
    plus = lst.index("+")
    equal = lst.index("=")
    
    st = len(lst[:plus])
    nd = len(lst[plus + 1: equal])
    result = len(lst[equal + 1:])
    
    if st + nd == result:
        print(*lst, sep=(""))
        
    elif st + nd - result == 2:
        if st > 1:
            lst.pop(0)
        else:
            lst.pop(st + 1)
        
        lst.append("|")
        print(*lst, sep=(""))
        
    elif st + nd - result == -2:
        lst.pop(-1)
        lst.insert(0, "|")
        print(*lst, sep=(""))
        
    else:
        print("Impossible")

    
sticks()