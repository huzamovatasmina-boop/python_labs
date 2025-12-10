import pytest
import json
import csv
import sys
import os

# Добавляем корневую папку в путь Python
sys.path.insert(0, os.path.abspath('.'))

from src.lab05.json_csv import json_to_csv, csv_to_json

def test_json_to_csv_basic(tmp_path):
    """Тест базовой конвертации JSON → CSV"""
    # Создаём тестовый JSON файл
    json_path = tmp_path / "test.json"
    csv_path = tmp_path / "test.csv"
    
    test_data = [
        {"name": "Анна", "age": 25, "city": "Москва"},
        {"name": "Петр", "age": 30, "city": "СПб"},
        {"name": "Мария", "age": 28, "city": "Казань"}
    ]
    
    # Записываем JSON
    json_path.write_text(json.dumps(test_data, ensure_ascii=False, indent=2), 
                         encoding='utf-8')
    
    # Конвертируем
    json_to_csv(str(json_path), str(csv_path))
    
    # Проверяем результат
    assert csv_path.exists()
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    assert len(rows) == 3
    assert set(rows[0].keys()) == {"name", "age", "city"}
    assert rows[0]["name"] == "Анна"
    assert rows[0]["age"] == "25"
    assert rows[0]["city"] == "Москва"

def test_csv_to_json_basic(tmp_path):
    """Тест базовой конвертации CSV → JSON"""
    # Создаём тестовый CSV файл
    csv_path = tmp_path / "test.csv"
    json_path = tmp_path / "test.json"
    
    csv_content = """name,age,city
Анна,25,Москва
Петр,30,СПб
Мария,28,Казань"""
    
    csv_path.write_text(csv_content, encoding='utf-8')
    
    # Конвертируем
    csv_to_json(str(csv_path), str(json_path))
    
    # Проверяем результат
    assert json_path.exists()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert len(data) == 3
    assert data[0] == {"name": "Анна", "age": "25", "city": "Москва"}
    assert data[1] == {"name": "Петр", "age": "30", "city": "СПб"}

def test_json_to_csv_empty_list(tmp_path):
    """Тест пустого JSON списка"""
    json_path = tmp_path / "empty.json"
    csv_path = tmp_path / "empty.csv"
    
    json_path.write_text('[]', encoding='utf-8')
    
    # Должна быть ошибка
    with pytest.raises(ValueError, match=".*Пустой.*|.*empty.*"):
        json_to_csv(str(json_path), str(csv_path))

def test_json_to_csv_invalid_json(tmp_path):
    """Тест некорректного JSON"""
    json_path = tmp_path / "invalid.json"
    csv_path = tmp_path / "test.csv"
    
    json_path.write_text('{not valid json}', encoding='utf-8')
    
    with pytest.raises(ValueError, match=".*JSON.*"):
        json_to_csv(str(json_path), str(csv_path))

def test_csv_to_json_missing_file():
    """Тест отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("несуществующий_файл.csv", "output.json")

def test_json_to_csv_missing_file():
    """Тест отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("несуществующий_файл.json", "output.csv")

def test_json_to_csv_roundtrip(tmp_path):
    """Тест полного цикла JSON → CSV → JSON"""
    # Исходные данные
    original_data = [
        {"name": "Test", "value": 123},
        {"name": "Another", "value": 456}
    ]
    
    # JSON → CSV
    json_path = tmp_path / "original.json"
    csv_path = tmp_path / "converted.csv"
    json_path2 = tmp_path / "back.json"
    
    json_path.write_text(json.dumps(original_data), encoding='utf-8')
    json_to_csv(str(json_path), str(csv_path))
    
    # CSV → JSON
    csv_to_json(str(csv_path), str(json_path2))
    
    # Проверяем что данные совпадают
    with open(json_path2, 'r', encoding='utf-8') as f:
        restored_data = json.load(f)
    
    # В CSV все значения строковые, поэтому сравниваем соответствующим образом
    assert len(restored_data) == len(original_data)
    assert restored_data[0]["name"] == original_data[0]["name"]
    assert restored_data[0]["value"] == str(original_data[0]["value"])  # CSV хранит строки