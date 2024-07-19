import collections
#quan tuong thu vi
if __name__ == '__main__' :
    n = int(input())
    a = []
    for _ in range(n):
        x,y= map(int, input().split())
        a.append((x,y))
    d = [x+y for x,y in a]
    e = [x-y for x,y in a]
    
    D = collections.Counter(d)
    E = collections.Counter(e)
    res = 0
    for x in D.values():
        res += x*(x-1)//2
    for X in E.values():
        res += x*(x-1)//2
    print(res)
     