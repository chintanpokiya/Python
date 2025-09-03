"""
    W.A.P. Menu Driven  Class| Database 
"""
import mysql.connector

class Student:
    def __init__(self,student_id,name,age,major):
        self.student_id = student_id
        self.name=name
        self.age=age
        self.major = major
    def __str__(self):
        return f"ID : {self.student_id},Name : {self.name} , Age : {self.age} ,Major: {self.major}"
        
        
class StudentDatabase:
    def __init__(self,host="localhost",user="root",password="",database="student_db"):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        #with self.conn:
        self.conn.execute("""
                CREATE TABLE IF NOT EXISTS students(
                    student_id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )
            """)
            
    def add_student(self,student:Student):
            sql = ("Insert INTO students (student_id,name,age,major) VALUES (%s,%s,%s,%s)"
            values = (student.student_id,student.name,student.age,student.major)
            self.cursor.execute(sql,values)
                   self.conn
            
    
    def view_students(self):
        with self.conn:
            cursor=self.conn.execute("Select * from students")
            for row in cursor:
                print(f"ID : {row[0]},Name : {row[1]}, Age : {row[2]} , Major : {row[3]}")
                
    def update_student(self,student_id,name,age,major):
        with self.conn:
            self.conn.execute("Update students SET name=? ,age=?,major=? where student_id=?",(name,age,major,student_id))

    def delete_student(self,student_id):
        with self.conn:
            self.conn.execute("DELETE FROM students where student_id = ?",(student_id,))
def main():
    db = StudentDatabase(user='root',password='',database='student_db')
    while(True):
        print("1.Add Student")
        print("2.View All Student")
        print("3.Update Student")
        print("4.Delete All Student")
        print("5.Search Student")
        print("6.Exit")
        choice=int(input("Enter Your Choice : "))
        if choice == 1:
            student_id = int(input("Enter Student ID : "))
            name=input("Enter Student Name : ")
            age=int(input("Enter Student Age : "))
            major=input("Enter Student Major : ")
            student=Student(student_id,name,age,major)
            db.add_student(student)
            print(f"Student {name} added successfully !!!")
            
        elif choice == 2:
            print("List of Students")
            db.view_students()
            
        elif choice == 3:
            student_id = int(input("Enter New Student ID : "))
            name=input("Enter New Student Name : ")
            age=int(input("Enter New Student Age : "))
            major=input("Enter New Student Major : ")            
            db.update_student(student_id,name,age,major)
            print(f"Student {name} updated successfully !!!")
        
        elif choice == 4:
            student_id = int(input("Enter STudent ID to Delete "))
            db.delete_student(student_id)
            print(f'Student {student_id} deleted Successfully')

        elif choice == 5:
            print("Search By :- ")
            print("a. Name ")
            print("b. Age ")
            print("c. Major")
            search_choice = input("Enter Your Choice (a/b/c) : ").lower()

            if search_choice == 'a':
                name = input("Enter Name To Search :- ")
                db.search_students('name',name)
            elif search_choice == 'b':
                age = input("Enter age to search :- ")
                db.search_students('age',age)
            elif search_choice == 'c':
                major = input("Enter Major to Search :- ")
                db.search_students('major',major)
            else:
                print("Invalid search option")
                
                
        elif choice == 6:
            print("Exiting Program..!!")
            db.close_connection()
            break
        else:
            print("You Have Entered Invalid Choice")
                      

if __name__ == '__main__':
    main()
