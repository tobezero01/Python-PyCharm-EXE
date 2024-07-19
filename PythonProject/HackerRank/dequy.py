# def f(n) :
#     if n != 0 :
#         f(n//16)
#         r = n%16
#         if r < 10 : print(r, end = '')
#         else : print(chr(r+55), end='')
# if __name__ == '__main__':
#     n = int(input())
#     f(n)

# tim chu so lon nhat cua 1 so
# def maxso(n) :
#     if n < 10 : return n
#     else : 
#         return max(n%10, maxso(n//10))
# if __name__ == '__main__':
#     n = int(input())
#     print(maxso(n))


# in so 2 chieu
# def inso(n) :
#     if n < 10 : print(n, end=' ')
#     else :
#         print(n//10, end=' ')
#         inso(n//10)
        
# def inso2(n) :
#     if n < 10 : print(n, end=' ')
#     else : 
#         inso2(n//10)
#         print(n//10, end=' ')
        
# if __name__ == '__main__' :
#     n = int(input())
#     inso(n)
#     print()
#     inso2(n)
    


# def tongLe(n) :
#     if n < 10 :
#         if n%2 == 1 :
#             return n
#         else : return 0
#     else :
#         if n%2 == 1 :            
#             return n%10+ tongLe(n//10)
#         else : tongLe(n//10)



# def ktSoChan(n) :
#     if n < 10 :
#         if n%2 == 1 :
#             return False
#         else : return True
#     else :
#         if(n%2 == 1) :
#             return False
#         else :
#             return ktSoChan(n//10)
# if __name__ == '__main__':
#     n = int(input())
#     if ktSoChan(n) : print("Yes")
#     else : print("no")



#dem so thao tac it nhat bien doi n ve \
# def f(n) :
#     if n==1 : return 0
#     else:
#         tt1,tt2,tt3 = 10**9,10**9,10**9
#         if n %2 == 0 : 
#             tt1 = 1+f(n//2)
#         if n %3 == 0 :
#             tt2 = 1+f(n//3)
#         if n > 1 :
#             tt3 = 1+f(n-1)
#         return min(tt1,tt2,tt3)
# if __name__ == "__main__": 
#     n = int(input())    
#     print(f(n))

lst = [1,2,3,4,5,6,7,8, 9, 10 ,11,12,13,14,14]
for i in lst : 
    print(i , end=" ")