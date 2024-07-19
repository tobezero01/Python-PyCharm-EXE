from queue import Queue
import math
def search(n,s) :
    res = {n}
    s.put(n)
    
    while s.qsize() > 0 :
        x = s.get()
        m = int(x**0.5)+1
        for a in range(1,m)  :
            if x%a == 0:
                b = x//a
                y = (a-1)*(b+1)
                if y not in res :
                    res.add(y)
                    s.put(y)
    return res

if __name__ == "__main__":
    n = int(input())
    s = Queue()
    print(*search(n, s))