def winner():
    _ = int(input())
    games = input()
    
    anton = games.count("A")
    danik = games.count("D")
    
    if anton > danik:
        print("Anton")
        
    elif anton < danik:
        print("Danik")
        
    else:
        print("Friendship")
        
        
winner()