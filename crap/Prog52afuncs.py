import voidfunction

def calcArea(len, wid) -> int:
    return len*wid


def calcPerim(len:int, wid:int):
    return len*2 + wid * 2

def areaPerim(len, wid):
    area = calcArea(len, wid)
    perim = calcPerim(len, wid)
    return area, perim

def main():
    voidfunction.doThing() # Runs do thing from voidfunction
    length = int(input("Enter Length : "))
    width = int(input("Enter Width : "))
    a, p = areaPerim(length, width)
    print(f"Area : {a}\nPerimeter : {p}")
    pass


if __name__ == "__main__":
    main()

