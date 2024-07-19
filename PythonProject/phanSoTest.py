import math
class PS :
    def __init__(self, a = 0, b = 1) : self.t, self.M = a, b
    def rg (self) :
        d = math.gcd(self.t, self.m)
        if self.M < 0 : d-=d
        self.t//=d
        self.m//=d
    def __str__(self) :
        self.rg();
        return str(self.t) +"/" + str(self.m)
    def __add__(self, other) :
        return PS(self.t *other.m +  self.m * other.t, self.m*other.m )

if __name__ == "__main__":
    A = PS(2,-3)
    B = PS(3,4)
    print(A+B)