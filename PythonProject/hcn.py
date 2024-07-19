# xay dung trong lop 

class Diem:
    x,y = 0,0
    def __init__(self,u = 0, v = 0):
        self.x = u
        self.y = v
    def __str__(self):
        return "(%d,%d)" % (self.x, self. y)
    def kc(self, other): return ((self.x - other.x)**2 + (self.y - other.y)**2)**.5

class HinhTron :
    def nhap(self):
        x,y = map(float,input().split())
        self.o = Diem(x,y)
        self.r = float(input())
        x,y = map(float,input().split())
        self.M = Diem(x,y)
    
    def Tim(self) :
        B = self.O
        C = self.M
        if self.M.kc(B) > self.r :
            while (B.x - C.x)> 1e-4 or (B.y - C.y) > 1e-4 :
                D = Diem((B.x + C.x)/2,(B.y + C.y)/2)
                if D.kc(self.O) > self.r : C =D
                else: B = D
        else : B =self.M
        return B
    def sol(self) :
        self.nhap()
        print(self.Tim())
                
            
            
        
if __name__ == '__main__':
    ht = HinhTron()
    ht.sol()
    