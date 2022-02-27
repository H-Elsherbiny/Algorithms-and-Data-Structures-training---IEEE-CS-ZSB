def colored():
    t = list(map(int, input().split()))
    photo = []
    status = False
    
    for i in range(t[0]):
        photo.append(list(map(str, input().split())))
        if 'C' in photo[i] or 'M' in photo[i] or 'Y' in photo[i]:
            status = True
            
    return status


if colored():
    print("#Color")
    
else:
    print("#Black&White")