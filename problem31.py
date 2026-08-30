def ot(n):
    return n//2 +1
def otf(n):
    a=0
    for i in range(0,n//5 +1):
        a+=ot(n-5*i)
    return a
def otft(n):
    a=0
    for i in range(0,n//10 +1):
        a+=otf(n-10*i)
    return a
def otftt(n):
    a=0
    for i in range(0,n//20 +1):
        a+=otft(n-20*i)
    return a
def otfttf(n):
    a=0
    for i in range(0,n//50 +1):
        a+=otftt(n-50*i)
    return a
def otfttfo(n):
    a=0
    for i in range(0,n//100 +1):
        a+=otfttf(n-100*i)
    return a
print(otfttfo(200)+1)
