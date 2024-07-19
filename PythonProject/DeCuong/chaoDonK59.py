# chao don k59, duyet trai phai tim cao hon gan nhat
from queue import Queue, LifoQueue
import math
def tim(a,b) :
    S = LifoQueue()
    S.put((math.inf, -1))
    L = [0]*n
    for i,x in enumerate(a):
        while S.queue[-1][0] <=x : S.get()
        L[i] = S.queue[-1][1]
        S.put((x,i))
    return L
if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    L = tim(a,n)
    R = tim(a[::-1], n)
    R = [n-x-1 if x>=0 else x for x in R][::-1]
    for i in range(n) : 
        if L[i] == -1 or R[i] == -1 : print(L[i]+ R[i] +1 , end = " ")
        else : print(L[i] if L[i] < R[i] else R[i], end = " ")
    print()
    print(L)
    print(R)