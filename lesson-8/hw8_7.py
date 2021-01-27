"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, real, imag=0):
        self.__real = real
        self.__imag = imag

    def __add__(self, other):
        return ComplexNumber(self.__real + other.__real, self.__imag + other.__imag)

    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return ComplexNumber(other * self.__real, other * self.__imag)
        elif isinstance(other,ComplexNumber):
            return ComplexNumber(self.__real * other.__real - self.__imag*other.__imag,\
                             self.__imag * other.__real + self.__real * other.__imag)
        else:
            raise ValueError("Invalid object type")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return ComplexNumber((self.__real * other.__real + self.__imag * other.__imag)/(other.__real**2 + other.__imag**2),\
                             (self.__imag * other.__real - self.__real * other.__imag)/(other.__real**2 + other.__imag**2))

    def __str__(self):
        return f"{self.__real}{self.__imag:+}*i"

    def __abs__(self):
        return self.__real**2 + self.__imag**2

    def __invert__(self):
        return self.conj()

    def conj(self):
        return ComplexNumber(self.__real,-self.__imag)

    @property
    def re(self):
        return self.__real

    @property
    def im(self):
        return self.__imag

c1 = ComplexNumber(2, -1.1)
c2 = ComplexNumber(5)
c3 = ComplexNumber(0,2.1)

print(c1)
print(c2)
print(c3)

print(c1 + c2 + c3)
print(c1 * c2 * c3)
print(c1 / c2)

print(abs(c1))

print(~c1)
print(c3.conj())

print(c1 * 2)

try:
    print("a"*c1)
except:
    print("Неверные аргументы")