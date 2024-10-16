class Card:
    def __init__(self,fullname, gender, year, address, idcard):
        self.fullname = fullname
        self.gender = gender
        self.year = year
        self.address = address
        self.__idcard = idcard

    def __idcard(self):
        return self.__idcard


s = Card("Xasan", "Male", 2008, "Samarkand", "SS77777")
print(s.__idcard())