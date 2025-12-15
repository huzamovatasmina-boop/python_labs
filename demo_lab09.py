# demo_lab09.py
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.lab08.models import Student
from src.lab09.group import Group

def main():
    print("=== Демонстрация работы класса Group (CRUD на CSV) ===")
    
    # Используем новый файл для демонстрации
    db_path = "data/lab09/demo_students.csv"
    
    # Удаляем старый файл если есть (чтобы начать с чистого листа)
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Создаём объект Group
    group = Group(db_path)
    
    print("1. Создаём новую пустую базу данных")
    print(f"   Файл: {db_path}")
    print(f"   Студентов в базе: {len(group.list())}")
    
    print("\n2. Добавляем студентов:")
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна Сергеевна", "2001-02-20", "SE-02", 4.8),
        Student("Сидоров Алексей Петрович", "1999-11-30", "SE-01", 3.9),
        Student("Козлова Мария Дмитриевна", "2002-07-10", "SE-03", 4.2),
        Student("Николаев Денис Олегович", "2000-12-05", "SE-02", 3.5)
    ]
    
    for student in students:
        group.add(student)
        print(f"   ✅ Добавлен: {student.fio}")
    
    print("\n3. Выводим список всех студентов:")
    group.print_table()
    
    print("\n4. Поиск студентов:")
    search_queries = ["Иван", "Петр", "ов"]
    for query in search_queries:
        found = group.find(query)
        print(f"   По запросу '{query}': найдено {len(found)} студентов")
    
    print("\n5. Обновление данных:")
    print("   - Меняем GPA у Иванова с 4.5 на 4.7")
    print("   - Меняем группу у Петровой с SE-02 на SE-03")
    group.update("Иванов Иван Иванович", gpa=4.7)
    group.update("Петрова Анна Сергеевна", group="SE-03")
    
    print("\n6. Удаление студента:")
    print("   - Удаляем Сидорова Алексея Петровича")
    group.remove("Сидоров Алексей Петрович")
    
    print("\n7. Финальный список студентов:")
    group.print_table()
    
    print("\n8. Статистика (доп. задание со звёздочкой):")
    stats = group.stats()
    print(f"   Всего студентов: {stats['count']}")
    print(f"   Минимальный GPA: {stats['min_gpa']:.2f}")
    print(f"   Максимальный GPA: {stats['max_gpa']:.2f}")
    print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"   Распределение по группам:")
    for group_name, count in stats['groups'].items():
        print(f"     - {group_name}: {count} студентов")
    print(f"   Топ-3 студентов:")
    for i, student in enumerate(stats['top_5_students'][:3], 1):
        print(f"     {i}. {student['fio']} (GPA: {student['gpa']:.2f})")
    
    print("\n9. Проверяем содержимое CSV файла:")
    with open(db_path, 'r', encoding='utf-8') as f:
        print(f.read())
    
    print("\n✅ Демонстрация завершена успешно!")

if __name__ == "__main__":
    main()