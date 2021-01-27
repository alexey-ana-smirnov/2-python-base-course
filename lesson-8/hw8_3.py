"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

class NotNumberException(Exception):

    def __init__(self, item, message="Введен нечисловой тип"):
        self.item = item
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.item} -> {self.message}'

class myList(list):

    def check(self,item):
        try:
            return float(item)
        except:
            raise NotNumberException(item)

    def append(self, item):
        super().append(self.check(item))

    def insert(self, i, item):
        super().insert(i,self.check(item))


my_list = myList()

while True:
    user_input = input("Введите очередной элемент списка, или 'stop' для выхода:")

    if user_input == "stop":
        break

    try:
        my_list.append(user_input)
    except NotNumberException as err:
        print(err)

print(my_list)
