class Cost():
    def __init__(self, dia):
        self.dia = dia

        self.total = 0.0

    def mat(self):
        self.total += float((0.05*self.dia*self.dia)) + 1.75

    def dis(self):
        print("Your Pizza Cost Is ... $" + str(self.total))
def main():
    dia = int(input("Enter Diameter Of Pizza : "))

    c = Cost(dia)
    c.mat()
    c.dis()


    pass


if __name__ == "__main__":
    main()
