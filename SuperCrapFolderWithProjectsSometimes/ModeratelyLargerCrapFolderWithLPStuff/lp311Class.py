class Time:
    def __init__(self, des, cod, deb, test):
        self.des = des
        self.cod = cod
        self.deb = deb
        self.test = test

        self._total = int(des + cod + deb + test)
        self._percent = [0] * 4

        self.time = 0

    def getPercent(self, number):
        return round((number / self._total) * 100,2)

    def Calc(self):
        self._percent[0] = self.getPercent(self.des)
        self._percent[1] = self.getPercent(self.cod)
        self._percent[2] = self.getPercent(self.deb)
        self._percent[3] = self.getPercent(self.test)

    def Display(self):
        print("\nTime Spent Designing : " + str(self._percent[0]) + "%")
        print("Time Spent Coding : " + str(self._percent[1]) + "%")
        print("Time Spent Debugging : " + str(self._percent[2]) + "%")
        print("Time Spent Testing : " + str(self._percent[3]) + "%")




def main():
    des = int(input("Enter Time Designing : "))
    cod = int(input("Enter Time Coding : "))
    deb = int(input("Enter Time Debugging : "))
    test = int(input("Enter Time Testing : "))

    t = Time(des, cod, deb, test)
    t.Calc()
    t.Display()


if __name__ == "__main__":
    main()
