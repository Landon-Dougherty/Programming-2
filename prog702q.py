class Vehicle():
    def __init__(self, name, tire):
        self.name = name
        self.tire = tire

class Car(Vehicle):
    def __init__(self, name, tire, worth):
        super().__init__(name, tire)
        self.worth = worth


class Truck(Vehicle):
    def __init__(self, name, tire, mile):
        super().__init__(name, tire)
        self.mile = mile


class Bus(Vehicle):
    def __init__(self, name, tire, home):
        super().__init__(name, tire)  # Can also be Vehicle.__init__(name,tire)
        self.home = home

def main():
    try:
        with open("Langdat/prog701g.txt",'r') as f:
            pass
    pass

if __name__ == "__main__":
    main()
