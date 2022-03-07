def transmigration():
    n, m, k = map(float, input().split())
    skills = {}
    
    for i in range(int(n)):
        temp = input().split()
        exp = int(temp[1]) * k
        
        if exp >= 100:
            skills[temp[0]] = exp
            
    for i in range(int(m)):
        temp = input()
        
        if temp not in skills:
            skills[temp] = 0
            
    print(len(skills))
    for i in sorted(skills):
        print(i, int(round(skills[i], 3)))
        

transmigration()