
class Cost():
    def __init__(self):
        self.total = 0
        self.ages = []
        self.b20 = 0
        self.b40 = 0
        self.b60 = 0
        self.b80 = 0
        self.a80 = 0



        with open("../Langdat/prog213e.dat", 'r') as f:
            for line in f:
                self.ages.append(int(line))

    def Display(self):
        print("This Code Sucked")
        print(f"<20 \t {self.b20} \t Percent : {(self.b20/self.total)*100:.2f}")
        print(f"20-39 \t {self.b40} \t Percent : {(self.b40/self.total)*100:.2f}")
        print(f"40-59 \t {self.b60} \t Percent : {(self.b60/self.total)*100:.2f}")
        print(f"60-79 \t {self.b80} \t Percent : {(self.b80/self.total)*100:.2f}")
        print(f">80 \t {self.a80} \t Percent : {(self.a80/self.total)*100:.2f}")
    def Calc(self):
        for x in self.ages:
            if x in range(1,20):
                self.b20 += 1
            if x in range(20,40):
                self.b40 += 1
            if x in range(40,60):
                self.b60 += 1
            if x in range(60,80):
                self.b80 += 1
            if x >= 79:
                self.a80 += 1

        self.total = self.b20 + self.b40 + self.b60 + self.b80 + self.a80





def main():
    c = Cost()
    c.Calc()
    c.Display()


if __name__ == '__main__':
    main()


