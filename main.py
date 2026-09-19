import sqlite3 as sql
connection = sql.connect('university.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                                          id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                          name TEXT NOT NULL, 
                                                          age INTEGER, major TEXT)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                                                         course_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                         course_name TEXT NOT NULL, 
                                                         instructor TEXT)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses (
                  student_id INTEGER,
                  course_id INTEGER,
                  FOREIGN KEY (student_id) REFERENCES students (id),
                  FOREIGN KEY (course_id) REFERENCES courses (course_id))
               ''')

while True:
    print("1. Add a new student:")
    print("2. Add a new course:")
    print("3. Enroll a list of students:")
    print("4. Enroll a list of courses:")
    print("5. Register a student in a course:")
    print("6. View all students in a course:")
    print("7. Exit:")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")
        cursor.execute('''INSERT INTO students (name, age, major) VALUES (?,?,?)''', (name,age,major))

        connection.commit()
        print("Student added successfully")
    elif choice == "2":
        course_name = input("Enter course name: ")
        instructor = input("Enter instructor: ")
        cursor.execute('''INSERT INTO courses (course_name, instructor) VALUES (?,?)''', (course_name,instructor))

        connection.commit()
        print("Course added successfully")
    elif choice == "3":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("List of students:")
        for student in students:
            print(student)
    elif choice == "4":
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()

        print("List of courses:")
        for course in courses:
            print(course)
    elif choice == "5":
        course_id = input("Enter course id: ")
        new_name = input("Enter new student name: ")
        new_age = input("Enter new student age: ")
        new_major = input("Enter new student major: ")
        cursor.execute('''UPDATE students SET name = ?, age = ?, major = ? 
                          WHERE id = ?''', (new_name,new_age,new_major,course_id))
    elif choice == "6":
        course_id = input("Enter course id: ")
        cursor.execute('''SELECT students.id, students.name, students.age, students.major
        FROM students
        JOIN student_courses ON students.id = student_courses.student_id
        WHERE student_courses.course_id = ?''', (course_id,))

        enrolled_students = cursor.fetchall()
        print(f"Enrolled students in course {course_id}:")
        for student in enrolled_students:
            print(student)

    elif choice == "7":
        break
    else:
        print("Invalid choice")