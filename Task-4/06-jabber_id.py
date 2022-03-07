import string

def checker():
    email = input()
    
    resource = "o"
    charactrs = string.ascii_letters + string.digits + '_'
    
    try:
        username = email[:email.index('@')]
    except:
        print("NO")
        return 
    
    try:
        hostname = email[email.index('@') + 1: email.index("/")]
    except:
        hostname = email[email.index('@') + 1:]
    
    try:
        resource = email[email.index('/') + 1:]
    except:
        pass
        
    temp = username + resource    
    
    if 0 < len(username) < 17 and 0 < len(resource) < 17:
        for i in temp:
            if i not in charactrs:
                print("NO")
                return        
    else:
        print("NO")
        return

    if 0 < len(hostname) < 33:
        for i in hostname.split("."):
            if i == '':
                print("NO")
                return
                
            else:
                for j in i:
                    if j not in (charactrs + '.'):
                        print("NO")
                        return
    else:
        print("NO")
        return
    
    
    print("YES")
    
    
    
checker()