def fuel_spent():
    time = int(input())
    speed = int(input())
    
    print("{:.3f}".format(time * speed / 12))
    
fuel_spent()