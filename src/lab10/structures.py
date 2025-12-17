"""
Модуль содержит реализации базовых структур данных: Stack (стек) и Queue (очередь).
"""

from collections import deque
from typing import Any, Optional


class Stack:
    """
    Реализация стека (LIFO - Last In, First Out) на основе списка Python.
    
    Стек - это структура данных, в которой элементы добавляются и удаляются 
    с одного конца (вершины стека). Аналогия: стопка тарелок.
    
    Операции:
    - push(item): Добавить элемент на вершину стека - O(1)
    - pop(): Удалить и вернуть элемент с вершины - O(1)
    - peek(): Посмотреть элемент на вершине без удаления - O(1)
    - is_empty(): Проверить, пуст ли стек - O(1)
    """
    
    def __init__(self):
        """Инициализация пустого стека."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Добавляет элемент на вершину стека.
        
        Args:
            item: Элемент для добавления
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Удаляет и возвращает элемент с вершины стека.
        
        Returns:
            Элемент с вершины стека
            
        Raises:
            IndexError: Если стек пуст
        """
        if self.is_empty():
            raise IndexError("Нельзя удалить элемент из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """
        Возвращает элемент на вершине стека без удаления.
        
        Returns:
            Элемент на вершине стека или None, если стек пуст
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        
        Returns:
            True если стек пуст, иначе False
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        
        Returns:
            Количество элементов
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление стека.
        
        Returns:
            Строка вида "Stack([элементы])"
        """
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        """Возвращает представление стека для отладки."""
        return f"Stack({self._data})"
    
    def clear(self) -> None:
        """Очищает стек (удаляет все элементы)."""
        self._data.clear()


class Queue:
    """
    Реализация очереди (FIFO - First In, First Out) на основе deque.
    
    Очередь - это структура данных, в которой элементы добавляются в конец,
    а удаляются из начала. Аналогия: очередь в магазине.
    
    Используется collections.deque для эффективной реализации (O(1) для операций
    добавления/удаления с обоих концов).
    
    Операции:
    - enqueue(item): Добавить элемент в конец очереди - O(1)
    - dequeue(): Удалить и вернуть элемент из начала - O(1)
    - peek(): Посмотреть первый элемент без удаления - O(1)
    - is_empty(): Проверить, пуста ли очередь - O(1)
    """
    
    def __init__(self):
        """Инициализация пустой очереди."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Добавляет элемент в конец очереди.
        
        Args:
            item: Элемент для добавления
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Удаляет и возвращает элемент из начала очереди.
        
        Returns:
            Элемент из начала очереди
            
        Raises:
            IndexError: Если очередь пуста
        """
        if self.is_empty():
            raise IndexError("Нельзя удалить элемент из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """
        Возвращает первый элемент очереди без удаления.
        
        Returns:
            Первый элемент очереди или None, если очередь пуста
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        
        Returns:
            True если очередь пуста, иначе False
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        
        Returns:
            Количество элементов
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление очереди.
        
        Returns:
            Строка вида "Queue([элементы])"
        """
        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:
        """Возвращает представление очереди для отладки."""
        return f"Queue({list(self._data)})"
    
    def clear(self) -> None:
        """Очищает очередь (удаляет все элементы)."""
        self._data.clear()


def stack_example() -> None:
    """Пример использования стека."""
    print("=== Пример работы стека (LIFO) ===")
    stack = Stack()
    
    # Добавляем элементы
    stack.push("первый")
    stack.push("второй")
    stack.push("третий")
    
    print(f"Стек после добавлений: {stack}")
    print(f"Вершина стека (peek): {stack.peek()}")
    print(f"Размер стека: {len(stack)}")
    
    # Удаляем элементы (в обратном порядке)
    print("\nУдаляем элементы из стека:")
    while not stack.is_empty():
        print(f"  Извлечено: {stack.pop()}")
    
    print(f"Стек пуст: {stack.is_empty()}")


def queue_example() -> None:
    """Пример использования очереди."""
    print("\n=== Пример работы очереди (FIFO) ===")
    queue = Queue()
    
    # Добавляем элементы
    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")
    
    print(f"Очередь после добавлений: {queue}")
    print(f"Первый в очереди (peek): {queue.peek()}")
    print(f"Размер очереди: {len(queue)}")
    
    # Удаляем элементы (в порядке добавления)
    print("\nУдаляем элементы из очереди:")
    while not queue.is_empty():
        print(f"  Извлечено: {queue.dequeue()}")
    
    print(f"Очередь пуста: {queue.is_empty()}")


def reverse_string_with_stack(text: str) -> str:
    """
    Пример практического применения стека: переворот строки.
    
    Args:
        text: Исходная строка
        
    Returns:
        Перевернутая строка
    """
    stack = Stack()
    
    # Добавляем все символы в стек
    for char in text:
        stack.push(char)
    
    # Извлекаем символы (в обратном порядке)
    reversed_text = []
    while not stack.is_empty():
        reversed_text.append(stack.pop())
    
    return ''.join(reversed_text)


if __name__ == "__main__":
    # Демонстрация работы
    stack_example()
    queue_example()
    
    # Практический пример
    print("\n=== Практический пример: переворот строки с помощью стека ===")
    text = "Hello, World!"
    reversed_text = reverse_string_with_stack(text)
    print(f"Исходная строка: {text}")
    print(f"Перевернутая строка: {reversed_text}")