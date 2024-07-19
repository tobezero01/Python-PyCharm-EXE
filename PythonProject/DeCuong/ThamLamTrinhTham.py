#http://laptrinhonline.club/problem/tichpxtrinhtham
from queue import PriorityQueue

if __name__ == '__main__':
    Q = PriorityQueue()
    n, k = map(int, input().split())
    
    for i, x in enumerate(input().split(), 1):
        Q.put((-int(x), i))
        
        if i >= k:
            while i - Q.queue[0][1] >= k:
                Q.get()
            print(-Q.queue[0][0], end=" ")


# class elem :
#     def __init__(self,g,v) : self.g = g,self.v = v
#     def __lt__(self,other) : return self.g > other.g
    
# if __name__ == "__main__":
#     Q = PriorityQueue()
#     n, k = map(int, input().split())   
#     for i,x in enumerate(input().split(),1): 
#         Q.put(elem(int(x),i))
#         if i >= k :
#             while i - Q.queue[0].v >= k : Q.get()
#             print(Q.queue[0].g, end=" ")