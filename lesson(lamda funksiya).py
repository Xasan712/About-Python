# high_ord_func = lambda x, func: x + func(x)
#
# print(high_ord_func(2,lambda x: x*x))
# print(high_ord_func(2,lambda x: x+3))
#
#


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# toq = list(filter(lambda a:(a % 2 ==0),a))   # noqa
# juft = list(filter(lambda a:(a % 2 ==1),a))  # noqa
# print(toq)
# print(juft)
# 1. python def function

# def func(n):
#     return n
# print(func("pdp"))

# 2. python lambda function
# x = lambda n: n
# print(x("pdp"))

# x = lambda n: n + 2
#
# print(x(10))
"""
(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3
"""
# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
#
# print(full_name('guido', 'van rossum'))

# lambda x, y: x + y
# _(1, 2)


# x = (lambda x, y: x + y)(70, 30)
# print(x)
#
# high_ord = lambda x, func: x + func(x)
# print(high_ord(2, lambda x: x * x))
# print(high_ord(2, lambda x: x + 3))

# standard = max() min() map() filter() sort() sorted() in with lambda

# Max = lambda x, y: x if (x > y) else y
# print(Max(7, 9))

# students = ["aziz", "ali", "dilshod", "bobur", "malika"]
# up = list(filter(lambda students: (students[-0] == 'a'), students))
# print(up)

# example
# 1 list barcha toq sonlarni chop etsin => in lambda orqali
# 2 list barcha juft sonlarni chop etsin => in lambda orqali

num = [10, 2, 7, 8, 6, 4, 3, 1, 5, 9]
# num.sort()
# son = (lambda x: x)(num)
# print(son)

# HOMETASK
# standard = max() min() map() filter() sort() sorted() lambda bilan ishlatib kelish


# sort()
# sortlist = lambda x: (sorted(x) for x in x)
# print(sortlist(num))

# max()
# Max = lambda x, y: x if (x > y) else y
# print(Max(7, 9))

# min()
# Min = lambda x, y: x if (x < y) else y
# print(Min(7, 9))

# map()
# n = (1, 2, 3, 4)
# s = map(lambda x: x + x, n)
# print(list(s))

# filter()
# students = ["Xasan", "Ezoza", "Bunyod", "bobur", "Durdona"]  # noqa
# up = list(filter(lambda students: (students[-0] == 'a'), students))
# print(up)

