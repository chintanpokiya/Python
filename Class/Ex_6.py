#Example 6

class Student:
    def __init__(self,name,age,student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def get_info(self):
        return f"Name: {self.name}, Age:{self.age},student id: {self.student_id}"

    def is_adult(self):
        return self.age >= 18

    def update_age(self,new_age):
        self.age = new_age
        print(f"Updated age to : {self.age}")

#example usage:
if __name__ == "__main__":
    student1 = Student("Alice",20,"S12345")
    print(student1.get_info())
    print("Is Adult :- ",student1.is_adult())

#update age
    student1.update_age(21)
    print(student1.get_info())
