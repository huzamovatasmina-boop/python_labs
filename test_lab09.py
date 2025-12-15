# test_lab09.py
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Импортируем Student из ЛР8
from src.lab08.models import Student
from src.lab09.group import Group

def main():
    print("=== Тестирование класса Group (CRUD операции) ===")
    
    # Путь к файлу базы данных
    db_path = "data/lab09/students.csv"
    
    # Создаем объект Group
    group = Group(db_path)
    
    # 1. Проверяем список (должен быть пустым или с данными)
    print("\n1. Текущий список студентов:")
    students = group.list()
    print(f"   В базе: {len(students)} студентов")
    
    # 2. Добавляем студентов
    print("\n2. Добавляем студентов:")
    
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.5
    )
    
    student2 = Student(
        fio="Петрова Анна Сергеевна",
        birthdate="2001-02-20",
        group="SE-02",
        gpa=4.8
    )
    
    student3 = Student(
        fio="Сидоров Алексей Петрович",
        birthdate="1999-11-30",
        group="SE-01",
        gpa=3.9
    )
    
    group.add(student1)
    group.add(student2)
    group.add(student3)
    
    # 3. Выводим таблицу
    print("\n3. Таблица всех студентов:")
    group.print_table()
    
    # 4. Поиск студентов
    print("\n4. Поиск студентов по ФИО:")
    
    # Поиск по подстроке
    found = group.find("Иванов")
    print(f"   Найдено по 'Иванов': {len(found)} студентов")
    
    found = group.find("Петр")
    print(f"   Найдено по 'Петр': {len(found)} студентов")
    
    # 5. Обновление данных
    print("\n5. Обновление данных студента:")
    
    # Обновляем GPA у Иванова
    group.update("Иванов Иван Иванович", gpa=4.7)
    
    # Обновляем группу у Петровой
    group.update("Петрова Анна Сергеевна", group="SE-03")
    
    # 6. Удаление студента
    print("\n6. Удаление студента:")
    group.remove("Сидоров Алексей Петрович")
    
    # 7. Выводим обновленную таблицу
    print("\n7. Обновленная таблица студентов:")
    group.print_table()
    
    # 8. Статистика
    print("\n8. Статистика группы:")
    stats = group.stats()
    
    print(f"   Всего студентов: {stats['count']}")
    print(f"   Минимальный GPA: {stats['min_gpa']:.2f}")
    print(f"   Максимальный GPA: {stats['max_gpa']:.2f}")
    print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
    
    print(f"   Распределение по группам:")
    for grp, count in stats['groups'].items():
        print(f"     - {grp}: {count} студентов")
    
    print(f"   Топ-5 студентов:")
    for i, student in enumerate(stats['top_5_students'], 1):
        print(f"     {i}. {student['fio']} (GPA: {student['gpa']:.2f})")
    
    # 9. Тестирование с твоими данными (если есть)
    print("\n" + "="*60)
    print("Тестирование с реальными данными из ЛР8:")
    
    try:
        # Загружаем студентов из ЛР8
        from src.lab08.serialize import students_from_json
        real_students = students_from_json("data/lab08/students_input.json")
        
        # Создаем новую базу для теста
        test_db = Group("data/lab09/test_students.csv")
        
        # Добавляем реальных студентов
        for student in real_students:
            test_db.add(student)
        
        print(f"   Добавлено {len(real_students)} студентов")
        
        # Выводим статистику
        real_stats = test_db.stats()
        print(f"   Средний GPA реальных студентов: {real_stats['avg_gpa']:.2f}")
        
    except Exception as e:
        print(f"   ⚠️ Не удалось загрузить реальные данные: {e}")
    
    print("\n✅ Все операции CRUD протестированы успешно!")

if __name__ == "__main__":
    main()