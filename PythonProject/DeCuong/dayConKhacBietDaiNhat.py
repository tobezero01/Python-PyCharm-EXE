# Đọc số phần tử của dãy
n = int(input())

# Đọc dãy số
arr = list(map(int, input().split()))

# Khởi tạo dictionary để lưu trữ vị trí xuất hiện gần nhất của mỗi phần tử trong dãy
last_seen = {}

# Khởi tạo biến lưu trữ độ dài của dãy con liên tục
max_length = 0

# Khởi tạo biến lưu trữ vị trí bắt đầu của dãy con hiện tại
start_index = 0

# Duyệt qua từng phần tử trong dãy
for i in range(n):
    # Nếu phần tử đã xuất hiện trước đó và vị trí xuất hiện gần nhất lớn hơn hoặc bằng vị trí bắt đầu của dãy con hiện tại
    if arr[i] in last_seen and last_seen[arr[i]] >= start_index:
        # Cập nhật vị trí bắt đầu của dãy con hiện tại
        start_index = last_seen[arr[i]] + 1

    # Cập nhật vị trí xuất hiện gần nhất của phần tử
    last_seen[arr[i]] = i

    # Cập nhật độ dài của dãy con liên tục
    max_length = max(max_length, i - start_index + 1)

# In ra độ dài của dãy con liên tục dài nhất
print(max_length)
#12
#4 7 2 8 4 8 3 2 4 9 3 6