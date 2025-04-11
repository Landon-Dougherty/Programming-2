class Person():
    def __init__(self, fn, ln):
        self._first = fn
        self._last = ln

    def get_name(self):
        return self._first + " " + self._last

class Student(Person):
    def __init__(self, fn, ln, gpa):
        super().__init__(fn, ln) # or Person.__init__(fn,ln)
        self.gpa = gpa

class Teacher(Person):
    def __init__(self, fn, ln, num_stu):
        super().__init__(fn, ln) # or Person.__init__(fn,ln)
        self.num_stu = num_stu

class Admin(Person):
    def __init__(self, fn, ln, fav_word):
        super().__init__(fn, ln) # or Person.__init__(fn,ln)
        self.fav_word = fav_word

def main():
    try:
        people: list[Person] = []
        with open("Langdat/prog701g.dat", 'r') as f:
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
            tot = 0.0
            cnt = 0
            tot_stus = 0
            large = ""
            small = "0" * 10**5
            for person in people:
                if isinstance(person, Student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    tot_stus += person.num_stu
                elif isinstance(person,Admin):
                    fw = person.fav_word
                    if len(fw) > len(large):
                        large = fw
                    if len(fw) < len(small):
                        small = fw
            print("Average Student GPA :", round(tot/cnt,2))
            print("Total # of Students Taught : ", tot_stus)
            print("Smallest Favorite Admin Word : ", large)
            print("Largest Favorite Admin Word : ", small)

    except OSError as e:
        print("Error:" ,e)
    pass


if __name__ == "__main__":
    main()

