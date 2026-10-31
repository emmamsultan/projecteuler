p=list(range(2,1000000))
p=[0,0]+p
x=0
while x<10000:
    if p[x]!=0:
        for y in range(2*x,1000000,x):
            p[y]=0
    x+=1    
primes=set()
for x in p:
    if x!=0:
        primes.add(x)
def parts(n):
    a=[]
    sn =str(n)
    for i in range(1,len(sn)):
        a.append(int(sn[i:]))
        a.append(int(sn[:i]))
    a.append(n)
    return a
def c(n):
    for p in parts(n):
        if p not in primes:
            return False
    return True        
ans=0
for i in range(10,1000000):
    if c(i):
        ans+=i
print(ans)            
