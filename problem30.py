def c(n):
    s=0
    for  l in str(n):
        s+=int(l)**5
    if s==n:
        return True
    return False
a=0
for i in range(2,10000000):
    if c(i):
        a+=i
