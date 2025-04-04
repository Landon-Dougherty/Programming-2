class Solve():
    def __init__(self):
        self.all = []
        self.b500 = 0
        self.aoe500 = 0
        self.total = 0

        with open("Langdat/prog215a.dat", 'r') as f:
            for line in f:
                self.all.append(int(line))
                self.total += 1

    def calc(self):
        for x in self.all:
            if x in range(0, 500):
                self.b500 += 1
            if x in range(500, 10000000):
                self.aoe500 += 1


    def display(self):
        print(f"Number of #'s below 500 : {self.b500}")
        print(f"Number of #'s above 500 : {self.aoe500}")
        print(f"Number of #'s : {self.total}")
        pass


def main():
    c = Solve()
    c.calc()
    c.display()

if __name__ == "__main__":
    main()
