#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    __consumption = 25 #расход на квадратный метр

    def __init__(self,length,width):
        self.__length = float(length)
        self.__width = float(width)

    def expense(self):
        return self.__length*self.__width*Road.__consumption

r = Road(1000,10)

print(r.expense())