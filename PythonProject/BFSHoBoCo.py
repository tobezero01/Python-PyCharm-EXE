from queue import Queue, LifoQueue

if __name__ == "__main__":
    
    S = LifoQueue()
    
    for x in [6,4,3,2,3,2,32 ] : S.put(x)
    print(S.queue[-1])
    print(S.queue)
    while S.qsize() > 0  : print(S.get())
    
    