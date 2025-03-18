class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0


    def calc(self):
        if kwh <= 2000:
            cost = 0.07
        if kwh > 2000 and kwh < 10000:
            cost = 
        ...
    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"
