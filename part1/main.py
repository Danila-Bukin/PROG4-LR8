import sqlite3

# Создаем соединение с нашей базой данных
conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получаем результат сделанного запроса
results = cursor.fetchall()
results2 =  cursor.fetchall()

print(results) # здесь данные
print(results2)  # здесь пусто

# Делаем INSERT запрос
cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")

# Сохранение транзакции
conn.commit()

# Проверяем результат
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results = cursor.fetchall()
print(results)

# Делаем множественную вставку строк
new_artists = [
    ('A Aagrh!',),
    ('A Aagrh!-2',),
    ('A Aagrh!-3',),
]
cursor.executemany("insert into Artist values (Null, ?);", new_artists)

# Получаем результаты по одному
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print("\nРезультаты по подному:")
print(cursor.fetchone())
print(cursor.fetchone())    
print(cursor.fetchone())    
print(cursor.fetchone()) 

# Использование курсора как итератора
print("\nИтератор:")
for row in cursor.execute('SELECT Name from Artist ORDER BY Name LIMIT 3'):
        print(row)

# Закрываем соединение с базой данных
conn.close()