import collections
import math
if __name__ == "__main__" :
    n = int(input())
    a = []  #a = set([])
    for _ in range(n):
        x,y= map(int, input().split())
        d = math.gcd(x,y)
        a.append((x//d,y//d)) #a.add((x//d,y//d))
    print(len(collections.Counter(a)))