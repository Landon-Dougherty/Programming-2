class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0


    def calc(self):
        if self.kwh <= 2000:
            self.cost = 0.07
        if self.kwh > 2000 and self.kwh < 10000:
            self.cost = 0.05
        if self.kwh > 10000:
            self.cost = 0.4
        self.cost = self.cost * self.kwh
    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"
