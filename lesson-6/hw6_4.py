#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала вперед")

    def stop(self):
        print(f"Машина остановилась")

    def turn(self,direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} {self.speed} км/ч")


class TownCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed,color,name,False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость автомобиля {self.name} {self.speed} км/ч, превышение допустимого порога скорости")
        else:
            print(f"Скорость автомобиля {self.name} {self.speed} км/ч")

class WorkCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed,color,name,False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость автомобиля {self.name} {self.speed} км/ч, превышение допустимого порога скорости")
        else:
            print(f"Скорость автомобиля {self.name} {self.speed} км/ч")


class PoliceCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed,color,name,True)


class SportCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed,color,name,False)


c1 = Car(120,'черный','Audi',False)
c2 = TownCar(70,'металлик','Kia Rio')
c3 = WorkCar(50,'белый','Lada Granta')
c4 = PoliceCar(80,'серый','Lada Vesta')
c5 = SportCar(150,'красный','Ferrari')

print(f"{c1.name} {c1.color}")
c1.go()
c1.stop()
c1.turn('направо')
c1.show_speed()

print(f"{c2.name} {c2.color}")
c2.go()
c2.stop()
c2.turn('налево')
c2.show_speed()

print(f"{c3.name} {c3.color}")
c3.go()
c3.stop()
c3.turn('направо')
c3.show_speed()

print(f"{c4.name} {c4.color}")
c4.go()
c4.stop()
c4.turn('направо')
c4.show_speed()

print(f"{c5.name} {c5.color}")
c5.go()
c5.stop()
c5.turn('направо')
c5.show_speed()
