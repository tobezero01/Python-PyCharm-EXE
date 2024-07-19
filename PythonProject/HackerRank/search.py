# n,x = map(int,input().split())
# a= list(map(int,input().split()))
# ans = 0
# a.sort()
# l,r = 0 , n-1 
# while l <= r :
#     if a[l] + a[r] <= x : 
#         ans += 1
#         r -= 1
#         l += 1
#     else : 
#         ans += 1
#         r -= 1
# print(ans)
def f(n, g) :
    return g(n)
print(f(3,lambda x : x**2))
