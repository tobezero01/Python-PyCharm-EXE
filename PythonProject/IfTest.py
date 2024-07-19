# test lenh dieu khien if

# de baif dem so nghiem phuong trinh trung phuong -> at^2 +bt + c = 0
import math
def dem(t) : 
    if t>0 : return 2
    return t == 0
def pttp(a,b,c) :
    if a == b==c ==0 : return "vo so nghiem"
    d = b*b - 4*a*c
    if a==b==0 or d < 0 : return 0
    
    if a==0 : return dem(-c/b)
    if d==0 : return dem(-b/2/a)
    d = math.sqrt(d)
    return dem((-b-d)/2/a) + dem((-b+d)/2/a)

if __name__ == "__main__" :
    a,b,c = map(float,input().split())
    print(pttp(a,b,c))
    
# giai phuong trinh trung phuong 

def dem1(t) : 
    if t>0 : return [-math.sqrt(t),math.sqrt(t) ]
    if t == 0 : return [t]
    return []
def pttp(a,b,c) :
    if a == b==c ==0 : return "vo so nghiem"
    d = b*b - 4*a*c
    if a==b==0 or d < 0 : return 0
    
    if a==0 : return dem(-c/b)
    if d==0 : return dem(-b/2/a)
    d = math.sqrt(d)
    return dem((-b-d)/2/a) + dem((-b+d)/2/a)

if __name__ == "__main__" :
    a,b,c = map(float,input().split())
    print(pttp(a,b,c))