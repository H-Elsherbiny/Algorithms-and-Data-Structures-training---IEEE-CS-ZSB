def steps():
    stones = input()
    instructions = input()
    j = 0
    
    for i in range(len(instructions)):
        if stones[j] == instructions[i]:
            j += 1
            
    print(j + 1)
    
steps()