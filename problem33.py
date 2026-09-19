for z in range(1,10):
    for x in range(1,10):
        for y in range(1,10):
            n1=int(str(z)+str(x))
            d1=int(str(y)+str(z))
            if n1/d1==x/y:
                print(n1,d1)
