from cl701g import *

def main():
    try:
        people: list[Person] = []
        with open("../Landat/prog701g.dat", 'r') as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readline()
                ln = f.readline()
                if num == 1:
                    gpa = float(f.readline())
                    p = Student(fn, ln, gpa)
                    people.append(p)
                elif num == 2:
                    num_stu = int(f.readline())
                    p = Teacher(fn, ln, num_stu)
                elif num == 3:
                    fav_word = f.readline().strip()
                    p = Admin(fn, ln, fav_word)
                    people.append(p)
                num = int(f.readline())

    except OSError as e:
        print("Error:" ,e)
    pass


if __name__ == "__main__":
    main()
