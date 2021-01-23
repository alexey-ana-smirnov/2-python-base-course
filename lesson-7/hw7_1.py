#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self,list2d):
        self.matrix = list2d

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]

    @property
    def size(self):
        size = (len(self.matrix), len(self.matrix[0]))
        return size

    def __add__(self, other):
        if self.size != other.size:
            print("Размерности матриц не согласованы, сложение невозможно")
            return None
        else:
            result = []
            numbers = []
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    summa = other[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * x for x in y] for y in self.matrix]
            return Matrix(result)
        elif self.size[1] != other.size[0]:
            return 'Размерности матриц не согласованы'
        else:
            result = []
            for i in range(self.size[0]):
                res = []
                for j in range(other.size[1]):
                    el = 0
                    for k in range(self.size[1]):
                        el += self.matrix[i][k] * other.matrix[k][j]
                    res.append(el)
                result.append(res)
            return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

m1 = Matrix([[1,2],[3,4],[2,4]])
m2 = Matrix([[5,6,7],[7,8,9]])
print(m1)
print(m2)
print(f"размерность матрицы m1: {m1.size}")
print(f"размерность матрицы m2: {m2.size}")

print(3*m1)
print(m1*m2)

m3 = Matrix([[3,4],[5,6]])
m4 = Matrix([[11,4],[5,2]])
m5 = Matrix([[3,4],[4,6]])
print(m3)
print(m4)
print(m5)
print(f"размерность матрицы m3: {m3.size}")
print(f"размерность матрицы m4: {m4.size}")
print(f"размерность матрицы m5: {m5.size}")

print(m3+m4+m5)
