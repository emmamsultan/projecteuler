def c(n):
    if bin(n)[2:] == bin(n)[2:][::-1]:
        if str(n)[::-1]==str(n):
            return True
    return False        
b=[]
for i in range(10,1000000):
    if c(i):
        b.append(i)
sum(b)
