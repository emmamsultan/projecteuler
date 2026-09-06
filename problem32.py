def pan(a,b):
    c=a*b
    t=sorted(str(a)+str(b)+str(c))
    if t==['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False
ans=set()
for a in range(10000):
    for b in range(a,10000):
        if pan(a,b):
            ans.add(a*b)
sum(ans)
