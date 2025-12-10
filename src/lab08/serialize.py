import json
from pathlib import Path
from typing import List
from .models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.
    
    Args:
        students: Список объектов Student
        path: Путь для сохранения JSON файла
        
    Raises:
        ValueError: Если список пуст
        IOError: При ошибках записи файла
    """
    if not students:
        raise ValueError("Список студентов пуст")
    
    # Преобразуем студентов в словари
    data = [student.to_dict() for student in students]
    
    # Создаем директорию если её нет
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Записываем в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"✅ Данные сохранены в {path}")

def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON файла.
    
    Args:
        path: Путь к JSON файлу
        
    Returns:
        Список объектов Student
        
    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если JSON некорректен
    """
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка чтения JSON: {e}")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    
    # Создаем объекты Student из словарей
    students = []
    for i, item in enumerate(data, 1):
        try:
            student = Student.from_dict(item)
            students.append(student)
        except Exception as e:
            raise ValueError(f"Ошибка в записи {i}: {e}")
    
    print(f"✅ Загружено {len(students)} студентов из {path}")
    return students


# Дополнительные функции для работы с файлами
def export_students_csv(students: List[Student], path: str) -> None:
    """
    Экспортирует список студентов в CSV файл.
    
    Args:
        students: Список объектов Student
        path: Путь для сохранения CSV файла
    """
    import csv
    
    if not students:
        raise ValueError("Список студентов пуст")
    
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # Заголовок
        writer.writerow(['ФИО', 'Дата рождения', 'Группа', 'Средний балл', 'Возраст'])
        
        # Данные
        for student in students:
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                student.gpa,
                student.age()
            ])
    
    print(f"✅ Данные экспортированы в CSV: {path}")

def print_students_table(students: List[Student]) -> None:
    """
    Выводит таблицу со списком студентов.
    
    Args:
        students: Список объектов Student
    """
    if not students:
        print("📭 Список студентов пуст")
        return
    
    print("\n" + "="*80)
    print(f"{'№':<3} {'ФИО':<30} {'Группа':<10} {'GPA':<6} {'Возраст':<8}")
    print("="*80)
    
    for i, student in enumerate(students, 1):
        print(f"{i:<3} {student.fio:<30} {student.group:<10} {student.gpa:<6.2f} {student.age():<8}")
    
    print("="*80)
    print(f"Всего студентов: {len(students)}")
    print(f"Средний балл: {sum(s.gpa for s in students)/len(students):.2f}")