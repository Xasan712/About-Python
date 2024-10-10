# class MyClass:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def info(self):
#         return self.name, self.age, self.address
#
# obj = MyClass("Bob", 17, "New York")
# print(obj.info())
# obj1 = MyClass("Marina", 17, "London")
# print(obj1.info())
"""
Calculate class bor unda + - * / // % methods bor
"""


class MyClass:
    def __init__(self, num, num2):
        self.num = num
        self.num2 = num2

    def multiply(self):
        d = self.num2 * self.num
        return f"{self.num} * {self.num2} = {d} "
    def division(self):
        f = self.num2 / self.num
        return f"{self.num} / {self.num2} = {f} "
    def minus(self):
        e = self.num2 - self.num
        return f"{self.num} - {self.num2} = {e} "
    def plus(self):
        p = self.num2 + self.num
        return f"{self.num} + {self.num2} = {p} "
    def division2(self):
        g = self.num2 // self.num
        return f"{self.num} // {self.num2} = {g} "
ss = MyClass(1,2)
print(ss.multiply())
print(ss.division())
print(ss.plus())
print(ss.minus())
print(ss.division2())

