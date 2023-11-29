class Omacka:
    # private
    __voda = 0
    __mouka = 0

    #property
    @property
    def voda(self):
        return self.__voda

    @voda.setter
    def voda(self, value):
        if value > 0:
            self.__voda = value

    @property
    def mouka(self):
        return self.__mouka

    @mouka.setter
    def mouka(self, value):
        if value > 0:
            self.__mouka = value

    def serviruj(self):
        return "Omáčka" if (self.__voda > self.__mouka) else "Fuj"

omacka = Omacka()
omacka.voda = -6
print(omacka.voda) # 0
