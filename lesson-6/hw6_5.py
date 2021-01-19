#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    title = 'Канцелярская принадлежность'

    def Draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):

    title = 'Ручка'

    def Draw(self):
        print("Рисование ручкой")

class Pencil(Stationary):

    title = 'Карандаш'

    def Draw(self):
        print("Рисование карандашом")

class Handle(Stationary):

    title = 'Маркер'

    def Draw(self):
        print("Рисование маркером")


obj1=Stationary()
obj2=Pen()
obj3=Pencil()
obj4=Handle()

obj1.Draw()
obj2.Draw()
obj3.Draw()
obj4.Draw()

