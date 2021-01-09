#5.	Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def isNumber(x):
    """
    Фукнция проверяет возможность конвертации строки x в числовое значение (Int или float).
    :param x: строковый параметр
    :return: True либо False
    """
    try:
        float(x)
        return True
    except ValueError:
        return False

print("Для завершения работы с программой нажимаем #+Enter")
summa=0

while True:

    list1 = input("Ввод последовательности чисел: ").split('#')
    list2 = list(map(float, list(filter(isNumber, list1[0].split()))))

    if len(list2)>0:
        summa = summa + sum(list2)
        print(summa)

    if len(list1)>1:
        print("Процесс завершен")
        break

