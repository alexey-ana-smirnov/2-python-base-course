#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

str=input("Введите числа через пробел: ")

file_input = open("5_5.txt","w")
file_input.write(str)
file_input.close()

file_input = open("5_5.txt","r")
numbers = map(int,file_input.readline().split())
file_input.close()

print(sum(numbers))