class Person():
    def __init__(self, job):
        self.job = job

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__('Student')
        self.name = name
        self.yob = yob
        self.grade = grade
    def describe(self):
        print(f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')
    
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__('Teacher')
        self.name = name
        self.yob = yob
        self.subject = subject
    def describe(self):
        print(f'Teacher - Name: {self.name} - YoB: {self.yob} - Grade: {self.subject}')
    
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__('Doctor')
        self.name = name
        self.yob = yob
        self.specialist = specialist
    def describe(self):
        print(f'Doctor - Name: {self.name} - YoB: {self.yob} - Grade: {self.specialist}')
    
class Ward():
    def __init__(self, name) -> None:
        self.name = name
        self.lst_ward = []
    def add_person(self, person):
        self.lst_ward.append(person)
    def count_doctor(self):
        count = 0
        for person in self.lst_ward:
            if person.job == "Doctor":
                count += 1
        return count
    def sort_age(self):
        self.lst_ward =  sorted(self.lst_ward, key= lambda person: person.yob, reverse=True)
    def compute_average(self):
        result = 0 
        count = 0
        for person in self.lst_ward:
            if person.job == "Teacher":
                result += person.yob
                count += 1
        return int(result/count)
    def describe(self):
        print(f'Ward Name: {self.name}')
        for person in self.lst_ward:
            person.describe()
    

if __name__ == "__main__":
    split_line = "######################################################################"
    student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
    teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
    doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
    teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
    doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
    print(split_line)
    student1 . describe ()
    teacher1 . describe ()
    doctor1 . describe ()
    print(split_line)
    ward1 = Ward ( name =" Ward1 ")
    ward1 . add_person ( student1 )
    ward1 . add_person ( teacher1 )
    ward1 . add_person ( teacher2 )
    ward1 . add_person ( doctor1 )
    ward1 . add_person ( doctor2 )
    ward1 . describe ()
    print(split_line)
    print ( f"Number of doctors : { ward1 . count_doctor ()}")
    print(split_line)
    print ("After sorting Age of Ward1 people ")
    ward1 . sort_age ()
    ward1 . describe ()
    print(split_line)
    print ( f"Average year of birth ( teachers ): { ward1 . compute_average ()}")