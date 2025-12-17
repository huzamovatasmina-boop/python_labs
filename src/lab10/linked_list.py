"""
Модуль содержит реализацию односвязного списка (Singly Linked List).
"""

from typing import Any, Optional, Iterator


class Node:
    """
    Узел односвязного списка.
    
    Содержит значение и ссылку на следующий узел.
    """
    
    def __init__(self, value: Any):
        """
        Инициализация узла.
        
        Args:
            value: Значение, хранимое в узле
        """
        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __str__(self) -> str:
        """Строковое представление узла."""
        return f"[{self.value}]"
    
    def __repr__(self) -> str:
        """Представление узла для отладки."""
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список.
    
    Состоит из узлов Node, каждый из которых содержит значение и ссылку 
    на следующий узел. Последний узел имеет next = None.
    
    Основные операции:
    - append(value): Добавить в конец - O(1) с tail, O(n) без tail
    - prepend(value): Добавить в начало - O(1)
    - insert(index, value): Вставить по индексу - O(n) в худшем случае
    - remove(value): Удалить по значению - O(n)
    - remove_at(index): Удалить по индексу - O(n)
    """
    
    def __init__(self):
        """Инициализация пустого списка."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        Добавляет элемент в конец списка.
        
        Сложность: O(1) при использовании tail, O(n) без tail.
        
        Args:
            value: Значение для добавления
        """
        new_node = Node(value)
        
        if self.is_empty():
            # Если список пуст, новый узел становится и head, и tail
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем в конец и обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавляет элемент в начало списка.
        
        Сложность: O(1).
        
        Args:
            value: Значение для добавления
        """
        new_node = Node(value)
        
        if self.is_empty():
            # Если список пуст, новый узел становится и head, и tail
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем в начало
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, index: int, value: Any) -> None:
        """
        Вставляет элемент по указанному индексу.
        
        Сложность: O(n) в худшем случае.
        
        Args:
            index: Позиция для вставки (0-based)
            value: Значение для вставки
            
        Raises:
            IndexError: Если индекс выходит за пределы списка
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Индекс {index} выходит за пределы списка (размер: {self._size})")
        
        if index == 0:
            # Вставка в начало
            self.prepend(value)
        elif index == self._size:
            # Вставка в конец
            self.append(value)
        else:
            # Вставка в середину
            new_node = Node(value)
            current = self.head
            current_index = 0
            
            # Ищем узел перед позицией вставки
            while current_index < index - 1:
                current = current.next
                current_index += 1
            
            # Вставляем новый узел
            new_node.next = current.next
            current.next = new_node
            
            self._size += 1
    
    def remove(self, value: Any) -> bool:
        """
        Удаляет первое вхождение указанного значения.
        
        Сложность: O(n).
        
        Args:
            value: Значение для удаления
            
        Returns:
            True если элемент был удалён, False если не найден
        """
        if self.is_empty():
            return False
        
        # Специальный случай: удаление первого элемента
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            
            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None
            
            return True
        
        # Ищем узел, предшествующий удаляемому
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # Если нашли узел для удаления
        if current.next is not None:
            current.next = current.next.next
            self._size -= 1
            
            # Если удалили последний элемент, обновляем tail
            if current.next is None:
                self.tail = current
            
            return True
        
        return False
    
    def remove_at(self, index: int) -> Any:
        """
        Удаляет элемент по указанному индексу и возвращает его значение.
        
        Сложность: O(n) в худшем случае.
        
        Args:
            index: Индекс элемента для удаления
            
        Returns:
            Значение удалённого элемента
            
        Raises:
            IndexError: Если индекс выходит за пределы списка
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Индекс {index} выходит за пределы списка (размер: {self._size})")
        
        # Специальный случай: удаление первого элемента
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
            
            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None
            
            return value
        
        # Ищем узел, предшествующий удаляемому
        current = self.head
        current_index = 0
        
        while current_index < index - 1:
            current = current.next
            current_index += 1
        
        # Удаляем узел
        value = current.next.value
        current.next = current.next.next
        self._size -= 1
        
        # Если удалили последний элемент, обновляем tail
        if current.next is None:
            self.tail = current
        
        return value
    
    def get(self, index: int) -> Any:
        """
        Возвращает значение элемента по указанному индексу.
        
        Сложность: O(n).
        
        Args:
            index: Индекс элемента
            
        Returns:
            Значение элемента
            
        Raises:
            IndexError: Если индекс выходит за пределы списка
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Индекс {index} выходит за пределы списка (размер: {self._size})")
        
        current = self.head
        current_index = 0
        
        while current_index < index:
            current = current.next
            current_index += 1
        
        return current.value
    
    def index(self, value: Any) -> int:
        """
        Возвращает индекс первого вхождения указанного значения.
        
        Сложность: O(n).
        
        Args:
            value: Значение для поиска
            
        Returns:
            Индекс элемента или -1, если не найден
        """
        current = self.head
        index = 0
        
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли список.
        
        Returns:
            True если список пуст, иначе False
        """
        return self.head is None
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.
        
        Returns:
            Количество элементов
        """
        return self._size
    
    def __iter__(self) -> Iterator[Any]:
        """
        Возвращает итератор по значениям списка.
        
        Returns:
            Итератор
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление списка.
        
        Returns:
            Строка вида "A -> B -> C -> None"
        """
        if self.is_empty():
            return "SinglyLinkedList(пуст)"
        
        result = []
        current = self.head
        
        while current is not None:
            result.append(str(current.value))
            current = current.next
        
        return " -> ".join(result) + " -> None"
    
    def __repr__(self) -> str:
        """Возвращает представление списка для отладки."""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def clear(self) -> None:
        """Очищает список (удаляет все элементы)."""
        self.head = None
        self.tail = None
        self._size = 0


def linked_list_example() -> None:
    """Пример использования односвязного списка."""
    print("=== Пример работы односвязного списка ===")
    lst = SinglyLinkedList()
    
    # Добавляем элементы
    lst.append("первый")
    lst.append("второй")
    lst.prepend("нулевой")  # Добавляем в начало
    
    print(f"Список после добавлений: {lst}")
    print(f"Размер списка: {len(lst)}")
    print(f"Первый элемент: {lst.get(0)}")
    print(f"Последний элемент: {lst.get(len(lst)-1)}")
    
    # Вставляем элемент
    lst.insert(2, "вставленный")
    print(f"\nПосле вставки по индексу 2: {lst}")
    
    # Ищем элемент
    search_value = "второй"
    index = lst.index(search_value)
    print(f"Элемент '{search_value}' найден по индексу: {index}")
    
    # Удаляем элемент
    removed = lst.remove("вставленный")
    print(f"\nУдаление 'вставленного': {'успешно' if removed else 'не найден'}")
    print(f"Список после удаления: {lst}")
    
    # Итерируемся по списку
    print("\nИтерация по списку:")
    for i, value in enumerate(lst):
        print(f"  Элемент {i}: {value}")


if __name__ == "__main__":
    linked_list_example()