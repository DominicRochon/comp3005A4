import psycopg2

def setup():
    #Create a connection object and curs0r
    connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password=postGresPassword)
    cur = connection.cursor()

    #Drop every table from database
    cur.execute(
    """
    SELECT tablename 
    FROM pg_tables 
    WHERE schemaname != 'pg_catalog' AND 
            schemaname != 'information_schema'
            """
    )
    tables = cur.fetchall()
    for table in tables:
        cur.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")

    # Create the students table and insert the initial data
    cur.execute(
    """
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    )"""
    )
    cur.execute(
    """
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    """
    )

    #Commit and close
    connection.commit()
    cur.close()
    connection.close()


def getAllStudents():
   connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password=postGresPassword)
   cur = connection.cursor()

   #Get all students
   cur.execute("SELECT * FROM students")
   students = cur.fetchall()

   cur.close()
   connection.close()

   return students

def addStudent(first_name, last_name, email, enrollment_date):
   connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password=postGresPassword)
   cur = connection.cursor()

   #Insert new student into table
   cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
               (first_name, last_name, email, enrollment_date))


   connection.commit()
   cur.close()
   connection.close()

def updateStudentEmail(student_id, new_email):
   connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password=postGresPassword)
   cur = connection.cursor()

   #Update emailAddress
   cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))

   connection.commit()
   cur.close()
   connection.close()

def deleteStudent(student_id):
   connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password=postGresPassword)
   cur = connection.cursor()

   #Delete the student
   cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

   connection.commit()
   cur.close()
   connection.close()


def main():
   global postGresPassword
   postGresPassword = input("Enter the password to your PostgreSQL server: ")

   #wipes tables and initializes students
   setup()
   
   while True:
        print("\n\nGet all students (1)\nAdd a student (2)\nUpdate student's email (3)\nDelete a student (4)\nQuit (q)")
        choice = input("Enter the number of the function you want to call: ")
        print("\n\n")


        if choice == "q":
                break

        if choice == "1":
            # Get all students
            students = getAllStudents()
            for student in students:
                print(student)

        elif choice == "2":
            # Add a student
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            # Update a student's email
            student_id = int(input("Enter the student's ID: "))
            new_email = input("Enter the new email: ")
            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            # Delete a student
            student_id = int(input("Enter the student's ID: "))
            deleteStudent(student_id)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
   main()
