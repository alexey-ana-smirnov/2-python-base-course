#5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce

list_odd = list(range(100,1001,2))
product = reduce(lambda x,y:x*y,list_odd)

print(list_odd)
print(product)