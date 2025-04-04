import sys
sys.setrecursionlimit(5000)

def repeat(n):
    if n == 9672: return 0
    return n + repeat(n+3)

def main():
    num = 3
    if num == 3:
        test = repeat(num)
        print(f"3 + 6 + 9.. + 9663 = {test}")
    else:
        print("No")
        return 0





if __name__ == "__main__":
    main()
