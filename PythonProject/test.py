# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
a = [3,7,2,[1,4],"xau"]
print(a)
print(*a)
print(a[-1])
print(*a)
print("----------------------------------------------")
b = [3,7,2,1,4.5,5,4,32,332,32]
print(b[3:5])
print(b[-5:-3])
print(b[:4])
print(b[2:])
print(b[3:8:2])
print(b[::2])
print(b[1::2])        #lay cach deu 
print(b[::-1])    #dảo dãy
print("----------------------------------------------")

c = list(range(3,10,2))
print(c)
c= list(range(3,10))
print(c)
c= list(range(10))
print(c)
c= list(range(10,0,-1))
print(c)
print("----------------------------------------------")

def bp(x):return x*x

import math
d = list(range(1,10,2))
print(d)
e = list(map(math.sqrt,d))
print(e)
f = list(map(bp,d))
print(f)
g = list(map(lambda x:x+1,d))
print(g)
print(sum(d))
h = list(filter(lambda x:x%3 == 0,d ))
print(h)

print("----------------------------------------------")

k = [5,7,2,8]
for x in k : print(x,end = " ")
print()
for i,x in enumerate(k) : print(i,x)
s = 0
for i,x in enumerate(k,1) : s+=x*i
print(s)