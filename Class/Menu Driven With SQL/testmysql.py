import mysql.connector

# Student Class to define the attributes of the student
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age},Major: {self.major}"

# Database Class to handle MySQL operations
class StudentDatabase:
    def __init__(self, host="localhost", user="root", password="",database="student_db"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                major VARCHAR(100)
            )
        """)

    def add_student(self, student: Student):
        sql = "INSERT INTO students (student_id, name, age, major)VALUES (%s, %s, %s, %s)"
        values = (student.student_id, student.name, student.age,
                  student.major)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        result = self.cursor.fetchall()
        for row in result:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Major:{row[3]}")

    def update_student(self, student_id, name, age, major):
        sql = "UPDATE students SET name=%s, age=%s, major=%s WHERE student_id=%s"
        values = (name, age, major, student_id)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_student(self, student_id):
        sql = "DELETE FROM students WHERE student_id=%s"
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()

    # Search Functionality
    def search_students(self, column, value):
        sql = f"SELECT * FROM students WHERE {column} LIKE %s"
        self.cursor.execute(sql, ('%' + value + '%',))
        result = self.cursor.fetchall()
        if result:
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]},Major: {row[3]}")
        else:
            print(f"No student found with {column} matching '{value}'.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Menu-Driven Interface
def menu():
    db = StudentDatabase(user='root', password='', database='student_db')
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Students")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            major = input("Enter Student Major: ")
            student = Student(student_id, name, age, major)
            db.add_student(student)
            print(f"Student {name} added successfully.")

        elif choice == '2':
            print("List of Students:")
            db.view_students()

        elif choice == '3':
            student_id = int(input("Enter Student ID to Update: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            major = input("Enter New Major: ")
            db.update_student(student_id, name, age, major)
            print(f"Student {student_id} updated successfully.")

        elif choice == '4':
            student_id = int(input("Enter Student ID to Delete: "))
            db.delete_student(student_id)
            print(f"Student {student_id} deleted successfully.")

        elif choice == '5':
            print("Search by:")
            print("a. Name")
            print("b. Age")
            print("c. Major")
            search_choice = input("Enter your choice (a/b/c): ").lower()

            if search_choice == 'a':
                name = input("Enter name to search: ")
                db.search_students('name', name)
            elif search_choice == 'b':
                age = input("Enter age to search: ")
                db.search_students('age', age)
            elif search_choice == 'c':
                major = input("Enter major to search: ")
                db.search_students('major', major)
            else:
                print("Invalid search option.")

        elif choice == '6':
            print("Exiting program.")
            db.close_connection()
            break

        else:
            print("Invalid choice! Please try again.")

# Run the menu
if __name__ == '__main__':
    menu()
