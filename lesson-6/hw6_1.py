#1.Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from time import time,ctime

class TrafficLight:

    __states = ['Red','Yellow','Green','Yellow']
    __timeouts = {'Red':7,'Yellow':2,'Green':10}

    def __init__(self):
        self.__color = 0
        self.__timestamp = time()

    def running(self,color):
        i=(self.__color+1)%4
        diff = time() - self.__timestamp
        if TrafficLight.__states[i]==color and diff>=TrafficLight.__timeouts[TrafficLight.__states[self.__color]]:
            self.__color=i
            self.__timestamp = time()

    def getcolor(self):
        return self.__states[self.__color]

tl1 = TrafficLight()

while True:
    sleep(1)
    tl1.running('Red')
    tl1.running('Yellow')
    tl1.running('Green')
    print(f"{ctime(time())}: {tl1.getcolor()}")