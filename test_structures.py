# test_structures.py
import sys
import os
import time
import random
sys.path.insert(0, os.path.abspath('.'))

from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def benchmark_stack(n: int = 10000) -> None:
    """Тестирование производительности стека."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк стека для {n} операций")
    print('='*60)
    
    stack = Stack()
    
    # Тест push
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    push_time = time.perf_counter() - start
    print(f"Push {n} элементов: {push_time:.6f} сек")
    
    # Тест pop
    start = time.perf_counter()
    for _ in range(n):
        stack.pop()
    pop_time = time.perf_counter() - start
    print(f"Pop {n} элементов: {pop_time:.6f} сек")
    
    print(f"Среднее время на операцию: {(push_time + pop_time) / (2*n):.8f} сек")


def benchmark_queue(n: int = 10000) -> None:
    """Тестирование производительности очереди."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк очереди для {n} операций")
    print('='*60)
    
    queue = Queue()
    
    # Тест enqueue
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.perf_counter() - start
    print(f"Enqueue {n} элементов: {enqueue_time:.6f} сек")
    
    # Тест dequeue
    start = time.perf_counter()
    for _ in range(n):
        queue.dequeue()
    dequeue_time = time.perf_counter() - start
    print(f"Dequeue {n} элементов: {dequeue_time:.6f} сек")
    
    print(f"Среднее время на операцию: {(enqueue_time + dequeue_time) / (2*n):.8f} сек")


def benchmark_linked_list(n: int = 1000) -> None:
    """Тестирование производительности связного списка."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк связного списка для {n} операций")
    print('='*60)
    
    lst = SinglyLinkedList()
    
    # Тест append
    start = time.perf_counter()
    for i in range(n):
        lst.append(i)
    append_time = time.perf_counter() - start
    print(f"Append {n} элементов: {append_time:.6f} сек")
    
    # Тест prepend
    lst.clear()
    start = time.perf_counter()
    for i in range(n):
        lst.prepend(i)
    prepend_time = time.perf_counter() - start
    print(f"Prepend {n} элементов: {prepend_time:.6f} сек")
    
    # Тест get (доступ по индексу)
    start = time.perf_counter()
    for i in range(min(n, 100)):  # Меньше итераций, т.к. O(n)
        lst.get(i)
    get_time = time.perf_counter() - start
    print(f"Get 100 элементов (по индексу): {get_time:.6f} сек")
    
    print(f"\nПримечание: операции с индексами в связном списке O(n), "
          f"поэтому медленнее чем в массиве O(1)")


def compare_append_performance() -> None:
    """Сравнение производительности добавления элементов."""
    print(f"\n{'='*60}")
    print("Сравнение производительности добавления элементов")
    print('='*60)
    
    sizes = [100, 1000, 5000, 10000]
    
    for size in sizes:
        print(f"\nРазмер: {size} элементов")
        
        # Python list (аналог стека)
        start = time.perf_counter()
        py_list = []
        for i in range(size):
            py_list.append(i)
        py_time = time.perf_counter() - start
        
        # Наш Stack
        start = time.perf_counter()
        stack = Stack()
        for i in range(size):
            stack.push(i)
        stack_time = time.perf_counter() - start
        
        # Наш Queue
        start = time.perf_counter()
        queue = Queue()
        for i in range(size):
            queue.enqueue(i)
        queue_time = time.perf_counter() - start
        
        # Наш LinkedList
        start = time.perf_counter()
        lst = SinglyLinkedList()
        for i in range(size):
            lst.append(i)
        lst_time = time.perf_counter() - start
        
        print(f"  Python list: {py_time:.6f} сек")
        print(f"  Наш Stack:    {stack_time:.6f} сек")
        print(f"  Наш Queue:    {queue_time:.6f} сек")
        print(f"  Наш LinkedList: {lst_time:.6f} сек")


def practical_example() -> None:
    """Практический пример использования структур данных."""
    print(f"\n{'='*60}")
    print("Практический пример: проверка сбалансированности скобок")
    print('='*60)
    
    def is_balanced(expression: str) -> bool:
        """Проверяет, сбалансированы ли скобки в выражении."""
        stack = Stack()
        brackets = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in brackets.keys():  # Открывающая скобка
                stack.push(char)
            elif char in brackets.values():  # Закрывающая скобка
                if stack.is_empty():
                    return False
                opening = stack.pop()
                if brackets[opening] != char:
                    return False
        
        return stack.is_empty()
    
    test_cases = [
        ("(2 + 3) * [4 - 1]", True),
        ("{([<>])}", True),
        ("((())", False),
        ("([)]", False),
        ("", True)
    ]
    
    for expr, expected in test_cases:
        result = is_balanced(expr)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expr}' -> {result} (ожидалось: {expected})")


def main():
    print("=== Тестирование структур данных и бенчмарки ===")
    
    # Базовые тесты
    print("\n1. Базовые тесты работы структур:")
    
    # Стек
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"После pop: {stack}")
    
    # Очередь
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"\nОчередь: {queue}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"После dequeue: {queue}")
    
    # Связный список
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.prepend(5)
    print(f"\nСвязный список: {lst}")
    print(f"Элемент по индексу 1: {lst.get(1)}")
    
    # Бенчмарки
    benchmark_stack(10000)
    benchmark_queue(10000)
    benchmark_linked_list(1000)
    compare_append_performance()
    practical_example()
    
    print(f"\n{'='*60}")
    print("✅ Все тесты завершены успешно!")
    print('='*60)


if __name__ == "__main__":
    main()# test_structures.py
import sys
import os
import time
import random
sys.path.insert(0, os.path.abspath('.'))

from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def benchmark_stack(n: int = 10000) -> None:
    """Тестирование производительности стека."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк стека для {n} операций")
    print('='*60)
    
    stack = Stack()
    
    # Тест push
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    push_time = time.perf_counter() - start
    print(f"Push {n} элементов: {push_time:.6f} сек")
    
    # Тест pop
    start = time.perf_counter()
    for _ in range(n):
        stack.pop()
    pop_time = time.perf_counter() - start
    print(f"Pop {n} элементов: {pop_time:.6f} сек")
    
    print(f"Среднее время на операцию: {(push_time + pop_time) / (2*n):.8f} сек")


def benchmark_queue(n: int = 10000) -> None:
    """Тестирование производительности очереди."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк очереди для {n} операций")
    print('='*60)
    
    queue = Queue()
    
    # Тест enqueue
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.perf_counter() - start
    print(f"Enqueue {n} элементов: {enqueue_time:.6f} сек")
    
    # Тест dequeue
    start = time.perf_counter()
    for _ in range(n):
        queue.dequeue()
    dequeue_time = time.perf_counter() - start
    print(f"Dequeue {n} элементов: {dequeue_time:.6f} сек")
    
    print(f"Среднее время на операцию: {(enqueue_time + dequeue_time) / (2*n):.8f} сек")


def benchmark_linked_list(n: int = 1000) -> None:
    """Тестирование производительности связного списка."""
    print(f"\n{'='*60}")
    print(f"Бенчмарк связного списка для {n} операций")
    print('='*60)
    
    lst = SinglyLinkedList()
    
    # Тест append
    start = time.perf_counter()
    for i in range(n):
        lst.append(i)
    append_time = time.perf_counter() - start
    print(f"Append {n} элементов: {append_time:.6f} сек")
    
    # Тест prepend
    lst.clear()
    start = time.perf_counter()
    for i in range(n):
        lst.prepend(i)
    prepend_time = time.perf_counter() - start
    print(f"Prepend {n} элементов: {prepend_time:.6f} сек")
    
    # Тест get (доступ по индексу)
    start = time.perf_counter()
    for i in range(min(n, 100)):  # Меньше итераций, т.к. O(n)
        lst.get(i)
    get_time = time.perf_counter() - start
    print(f"Get 100 элементов (по индексу): {get_time:.6f} сек")
    
    print(f"\nПримечание: операции с индексами в связном списке O(n), "
          f"поэтому медленнее чем в массиве O(1)")


def compare_append_performance() -> None:
    """Сравнение производительности добавления элементов."""
    print(f"\n{'='*60}")
    print("Сравнение производительности добавления элементов")
    print('='*60)
    
    sizes = [100, 1000, 5000, 10000]
    
    for size in sizes:
        print(f"\nРазмер: {size} элементов")
        
        # Python list (аналог стека)
        start = time.perf_counter()
        py_list = []
        for i in range(size):
            py_list.append(i)
        py_time = time.perf_counter() - start
        
        # Наш Stack
        start = time.perf_counter()
        stack = Stack()
        for i in range(size):
            stack.push(i)
        stack_time = time.perf_counter() - start
        
        # Наш Queue
        start = time.perf_counter()
        queue = Queue()
        for i in range(size):
            queue.enqueue(i)
        queue_time = time.perf_counter() - start
        
        # Наш LinkedList
        start = time.perf_counter()
        lst = SinglyLinkedList()
        for i in range(size):
            lst.append(i)
        lst_time = time.perf_counter() - start
        
        print(f"  Python list: {py_time:.6f} сек")
        print(f"  Наш Stack:    {stack_time:.6f} сек")
        print(f"  Наш Queue:    {queue_time:.6f} сек")
        print(f"  Наш LinkedList: {lst_time:.6f} сек")


def practical_example() -> None:
    """Практический пример использования структур данных."""
    print(f"\n{'='*60}")
    print("Практический пример: проверка сбалансированности скобок")
    print('='*60)
    
    def is_balanced(expression: str) -> bool:
        """Проверяет, сбалансированы ли скобки в выражении."""
        stack = Stack()
        brackets = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in brackets.keys():  # Открывающая скобка
                stack.push(char)
            elif char in brackets.values():  # Закрывающая скобка
                if stack.is_empty():
                    return False
                opening = stack.pop()
                if brackets[opening] != char:
                    return False
        
        return stack.is_empty()
    
    test_cases = [
        ("(2 + 3) * [4 - 1]", True),
        ("{([<>])}", True),
        ("((())", False),
        ("([)]", False),
        ("", True)
    ]
    
    for expr, expected in test_cases:
        result = is_balanced(expr)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expr}' -> {result} (ожидалось: {expected})")


def main():
    print("=== Тестирование структур данных и бенчмарки ===")
    
    # Базовые тесты
    print("\n1. Базовые тесты работы структур:")
    
    # Стек
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"После pop: {stack}")
    
    # Очередь
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"\nОчередь: {queue}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"После dequeue: {queue}")
    
    # Связный список
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.prepend(5)
    print(f"\nСвязный список: {lst}")
    print(f"Элемент по индексу 1: {lst.get(1)}")
    
    # Бенчмарки
    benchmark_stack(10000)
    benchmark_queue(10000)
    benchmark_linked_list(1000)
    compare_append_performance()
    practical_example()
    
    print(f"\n{'='*60}")
    print("✅ Все тесты завершены успешно!")
    print('='*60)


if __name__ == "__main__":
    main()