import collections

def myFunction(a,b) : 
    #c = [x for x in a if x in b] 
    T = collections.Counter(b)
    c = []
    for x in a :
        if x in T.keys() :
            if T[x] > 0 : T[x] -= 1;c.append(x)
    return c
def chanLe(a) :
    b =[]; c = []
    for x in a :
        if x %2==0 : b.append(x) 
        elif x %2==1 : c.append(x)
    return b,c 
def bd(a) :
    for x in range(len(a)) :a[x]+=1
    
if __name__ == "__main__":
    a = [2,3,4,5,6,7,8,9,10,11,12]
    b = [1,2,3,4,5,6,8,8,9]
    c= myFunction(a,b)
    print(*c)
    
    d,e = chanLe(a)
    print(*d)
    print(*e)
    
    bd(a)
    print(*a)
    
    
    
    