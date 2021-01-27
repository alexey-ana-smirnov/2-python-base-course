"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:

    def __init__(self, date):
        items = date.split('-')

        if len(items) != 3 or not self.validate(*items):
            raise ValueError(f"неверный формат даты {date}")

        self.day, self.month, self.year = Date.transform(items)

    @classmethod
    def transform(cls, date):
        return [int(i) for i in date]

    @staticmethod
    def validate(*date):
        try:
            day, month, year = [int(x) for x in date]
        except TypeError:
            return False

        days_in_month = 28 + (month + (month // 8)) % 2 + 2 % month + 2 * (1 // month)
        if month == 2:
            days_in_month += bool(not (year % 4) and (year % 100 or not (year % 400)))


        return all([1 <= day <= days_in_month, 1 <= month <= 12, year >= 0])

    def __str__(self):

        return f"{self.day:02}-{self.month:02}-{self.year:04}"


for date in ('31-11-2011', '01-13-1969', '29-02-2021', '29-02-2000'):
    try:
        print(Date(date))
    except ValueError as e:
        print(e)
