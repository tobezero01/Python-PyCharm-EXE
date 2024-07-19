from queue import Queue

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

s = Queue()
res = 0

for i in range(1,n + k):
    if i <= n: x = a[i - 1]
    else: x = 0
    s.put(x)
    
    while s.qsize() > k: s.get()        
    
    t = 0
    while not s.empty() and t + s.queue[0] <= m:
        t += s.queue[0]
        s.get()
    
    if not s.empty():
        s.queue[0] -= m - t
        t = m
    
    res += t

print(res)

