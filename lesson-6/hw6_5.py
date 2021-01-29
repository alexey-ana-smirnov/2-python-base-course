#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    title = 'Канцелярская принадлежность'

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):

    title = 'Ручка'

    def draw(self):
        print("Рисование ручкой")

class Pencil(Stationary):

    title = 'Карандаш'

    def draw(self):
        print("Рисование карандашом")

class Handle(Stationary):

    title = 'Маркер'

    def draw(self):
        print("Рисование маркером")


obj1=Stationary()
obj2=Pen()
obj3=Pencil()
obj4=Handle()

obj1.draw()
obj2.draw()
obj3.draw()
obj4.draw()

