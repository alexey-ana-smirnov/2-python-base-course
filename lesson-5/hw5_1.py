#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

file_obj = open("5_1.txt","w")

while True:
    to_file = input("Введите текст: ")
    file_obj.write(f"{to_file}\n")
    if to_file=="":
        break

file_obj.close()

print("Работа программы завершена")