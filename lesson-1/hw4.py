#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
number,max_digit=number//10,number%10

while number>=1:
    digit=number%10
    number=number//10
    if digit>max_digit: max_digit=digit

print(f"Максимальная цифра {max_digit}")