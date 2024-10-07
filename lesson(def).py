# def add(*a):
#     d = 0
#     for i in a:
#         d += i
#     return d
# print(add(1,2,3,4))

#tasks
# 1- task
# def digit(k,n):
#     if len(str(k))>n:
#         return 2
#     if len(str(k))<n:
#         return -1
# print(digit(123456,4))
# print(digit(12,3))
# 2- task
# def isPalindrome(n):
#     d = str(n)
#     f = d == d[::-1]
#     return  f
# n = 12356
# print(isPalindrome(n))
# 3-task

# def fact(n):
#     d = 1
#     for i in range(1,n):
#        d *= i
#     return d
# print(fact(5))


# hometask
a = """
1. Berilgan n sonini raqamlar yigindisini topuvchi funksiya yarating.
2. Berilgan n sonini raqamlar orasidan eng kichigini topuvchi funksiya tuzing.
3. Berilgan n sonini raqamlar soni va kopaytmasini topuvchi funksiya yarating.
4. Oy raqami berilgan. Shu oyda nechta kun borligini chiqaruvchi funksiya tuzing.
5. a va b sonlar berilgan. Ekranga b marta a ni chiqaruvchi funksiya yarating.
6. n soni berilgan. Ushbu songa mos karra jadval chiqaruvchi funkisya yarating.
"""

# task - 1
# def uzunlk(n):
#    s = []
#    for i in str(n):
#        s.append(int(i))
#    y = 0
#    for x in s:
#        y +=x
#    return y
# print(uzunlk(54564))

# task - 2
# def vsmall(n):
#     s = []
#     for i in str(n):
#         s.append(int(i))
#     d = s[0]
#     for x in s:
#         if x < d:
#             d = x
#     return d
# print(vsmall(654465665))

# task - 3
# def ks(n):
#     d = len(str(n))
#     s = []
#     for i in str(n):
#        s.append(int(i))
#     f = 1
#     for i in s:
#         f *= i
#     return d,f
# print(ks(4646))

# task - 4
# def month(n):
#     to = [1, 3, 5, 7, 8, 10, 12]
#     t = [4, 6, 9, 11]
#     ten = [2]
#     if n in to:
#         print(f"Bu oyda 31 kun bor")
#     if n in t:
#         print(f"Bu oyda 30 kun bor")
#     if n in ten:
#         print(f"Bu oyda 28-29 kun bor")
# month(5)

# task - 5
# def ba(a,b):
#     for i in range(1,b+1):
#         print(a)
# ba(9,4)

# task - 6
# def karraj(n):
# #     for i in range(1, 11):
# #         s = n * i
# #         print(f"{n} x {i} = {s}")
# # karraj(45)

















