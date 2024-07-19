# if __name__ == "__main__":
#     a, b, c = list(map(int, input().split()))
#     m = int(input())
#     res = 0
#     while m > 0 :
#         i = m // 3
#         if i > c:
#             m -= 3 * c
#             res += c
#             break
#         else:
#             m -= 3 * i
#             res += i
#             h = m // 2
#             if h > b:
#                 m -= 2 * b
#                 res += b
#                 break
#             else:
#                 m -= 2 * h
#                 res += h + m
#                 break
#     if m > 0:
#         print("KHONG DOI DUOC")
#     else:
#         print(res)
