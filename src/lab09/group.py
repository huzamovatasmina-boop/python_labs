import csv
from pathlib import Path
from typing import List, Optional
from dataclasses import asdict

# Импортируем Student из ЛР8
try:
    from src.lab08.models import Student
except ImportError:
    # Для тестирования
    from dataclasses import dataclass
    from datetime import datetime, date
    
    @dataclass
    class Student:
        fio: str
        birthdate: str
        group: str
        gpa: float
        
        def age(self) -> int:
            birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
            today = date.today()
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            return age
        
        def to_dict(self) -> dict:
            return {
                "fio": self.fio,
                "birthdate": self.birthdate,
                "group": self.group,
                "gpa": self.gpa
            }
        
        @classmethod
        def from_dict(cls, data: dict):
            return cls(**data)


class Group:
    """
    Класс для работы с группой студентов, хранящейся в CSV-файле.
    Реализует CRUD-операции (Create, Read, Update, Delete).
    """
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы студентов.
        
        Args:
            storage_path: Путь к CSV-файлу для хранения данных
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """
        Создаёт файл с заголовками, если он не существует.
        """
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()
            print(f"📁 Создан новый файл базы данных: {self.path}")
    
    def _read_all(self) -> List[dict]:
        """
        Читает все записи из CSV-файла.
        
        Returns:
            Список словарей с данными студентов
        """
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows: List[dict]) -> None:
        """
        Записывает все записи в CSV-файл.
        
        Args:
            rows: Список словарей с данными студентов
        """
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        """
        Возвращает список всех студентов.
        
        Returns:
            Список объектов Student
        """
        rows = self._read_all()
        students = []
        
        for row in rows:
            try:
                # Преобразуем GPA из строки в float
                row['gpa'] = float(row['gpa'])
                student = Student.from_dict(row)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"⚠️ Ошибка при чтении студента {row.get('fio', 'unknown')}: {e}")
        
        return students
    
    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в базу данных.
        
        Args:
            student: Объект Student для добавления
        """
        # Читаем существующие данные
        rows = self._read_all()
        
        # Добавляем нового студента
        rows.append(student.to_dict())
        
        # Записываем обратно
        self._write_all(rows)
        
        print(f"✅ Студент {student.fio} успешно добавлен")
    
    def find(self, substr: str) -> List[Student]:
        """
        Ищет студентов по подстроке в ФИО.
        
        Args:
            substr: Подстрока для поиска в ФИО
            
        Returns:
            Список найденных студентов
        """
        all_students = self.list()
        substr_lower = substr.lower()
        
        found = [s for s in all_students if substr_lower in s.fio.lower()]
        
        if found:
            print(f"🔍 Найдено {len(found)} студентов по запросу '{substr}'")
        else:
            print(f"🔍 Студенты по запросу '{substr}' не найдены")
        
        return found
    
    def remove(self, fio: str) -> bool:
        """
        Удаляет студента по ФИО.
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если студент был удалён, False если не найден
        """
        rows = self._read_all()
        original_count = len(rows)
        
        # Удаляем всех студентов с указанным ФИО
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) < original_count:
            self._write_all(rows)
            print(f"🗑️ Студент {fio} удалён")
            return True
        else:
            print(f"⚠️ Студент {fio} не найден")
            return False
    
    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет данные студента.
        
        Args:
            fio: ФИО студента для обновления
            **fields: Поля для обновления (например, gpa=4.5, group="SE-01")
            
        Returns:
            True если студент был обновлён, False если не найден
        """
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                # Обновляем указанные поля
                for field, value in fields.items():
                    if field in row:
                        row[field] = value
                    else:
                        print(f"⚠️ Поле '{field}' не существует в записи студента")
                updated = True
                break
        
        if updated:
            self._write_all(rows)
            print(f"✏️ Данные студента {fio} обновлены")
        else:
            print(f"⚠️ Студент {fio} не найден")
        
        return updated
    
    def stats(self) -> dict:
        """
        Возвращает статистику по группе.
        
        Returns:
            Словарь со статистикой
        """
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        # Основная статистика
        gpa_values = [s.gpa for s in students]
        count = len(students)
        min_gpa = min(gpa_values)
        max_gpa = max(gpa_values)
        avg_gpa = sum(gpa_values) / count
        
        # Статистика по группам
        groups = {}
        for student in students:
            group = student.group
            if group not in groups:
                groups[group] = 0
            groups[group] += 1
        
        # Топ-5 студентов по GPA
        top_students = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in top_students]
        
        return {
            "count": count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": groups,
            "top_5_students": top_5
        }
    
    def print_table(self) -> None:
        """
        Выводит таблицу со списком студентов.
        """
        students = self.list()
        
        if not students:
            print("📭 База данных пуста")
            return
        
        print("\n" + "="*80)
        print(f"{'№':<3} {'ФИО':<30} {'Группа':<12} {'GPA':<6} {'Возраст':<8}")
        print("="*80)
        
        for i, student in enumerate(students, 1):
            print(f"{i:<3} {student.fio:<30} {student.group:<12} {student.gpa:<6.2f} {student.age():<8}")
        
        print("="*80)
        print(f"Всего студентов: {len(students)}")