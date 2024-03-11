from faker import Faker
import random
import mysql.connector

# Встановлюємо з'єднання з базою даних
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='university'
)

fake = Faker()
cursor = connection.cursor()

cursor.execute("DELETE FROM student_marks")
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM groupsst")
cursor.execute("DELETE FROM teachers")
cursor.execute("DELETE FROM subjects")

# Генеруємо випадкові дані для студентів, груп, викладачів та предметів
students = [(fake.name(), random.randint(1, 3)) for _ in range(random.randint(30, 50))]
groupsst = [(f'Group {i}',) for i in range(1, 4)]
teachers = [(fake.name(),) for _ in range(random.randint(3, 5))]
subjects = [(fake.word(), random.randint(1, len(teachers))) for _ in range(random.randint(5, 8))]

# Створюємо таблиці та заповнюємо їх даними
cursor.executemany("INSERT INTO students (student_name, stgroup_id) VALUES (%s, %s)", students)
cursor.executemany("INSERT INTO groupsst (group_name) VALUES (%s)", groupsst)
cursor.executemany("INSERT INTO teachers (teacher_name) VALUES (%s)", teachers)
cursor.executemany("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)", subjects)

# Витягуємо ідентифікатори предметів з бази даних
cursor.execute("SELECT subject_id FROM subjects")
subject_ids = cursor.fetchall()

# Генеруємо випадкові оцінки для студентів по предметах
for student in students:
    cursor.execute("SELECT student_id FROM students WHERE student_name = %s", (student[0],))
    student_id = cursor.fetchone()[0]
    for subject_id in subject_ids:
        marks = [(student_id, subject_id[0], random.uniform(60, 100), fake.date_between(start_date='-1y', end_date='today')) 
                 for _ in range(random.randint(5, 20))]
        cursor.executemany("INSERT INTO student_marks (student_id, subject_id, mark, mark_date) VALUES (%s, %s, %s, %s)", marks)

# Зберігаємо зміни та закриваємо з'єднання
connection.commit()
connection.close()
print("База даних успішно заповнена випадковими даними.")
