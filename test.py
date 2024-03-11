import mysql.connector

# Встановлюємо з'єднання з базою даних
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='university'
)

# Створюємо курсор
cursor = connection.cursor()

# Виконуємо SQL-запит з файлу
with open('query_10.sql', 'r') as file:
    sql_query = file.read()
    cursor.execute(sql_query)

# Отримуємо результати
results = cursor.fetchall()

# Виводимо результати
for row in results:
    print(row)

# Закриваємо курсор і з'єднання
cursor.close()
connection.close()
