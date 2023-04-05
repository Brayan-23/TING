from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()
        self.__lenght = 0

    def __len__(self):
        return self.__lenght

    def enqueue(self, value):
        self.data.append(value)
        self.__lenght += 1

    def dequeue(self):
        if len(self.data) == 0:
            return None
        self.__lenght -= 1
        return self.data.pop(0)

    def search(self, index):
        if index >= 0 and index <= len(self.data) - 1:
            return self.data[index]
        raise IndexError('Índice Inválido ou Inexistente')
