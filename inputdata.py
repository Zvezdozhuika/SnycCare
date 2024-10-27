import sqlite3
from datetime import datetime
connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    created_at TEXT NOT NULL
)
''')
def save_data_from_file(filename):
        while True:
                name = input("Введите имя (или 'exit' для выхода):").strip()
                if name.lower() == 'exit':
                    break
                age_input = input("Введите возраст: ").strip()
                try:
                    age = int(age_input)
                    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute('INSERT INTO users (name, age, created_at) VALUES (?, ?, ?)', (name, age, created_at))
                    print(f"Пользователь {name} с возрастом {age} добавлен.")
                except ValueError as e:
                    print(f"Ошибка при обработке строки: '{age_input}'. Проверьте формат данных. Ошибка: {e}")
                except Exception as e:
                    print(f"Неизвестная ошибка при обработке строки: '{name}'. Ошибка:{e}")
                    connect.commit()
save_data_from_file('C:/Users/Owner/Desktop/1.1.txt')
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)
connect.close()
