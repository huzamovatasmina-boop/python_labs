# test_lab08.py
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.lab08.models import Student, StudentList
from src.lab08.serialize import (
    students_to_json, 
    students_from_json,
    export_students_csv,
    print_students_table
)

def main():
    print("=== Тестирование класса Student ===")
    
    # Создаем студентов
    try:
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
        
        print("✅ Студенты созданы успешно")
        print(f"Студент 1: {student1}")
        print(f"Студент 2: {student2}")
        print(f"Возраст студента 1: {student1.age()} лет")
        print(f"Возраст студента 2: {student2.age()} лет")
        
        # Тестируем to_dict и from_dict
        print("\n=== Тестирование сериализации ===")
        student_dict = student1.to_dict()
        print(f"Словарь студента: {student_dict}")
        
        student_restored = Student.from_dict(student_dict)
        print(f"Восстановленный студент: {student_restored}")
        
        # Тестируем StudentList
        print("\n=== Тестирование StudentList ===")
        student_list = StudentList([student1, student2])
        print(f"Количество студентов: {len(student_list.students)}")
        print(f"Средний балл: {student_list.average_gpa():.2f}")
        
        # Тестируем сериализацию в JSON
        print("\n=== Тестирование JSON сериализации ===")
        students = [student1, student2]
        
        # Сохраняем в JSON
        students_to_json(students, "data/lab08/students_output.json")
        
        # Загружаем из JSON
        loaded_students = students_from_json("data/lab08/students_output.json")
        print(f"Загружено студентов: {len(loaded_students)}")
        
        # Выводим таблицу
        print_students_table(loaded_students)
        
        # Экспортируем в CSV
        export_students_csv(loaded_students, "data/lab08/students.csv")
        
        print("\n✅ Все тесты пройдены успешно!")
        
    except ValueError as e:
        print(f"❌ Ошибка валидации: {e}")
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()