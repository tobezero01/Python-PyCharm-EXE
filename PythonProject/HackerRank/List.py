# n = int(input())
# a = list(map(int,input().split()))
# cnt = [0] * 1000
# for x in a :
#     cnt[x] +=1
# cnt2 = cnt.copy()
# for x in  a : 
#     if cnt[x] != 0 :
#         print(x , cnt[x] )
#         cnt[x] = 0
# print()
# l, r = min(a), max(a)
# for i in range(l, r+1):
#     if cnt2[i] != 0 :
#         print(i, cnt2[i] )

# print()

# from sys import stdin
# a = []
# for s in stdin :
#     a += list(map(int,s.split()))
    

# mang cong don
# n = int(input())
# a = list(map(int,input().split()))
# F = [0] *n
# F[0] = a[0]
# for i in range(1,n):
#     F[i] = F[i - 1] + a[i]
# l,r = 3,5
# print(F[r] - F[l-1] )

#sang so nguyen to
# O(n*loglogn)
# goi tat ca cac so tu o den n la soo nguyen to
#boi cua 1 so nguyen to khong phai la  so nguyen to
from math import *
# prima  = [True] * (10**6 +1)

# def sieve() :
#     prima[0], prima[1] = False,False
#     for i in range(2, isqrt(10**6 +1)):
#         if prima[i] :
#             for j in range(i *i , 10**6 +1,i):
#                 prima[j] = False
# if __name__ == "__main__" :
#     sieve()
#     for i in range(1000):
#         if prima[i] :
#             print(i, end=' ')
 
 
# tinh n! chia du cho 10**9 + 1
f = [0] * (10**6 +1)
def init() :
    f[0] = 1
    for i in range(1, 10**6 + 1) :
        f[i] = f[i-1] *i
        f[i] %= (10**6 + 1)
if __name__ == '__main__':
    init()
    t = int(input())
    for i in range(t) :
        n = int(input())
        print(f[n], end = ' ')	