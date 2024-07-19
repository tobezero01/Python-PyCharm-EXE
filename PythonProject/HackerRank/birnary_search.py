# from functools import cmp_to_key
# def binary_search(arr, target, low, high):
#     # Kiểm tra điều kiện dừng
#     if low <= high:
#         mid = (low + high) // 2

#         # Nếu phần tử ở giữa là phần tử cần tìm, trả về chỉ số
#         if arr[mid] == target:
#             return True
#         # Nếu phần tử ở giữa lớn hơn phần tử cần tìm, tìm kiếm bên trái
#         elif arr[mid] > target:
#             return binary_search(arr, target, low, mid - 1)
#         # Nếu phần tử ở giữa nhỏ hơn phần tử cần tìm, tìm kiếm bên phải
#         else:
#             return binary_search(arr, target, mid + 1, high)
#     else:
#         # Trả về -1 nếu không tìm thấy phần tử trong mảng
#         return False

# def cmp1(m,n):  
#     if m < n : return -1
#     elif m > n : return 1
#     else : return 0
# if __name__ == "__main__":
#     arr = [2,2324,43,55,4,46,464646,66,4646,46,46,4,64,64644,34]
#     n = len(arr)
#     x= 4646
#     arr.sort(key = lambda x: x)
#     if binary_search(arr,0,n-1, x) : 
#         print("ok")
#     else : print("not found")
#     #a.sort(key = cmp_to_key(cmp1))
    
    
# if __name__ == "__main__":
#     a = [2, 2324, 43, 55, 4, 46, 464646, 66, 4646, 5, 46, 4, 64, 64644, 34]

#     # Sắp xếp chẵn trước, lẻ sau, chẵn tăng dần, lẻ giảm dần
#     a.sort(key=lambda x: (x % 2, x if x % 2 == 0 else -x))

#     print(a)
def binary_search(arr,l,r,x) : 
    while l <= r : 
        m = (l + r) // 2
        if arr[m] == x : return True
        elif arr[m] > x : r = m -1
        else : l = m + 1
    else : return False 
 
def binary_search_recursive(arr, target, low, high):
    # Kiểm tra điều kiện dừng
    if low <= high:
        mid = (low + high) // 2

        # Nếu phần tử ở giữa là phần tử cần tìm, trả về chỉ số
        if arr[mid] == target:
            return True
        # Nếu phần tử ở giữa lớn hơn phần tử cần tìm, tìm kiếm bên trái
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        # Nếu phần tử ở giữa nhỏ hơn phần tử cần tìm, tìm kiếm bên phải
        else:
            return binary_search_recursive(arr, target, mid + 1, high)
    else:
        # Trả về -1 nếu không tìm thấy phần tử trong mảng
        return False

# Ví dụ sử dụng
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
if binary_search_recursive(arr,target, 0, len(arr) -1): print("OK")
else : print("ERROR")
if binary_search(arr,0, len(arr) -1, target): print("OK")
else : print("ERROR")
# result = binary_search_recursive(arr, target, 0, len(arr) - 1)

# if result != -1:
#     print(f"Phần tử {target} được tìm thấy tại vị trí {result}.")
# else:
#     print(f"Phần tử {target} không có trong mảng.")
       