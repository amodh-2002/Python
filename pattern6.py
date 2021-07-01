for i in range(1,4+1):
    for j in range(1,i+1):
        if i%2!=0 and j%2!=0:
            print(1,end="")
        if i%2==0 and j%2!=0:
            print(0,end="")
        if i%2==0 and j%2==0:
            print(1,end="")
        if i%2!=0 and j%2==0:
            print(0, end="")
    print("")
    
        
