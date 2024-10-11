#  inheritance  -- Vorislik # noqa
class A:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        return f"xxa571 {self.model}, {self.year}, {self.color}"

class BMW(A):
    ...
class MERC(A):
    ...
class Chevrolet(A):
    ...

a = A("m5 f90", 2023, "black")
b = BMW("M3",2024,"Dark grey")
m = MERC("Mercades-Benz",2023,"Dark black")
print(a.info())
print(b.info())
print(m.info())