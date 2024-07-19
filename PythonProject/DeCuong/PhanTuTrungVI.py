# from queue import PriorityQueue
# if __name__ == '__main__':
#     L = PriorityQueue()
#     R = PriorityQueue()
#     n = int(input())
#     for i,x in enumerate(map(int,input().split()),1):       
#         if (i %2 == 1) : L.put(-x)
#         else : R.put(x)
#         if i > 1 and -L.queue[0] > R.queue[0] : 
#             a = L.get()
#             b = R.get()
#             R.put(-a)
#             L.put(-b)
#         print(-L.queue[0], end=" ")
            

from queue import PriorityQueue

# if __name__ == '__main__':
#     # Khởi tạo hàng đợi ưu tiên cho phần bên trái và phải
#     L = PriorityQueue()
#     R = PriorityQueue()
    
#     # Nhập số lượng phần tử trong dãy
#     n = int(input())
    
#     # Duyệt qua từng phần tử trong dãy
#     for i, x in enumerate(map(int, input().split()), 1):       
#         # Nếu là phần tử ở vị trí lẻ, thêm vào hàng đợi ưu tiên của bên trái (đảo dấu để sắp xếp giảm dần)
#         if i % 2 == 1:
#             L.put(-x)
#         # Nếu là phần tử ở vị trí chẵn, thêm vào hàng đợi ưu tiên của bên phải
#         else:
#             R.put(x)
        
#         # Nếu đã có ít nhất 2 phần tử và phần tử mới thêm vào bên trái lớn hơn phần tử bên phải
#         if i > 1 and -L.queue[0] > R.queue[0]:
#             # Hoán đổi phần tử giữa bên trái và bên phải
#             a = L.get()
#             b = R.get()
#             R.put(-a)
#             L.put(-b)
        
#         # In ra trung vị tại thời điểm hiện tại
#         print(-L.queue[0], end=" ")


l = PriorityQueue()
r = PriorityQueue()
n = int(input())
    
for i, x in enumerate(map(int, input().split()), 1):
    if i % 2 == 1:
        l.put(-x)
    else:
        r.put(x)

print("Priority Queue of L:", list(l.queue))
print("Priority Queue of R:", list(r.queue))

# 9
# 7 4 2 1 6 8 5 8 7    
# 7 4 4 2 4 4 5 5 6    
