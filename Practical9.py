class Student:
    def __init__(self, rollNumber, name, div):
        self.rollNumber = rollNumber
        self.name = name
        self.div = div


class Exam(Student):
    def __init__(self, rollNumber, name, div):
        super().__init__(rollNumber, name, div)
        self.mark = []

    def marks(self):
        print(f"Enter marks for six subject of {self.name} : ")
        for i in range(6):
            temp = int(input())
            self.mark.append(temp)


class Result(Exam):
    def __init__(self, rollNumber, name, div):
        super().__init__(rollNumber, name, div)
        self.total_marks = 0

    def final_result(self):
        for i in range(6):
            self.total_marks += self.mark[i]

        print(f"result"
              f"\nName :\t\t\t{self.name}\nRoll No : \t\t{self.rollNumber}\nDivision : \t\t{self.div}\nTotal Marks : \t{self.total_marks}")


result = Result("20CE006","meet bharodiya","ce1")
result.marks()
result.final_result()
