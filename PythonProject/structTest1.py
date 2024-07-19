#vidu ve trao giai chung ket marathon
from math import *
from collections import *
sv = namedtuple("sv", "ten diem")
if __name__ == "__main__" :
    a = []   # khoa dien
    b = []   # khoa khac
    n = int(input())
    for _ in range(n) :
        t,d,k = input().rsplit(" ", 2)
        if k== 'DDT' : a.append(sv(t,int(d)))
        else : b.append(sv(t,int(d)))
        
    a.sort(key=lambda x : x.diem, reverse = True)
    print("Giai nhat %s"% a[0].ten)
    print("Giai nhi %s"% a[1].ten)
    print("Giai ba %s"% a[2].ten)
    
    z = max(b, key = lambda x : x.diem)
    print("Giai giao luu %s" % z.ten)
    
    
    
    