#  inheritance  -- Vorislik # noqa
# class A:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def info(self):
#         return f"xxa571 {self.model}, {self.year}, {self.color}"
#
# class BMW(A):
#     ...
# class MERC(A):
#     ...
# class Chevrolet(A):
#     ...
#
# a = A("m5 f90", 2023, "black")
# b = BMW("M3",2024,"Dark grey")
# m = MERC("Mercades-Benz",2023,"Dark black")
# print(a.info())
# print(b.info())
# print(m.info())



# ----------------------------------------------------------------------------------------------------
class Car:
    def __init__(self,name,year,engine,petrol):
        self.name = name
        self.year = year
        self.engine = engine
        self.petrol = petrol
    def moving(self):
        if self.engine == True:
            print(f"{self.name} harakatlanayapti")  # noqa
        elif self.engine == False:
            print(f"{self.name} harakatlanmayapti")


class BMW(Car):
    def __init__(self, name, year, engine, color, speed, price, model, petrol):
        super().__init__(name, year, engine,petrol)
        self.color = color
        self.speed = speed
        self.price = price
        self.model = model



    def display(self):
        return f"name: {self.name} , year: {self.year} , engine: {self.engine}, color: {self.color}, speed: {self.speed}, price: {self.price}, model: {self.model} "
    def check(self):
        if self.petrol >0 and self.engine:
            print(f"Auto is running")
        else:
            print(f"Auto is not running")

    def show(self):
        if self.petrol:
            return f"Benzin {self.petrol // 10 * 100}kmga yetadi"
        else:
            return "notogri"


# s = Car("Cadilac",2024,False)
# print(s.moving())
d = BMW("Cadilac",2024,True,"Black",1700,24000,"M3",1)  # noqa
d.check()
print(d.show())
