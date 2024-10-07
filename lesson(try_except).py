# try:
#     s = int(input("s:"))
#     n = int(input("n:"))
#     print(s // n)
# except ZeroDivisionError as p:
#     print(f"siz {p} xatolik qildingiz")
# except ValueError as d:
#     print(f"siz {d} xatolik qildingiz")

# def salom(name):
#     print(f'salom{name}')
# salom('anna')
#task-1
# def power(son):
#     return son**3
# print(power(4))
#task-2
# def power(son):
#     a = son**2
#     b = son**3
#     c = son**4
#     return f"{son} ning 2 darajasi {a},3 darajasi {b},4 darajasi {c}"
# print(power(4))
#task-3
# def orta_arifmetik(a, b):
#     return (a + b) / 2

# d = 10
# x = 20
# p = orta_arifmetik(d, x)
# print(f"{d} va {x} sonlarining o'rta arifmetigi: {p}")

#task -4 

# def numy(n):
#     f = 0
#     while n > 0:
#         yigindi += n % 10  
#         n = n // 10        
#     return f

# s= 12345
# d = numy(s)
# print(f"{s} raqamlari yig'indisi: {d}")

#task -5
# def teskari(n):
#     a = str(n)
#     return list(a[::-1])
# a = 12345
# print(teskari(a))    



# Hometask

# task - 1
# try:
#     def sortInc(a,b,c):
#         d = [a,b,c]
#         d.sort()
#         return d
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = int(input("c: "))
#     f = sortInc(a,b,c)
#     print(f)
# except ValueError as l:
#     print(f"siz {l} xatolik qildingiz!!!")       

# task - 2
# def ishora(n):
#     if n<0:
#         return '-1'
#     elif n>0:     
#         return '1'
#     elif n==0:
#         return '0'

# a = int(input("Num: "))
# print(ishora(a))    

# task - 3

# def sumRange(a,b):
#     d = 0
#     s = range(a,b)
#     if a<b :
#         for i in s :
#             d +=i
#         return d+b
#     elif a>b:
#         return 0
# e = int(input("A: "))
# l = int(input("B: "))   
# print(sumRange(e,l))

# task - 4
# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# s = int(input('N: '))
# print(even(s))

# task - 5
# def isSquare(k):   
#     if k < 0:
#         return False      
#     i = 0
#     while i * i <= k:
#         if i * i == k:
#             return True
#         i += 1
#     return False
# k = 25
# print(isSquare(k))


