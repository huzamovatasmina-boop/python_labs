from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Self

@dataclass
class Student:
    """
    Класс, представляющий студента.
    
    Attributes:
        fio: ФИО студента
        birthdate: Дата рождения в формате YYYY-MM-DD
        group: Номер группы (например, 'SE-01')
        gpa: Средний балл (от 0 до 5)
    """
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """
        Валидация данных после инициализации объекта.
        Вызывается автоматически после __init__.
        """
        # Валидация даты рождения
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
        
        # Валидация среднего балла
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        
        # Валидация ФИО (должно содержать пробелы)
        if len(self.fio.split()) < 2:
            raise ValueError(f"ФИО должно содержать минимум два слова: {self.fio}")
    
    def age(self) -> int:
        """
        Вычисляет возраст студента в полных годах.
        
        Returns:
            Возраст студента (количество полных лет)
        """
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем возраст
        age = today.year - birth_date.year
        
        # Учитываем, был ли уже день рождения в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        """
        Преобразует объект Student в словарь.
        
        Returns:
            Словарь с данными студента
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """
        Создает объект Student из словаря.
        
        Args:
            data: Словарь с данными студента
            
        Returns:
            Объект класса Student
        """
        return cls(
            fio=data.get("fio", ""),
            birthdate=data.get("birthdate", ""),
            group=data.get("group", ""),
            gpa=data.get("gpa", 0.0)
        )
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление студента.
        
        Returns:
            Форматированная строка с информацией о студенте
        """
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, возраст: {self.age()} лет"


# Дополнительный класс для работы со списком студентов
@dataclass
class StudentList:
    """Класс для работы со списком студентов."""
    
    students: list[Student]
    
    def add_student(self, student: Student):
        """Добавляет студента в список."""
        self.students.append(student)
    
    def get_by_group(self, group: str) -> list[Student]:
        """Возвращает список студентов указанной группы."""
        return [s for s in self.students if s.group == group]
    
    def get_top_students(self, n: int = 5) -> list[Student]:
        """Возвращает топ-N студентов по среднему баллу."""
        return sorted(self.students, key=lambda s: s.gpa, reverse=True)[:n]
    
    def average_gpa(self) -> float:
        """Вычисляет средний балл по всем студентам."""
        if not self.students:
            return 0.0
        return sum(s.gpa for s in self.students) / len(self.students)