class Node: # Класс узла
    def __init__(self, value=None, next_el=None):
        self.value = value
        self.next_el = next_el

# создаем класс переменных (списка)
class LinkedList:
    def __init__(self):
        self.head = None # первая (головная)
        self.tail = None # последняя (хвост)
        self.length = 0 # длина

    def clear(self): # функция очистки односвязного списка
        self .__init__()

    def add(self, x):
        self.length += 1 # Добавляем новый элемент
        if self.head is None:
            self.tail = self.head = Node(x, None) # Создаем новый узел из одного элемента

        else:
            self.tail.next_el = self.tail = Node(x, None)  # Делаем новый хвост, то есть создаем новый элемент узла

    def __str__(self): # Формируем красивую строку вывода данных на экран
        if self.head is not None:
            current = self.head
            out = '[' + str(current.value) + ', '
            while current.next_el is not None:
                current = current.next_el
                out = out + str(current.value) + ', '

            return out[:-2] + ']'

# создает односвязный список
one_list = LinkedList()
one_list.add(3)
one_list.add(15)
one_list.add(56)
print(one_list)
