from queue import Queue
import math
import sys
def Dua_ngua():
    n,*a = map(int,sys.stdin.read().split())
    a = [x+1 for x in a]
    A = [[1]*(n+4),[1]*(n+4)]
    for i in range(n): A.append([1,1]+[0]*n+[1,1])
    A=A+[[1]*(n+4),[1]*(n+4)]

    Q=Queue()
    sx1,sy1 = sx1+1,sy1+1
    sx2,sy2 = sx2+1,sy2+1
    fx,fy = fx+1,fy+1
    A[fx][fy] = 1
    Q.put((fx,fy))
    while(Q.qsize()>0 or A[sx1][sy1] == 0 and A[sx2][sy2] == 0):
        fx,fy = Q.get()
        # Các bước đi có thể của quân mã
        for i,j in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]:
            if A[fx+i][fy+j]==0:
                A[fx + i][fy + j] = A[fx][fy]+1
                Q.put((fx+i,fy+j))
    A[sx1][sy1] -= 1
    A[sx2][sy2] -= 1
    z = A[sx1][sy1] if A[sx1][sy1] >= 0 else math.inf
    t = A[sx2][sy2] if A[sx2][sy2] >= 0 else math.inf
    if z==t : print("0\n%d %d"%(A[sx1][sy1], A[sx2][sy2]))
    elif z>t : print("2\n%d %d"%(A[sx1][sy1], A[sx2][sy2]))
    else : print("1\n%d %d"%(A[sx1][sy1], A[sx2][sy2]))
if __name__ == '__main__':
    Dua_ngua()
 
 
#  from queue import Queue

# def Buoc_di_ngan(n, sx, sy, fx, fy):
#     A = [[1]*(n+4),[1]*(n+4)]
#     for i in range(n):
#         A.append([1,1]+[0]*n+[1,1])
#     A=A+[[1]*(n+4),[1]*(n+4)]

#     Q=Queue()
#     sx,sy = sx+1,sy+1
#     fx,fy = fx+1,fy+1
#     A[sx][sy] = 1
#     Q.put((sx,sy))
#     while(Q.qsize()>0 or A[fx][fy] == 0):
#         u,v = Q.get()
#         for i,j in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]:
#             if A[u+i][v+j]==0:
#                 A[u + i][v + j] = A[u][v]+1
#                 Q.put((u+i,v+j))
#     return A[fx][fy]-1
# if __name__ == '__main__':
#     n = int(input())
#     sx1, sy1 = map(int,input().split())
#     sx2, sy2 = map(int,input().split())
#     fx, fy = map(int,input().split())
#     Ma_1 = Buoc_di_ngan(n, sx1, sy1, fx, fy)
#     Ma_2 = Buoc_di_ngan(n,  sx2, sy2, fx, fy)
#     if Ma_1 < Ma_2:
#         print('1')
#     elif Ma_2 < Ma_1:
#         print('2')
#     else:
#         print('0')
#     print(f'{Ma_1} {Ma_2}')
