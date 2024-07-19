from queue import Queue
if __name__  == "__main__":
    t = int(input())
   
    while t > 0 : 
        Q = Queue()
        for x in ["dangdungcntt", "tienquanutc", "quang123", "maianh", "nguyenminhduc2820"] : Q.put([x,1])
        n = int(input())
        while (n > Q.queue[0][1]) :
        
            n-= Q.queue[0][1]
            x = Q.get()
            Q.put(x)    
            Q.queue[-1][1] *= 2                
        print(Q.queue[0][0])
        t-=1
    
    