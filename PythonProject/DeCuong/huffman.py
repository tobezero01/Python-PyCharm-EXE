#http://laptrinhonline.club/problem/tichpxhuffman
from queue import PriorityQueue
import collections
# Nhập xâu từ người dùng
s = input()
# Sử dụng Counter để đếm tần suất xuất hiện của mỗi ký tự trong xâu
dic = collections.Counter(s)
# Khởi tạo hàng đợi ưu tiên để sắp xếp theo tần suất xuất hiện
Q = PriorityQueue()
# Khởi tạo biến tổng số bit cần để mã hóa Huffman
res = 0
# Đưa tần suất xuất hiện của mỗi ký tự vào hàng đợi ưu tiên
for x in dic.values():
    Q.put(x)
# Xây dựng cây Huffman
print(list(Q.keys()))
# while Q.qsize() > 1:
#     # Lấy hai phần tử có tần suất nhỏ nhất ra khỏi hàng đợi
#     x = Q.get() + Q.get()
#     # Cộng vào tổng số bit
#     res += x
#     # Đưa tổng tần suất trở lại hàng đợi
#     Q.put(x)

# # In ra tổng số bit sau khi mã hóa Huffman
# print(res)


# nangcap in ra chuoi ma hoa dung cay (node)
# CODE = {}
# class node : 
#     def __init__(self,c,f,l = None,r = None) :
#         self.kt = c
#         self.ts = f
#         self.left = l
#         self.right = r   
#     def __lt__(self,other): return self.kt < other.kt

# def inorder(h,q = ""):
#     if h == None: return 
#     inorder(h.left, q +"\t\t")
#     print("%s%s - %d" % (q,h.kt,h.ts))
#     inorder(h.right, q +"\t\t")

# def getcode(h, q ="") :
#     if h.left == None : CODE = print(h.kt, q)
#     else :
#         getcode(h.left, q + "0")
#         getcode(h.right, q + "1")
        
# if __name__ == '__main__':
#     s = input()
#     Q = PriorityQueue()
#     dic = collections.Counter(s)
#     for k,v in dic.items(): Q.put(node(k,v))
    
#     while Q.qsize() > 1:
#         u = Q.get()
#         v = Q.get()
#         Q.put(node('$', u.ts  + v.ts, u,v))
#     root  = Q.get()
#     inorder(root)
#     getcode(root)
              