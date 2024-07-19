import queue
# Định nghĩa lớp Canh với các thuộc tính dau, cuoi, trongso
class Canh:
    def __init__(self, dau, cuoi, trongso):
        self.dau = dau
        self.cuoi = cuoi
        self.trongso = trongso

    # Định nghĩa phương thức so sánh nhỏ hơn để sử dụng trong hàng đợi ưu tiên
    def __lt__(self, other):
        return self.trongso < other.trongso

n, m = map(int, input().split())
res = 0
a = []
# Nhập thông tin về các cạnh và thêm chúng vào danh sách a dưới dạng các đối tượng Canh
for _ in range(m):
    dau, cuoi, trongso = map(int, input().split())
    a.append(Canh(dau, cuoi, trongso))

q = queue.PriorityQueue()
for c in a:
    q.put(c)

# Khởi tạo mảng d để lưu trữ thông tin về các thành phần liên thông của đồ thị
d = [0] * (m + 5)

# Hàm tìm gốc của thành phần liên thông
def find(x):
    while d[x]:
        x = d[x]
    return x

# Thực hiện thuật toán Kruskal để tìm cây khung có trọng số nhỏ nhất
while not q.empty():
    c = q.get()
    x = find(c.dau)
    y = find(c.cuoi)
    if x != y:
        res += c.trongso
        d[x] = y

print(res)
