import queue

n = int(input())
res = 0
Max = 0
a = [[] for i in range(n + 5)]
Q = queue.PriorityQueue()

for i in range(n):
    t, v = map(int, input().split())
    a[t].append(v)
    if Max < t:
        Max = t

for i in range(Max, 0, -1):
    for x in a[i]:
        Q.put(-x)
    if not Q.empty():
        res -= Q.get()

print(res)