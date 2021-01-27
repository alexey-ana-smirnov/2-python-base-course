"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class MyZeroDivisionException(Exception):

    def __init__(self, divided,divider, message="Попытка деления на нуль"):
        self.divided = divided
        self.divider = divider
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.divided}/{self.divider} -> {self.message}'

class number(float):

    def __truediv__(self, other):
        if other != 0:
            return number(float(self)/float(other))
        elif other is not None:
            raise MyZeroDivisionException(self,other)

while True:

    try:
        divided, divider = map(number, input("Введите числитель и знаменатель через пробел: ").split())
        print(divided / divider)
    except MyZeroDivisionException as err:
        print(err)
    except ValueError as err:
        print(err)
