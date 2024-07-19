from queue import PriorityQueue

# Khởi tạo hàng đợi ưu tiên cho phần bên trái và phải
L = PriorityQueue()
R = PriorityQueue()
L.put(-7)
L.put(-2)
R.put(1)
R.put(4)
R.put(8)
R.put(8)

# Hiển thị trạng thái ban đầu
print("Priority Queue of L:", list(L.queue))
print("Priority Queue of R:", list(R.queue))

# Thực hiện lệnh a = L.get(), b = R.get(), và sau đó đặt lại vào hàng đợi
a = L.get()
b = R.get()
R.put(-a)
L.put(-b)

# Hiển thị trạng thái sau khi thực hiện lệnh
print("Priority Queue of L:", list(L.queue))
print("Priority Queue of R:", list(R.queue))

h = L.get()
k = R.get()
R.put(-h)
L.put(-k)

# Hiển thị trạng thái sau khi thực hiện lệnh
print("Priority Queue of L:", list(L.queue))
print("Priority Queue of R:", list(R.queue))
print(-L.queue[0])