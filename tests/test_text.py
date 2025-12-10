import sys
import os

# Добавляем корневую папку в путь Python
sys.path.insert(0, os.path.abspath("."))

from src.lab03.text_stats import count_freq, top_n


def test_count_freq_basic():
    """Тест базовой функции подсчёта частот"""
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count_freq(tokens)

    assert result == {"apple": 3, "banana": 2, "cherry": 1}
    assert len(result) == 3
    assert result["apple"] == 3
    assert result["banana"] == 2
    assert result["cherry"] == 1


def test_count_freq_empty():
    """Тест пустого списка"""
    tokens = []
    result = count_freq(tokens)
    assert result == {}


def test_count_freq_single_word():
    """Тест одного слова"""
    tokens = ["hello"] * 5
    result = count_freq(tokens)
    assert result == {"hello": 5}


def test_top_n_basic():
    """Тест функции top_n"""
    freq = {"a": 5, "b": 3, "c": 10, "d": 1, "e": 7}
    result = top_n(freq, 3)

    assert result == [("c", 10), ("e", 7), ("a", 5)]
    assert len(result) == 3


def test_top_n_all():
    """Тест когда запрашиваем все элементы"""
    freq = {"a": 1, "b": 2, "c": 3}
    result = top_n(freq, 10)  # больше чем есть
    assert result == [("c", 3), ("b", 2), ("a", 1)]


def test_top_n_tie_breaker():
    """Тест при равенстве частот (сортировка по алфавиту)"""
    freq = {"z": 5, "a": 5, "m": 5, "b": 2}
    result = top_n(freq, 3)
    # При равенстве частот сортировка по алфавиту
    assert result == [("a", 5), ("m", 5), ("z", 5)]


def test_top_n_zero_n():
    """Тест когда n=0"""
    freq = {"a": 1, "b": 2}
    result = top_n(freq, 0)
    assert result == []


def test_top_n_default():
    """Тест с default значением n=5"""
    freq = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    result = top_n(freq)  # default n=5
    assert len(result) == 5
    assert result[0] == ("f", 6)
