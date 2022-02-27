def seconds():
    _ = int(input())
    st = set(list(map(int, input().split())))
    try:
        st.remove(0)
        
    except:
        pass
    print(len(st))
    
seconds()