#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def ClothConsumption(self):
        pass

class Coat(Clothes):

    def __init__(self,size):
        self.size = size

    @property
    def ClothConsumption(self):
        return (self.size/6.5 + 0.5)

class Suit(Clothes):

    def __init__(self,height):
        self.height = height

    @property
    def ClothConsumption(self):
        return (2 * self.height + 0.3)

class ClothProduction:

    def __init__(self,coat_size_list,suit_height_list):
        self.coat_list=[]
        self.suit_list=[]
        for size in coat_size_list:
            self.coat_list.append(Coat(size))
        for height in suit_height_list:
            self.suit_list.append(Suit(height))

    @property
    def ClothConsumption(self):
        consumption = 0
        for coat in self.coat_list:
            consumption += coat.ClothConsumption
        for suit in self.suit_list:
            consumption += suit.ClothConsumption
        return consumption


prod = ClothProduction([48,50,54,54,50],[1.80,1.86,1.76,1.88,1.67])

print(f"Суммарный расход ткани = {prod.ClothConsumption:.2f}")