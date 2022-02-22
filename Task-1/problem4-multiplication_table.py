def multiplication_table():
    num = int(input())
    
    for i in range(1, 11):
        print(str(i) + " x " + str(num)  + " = " + str(i * num))
        
multiplication_table()