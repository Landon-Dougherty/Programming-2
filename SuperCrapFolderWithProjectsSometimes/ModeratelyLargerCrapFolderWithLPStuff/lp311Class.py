class TimePercent:
    def __init__(self, des, cod, deb, test, time):
        self.des = des
        self.cod = cod
        self.deb = deb
        self.test = test

        self._total = int(des+cod+deb+test)
        self._percent = [0] * 4

        self.time = 0

    def getPercent(self, number):
        return round((number / self.total) * 100,2)

    def Calc(self):
        self._percent[0] = self.getPercent(self.des)
        self._percent[1] = self.getPercent(self.cod)
        self._percent[2] = self.getPercent(self.deb)
        self._percent[3] = self.getPercent(self.test)

def main():
    des = int(input("Enter Time Designing : "))
    cod = int(input("Enter Time Coding : "))


if __name__ == "__main__":
    main()




