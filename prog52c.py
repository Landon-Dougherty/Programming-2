class Circle:
    def __init__(self, rad):
        self.rad = rad

        self._area = 0
        self._circ = 0



    def getArea(self):
        self._area = round((self.rad * 3.14159265)**2,2)

    def GetCirc(self):
        self._circ = round(2*(3.1519265 * self.rad),2)

    def Display(self):
        print("Radius : " + str(self.rad) + " Units")
        print("Circumference : " + str(self._circ) + " Units")
        print("Area : " + str(self._area) + " Units Squared" )
def main():
    rad = int(input("Enter Radius : "))

    c = Circle(rad)
    c.getArea()
    c.GetCirc()
    c.Display()


    pass


if __name__ == "__main__":
    main()




