from math import *
import collections
# tinh dien tich tu giac
diem = collections.namedtuple("diem", "x,y")
def dt(a,b):
    return a.x *b.y - a.y *b.x
if __name__ == "__main__" :
    A = []
    for i in range(4):
        x,y = map(float, input().split())
        A.append(diem(x,y))
    A.append(A[0])
    s=0
    for u,v in zip(A, A[1:]) :
        s+=dt(u,v)
    print("%.3f"%(abs(s)/2))