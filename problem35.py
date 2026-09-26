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
def c(n):
    a=[]
    for s in range(len(str(n))):
        sn=str(n)
        a.append(int(sn[s:]+sn[:s]))
    return set(a)    
x=0
for i in range(2,1000000):
    if len(c(i).intersection(primes))==len(c(i)):
        x+=1
x            
