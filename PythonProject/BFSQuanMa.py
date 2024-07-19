# http://laptrinhonline.club/problem/quanma
from queue import Queue
def fun(n,m,sx,sy,fx,fy):   
    A = [[1]*(m+4),[1]*(m+4)]
    for i in range(n):
        A.append([1,1]+[0]*m+[1,1])
    A=A+[[1]*(m+4),[1]*(m+4)]
    Q=Queue()
    sx,sy = sx+1,sy+1
    fx,fy = fx+1,fy+1
    A[sx][sy] = 1
    Q.put((sx,sy))
    while(Q.qsize()>0 or A[fx][fy] == 0):
        u,v = Q.get()
        for i,j in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]:
            if A[u+i][v+j]==0:
                A[u + i][v + j] = A[u][v]+1
                Q.put((u+i,v+j))
    print()
    print(A[fx][fy]-1)
if __name__ == '__main__':
    n,m = map(int,input().split())
    sx,sy=map(int,input().split())
    fx,fy=map(int,input().split())
    fun(n,m,sx,sy,fx,fy)
# # 2
# from collections import deque

# # Hàm kiểm tra xem một ô có nằm trong bàn cờ không
# def is_valid(x, y, n):
#     return 0 <= x < n and 0 <= y < n

# # Hàm tính bước đi ngắn nhất của quân mã cờ vua
# def min(n, x1, y1, x2, y2):
#     dx = [2, 1, -1, -2, -2, -1, 1, 2]
#     dy = [1, 2, 2, 1, -1, -2, -2, -1]

#     visited = [[False for _ in range(n)] for _ in range(n)]

#     Q = deque()
#     Q.append((x1, y1, 0))
#     visited[x1][y1] = True

#     while Q:
#         x, y, steps = Q.popleft()

#         if x == x2 and y == y2:
#             return steps

#         for i in range(8):
#             new_x = x + dx[i]
#             new_y = y + dy[i]

#             if is_valid(new_x, new_y, n) and not visited[new_x][new_y]:
#                 visited[new_x][new_y] = True
#                 Q.append((new_x, new_y, steps + 1))

#     return -1  # Trả về -1 nếu không thể tới được vị trí đích

# # Sử dụng hàm để tính toán bước đi ngắn nhất của quân mã cờ vua
# n = 8  # Kích thước của bàn cờ
# x1, y1 = 4, 6  # Vị trí ban đầu
# x2, y2 = 2, 4  # Vị trí đích
# result = min(n, x1, y1, x2, y2)
# print(result)
                    