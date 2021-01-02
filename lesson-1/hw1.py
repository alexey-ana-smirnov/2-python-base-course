#1. ѕоработайте с переменными, создайте несколько, выведите на экран, запросите у пользовател€ несколько чисел и строк и сохраните в переменные, выведите на экран.
a=15
b=5.1
c=False

print(a,type(a))
print(b,type(b))
print(c,type(c))

print(a/b)
print(a//b)
print(a%b)
print(a**2)

print(f'Int {a}, float {b:.4f}, boolean {c}')

answer=input("“во€ операционна€ система:")

if answer == 'windows':
    print("Hi, Windows")
elif answer == 'linux':
    print("Hi, Linux")

