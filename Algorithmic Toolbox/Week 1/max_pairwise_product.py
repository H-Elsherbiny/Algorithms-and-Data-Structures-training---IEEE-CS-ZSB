def max_pairwise_product():
    
    _ = input()
    lst = list(map(int, input().split()))
    
    greatest = max(lst)
    lst.pop(lst.index(greatest))
    
    second_greatest = max(lst)
            
    print(greatest * second_greatest)
    
    
max_pairwise_product()