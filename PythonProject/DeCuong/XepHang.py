# dem so cap nhin thay nhau
from queue import Queue, LifoQueue
if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    S = LifoQueue()
    
    res = 0
    for x in a:
        while S.qsize() > 0 and S.queue[-1][0] <x :
            res+=S.get()[1]
        
        if (S.qsize()  > 0 and S.queue[-1][0] == x) :
            res += S.queue[-1][1] + (S.qsize() > 1)
            S.queue[-1][1] += 1
        else : res += S.qsize() > 1; S.put([x,1]);
    
    print(res)

        