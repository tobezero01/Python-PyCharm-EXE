import math
# cong 3 da thuc
class DT :
    def __init__(self,a):
        self.a = a
    
    def Add(self,other) :
        b=[0]+max(len(self.a,other.a))
        for i in enumerate(self.a) : 
            b[i] +=self.a[i]
        for i in enumerate(other.a):
            b[i] += other.b[i]
        return DT(b)
        
    def rg(self) :
        while len(self.a) > 0 and self.a[-1] == 0 : self.a.pop()
    
    def str(self) :
        self.rg()
        return " ".join([str(x) for x in self.a])
        
if __name__ == "__main__":
    n = input()
    a = list(map(float,input().split()))
    p = DT(a)
    n = input()
    a = list(map(float,input().split()))
    q = DT(a)
    n = input()
    a = list(map(float,input().split()))
    r = DT(a)
    print(p,q,r,p+q+r,sep = "\n")