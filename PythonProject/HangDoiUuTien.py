from queue import PriorityQueue
if -__name__ == '__main__':
    n,k = map(int,input().split(''))
    arr = list(map(int, input().split()))
    res = 0
    Q = PriorityQueue()
    for x in arr : Q.put(x)
    while Q.qsize() > 1:   
        for i in range(min(Q.qsize(),k)):
            a = 0
            a += Q.get()
            res += a 
            Q.put(a )
    print(res)
