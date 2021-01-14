#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

file_obj = open("5_2.txt","r",encoding="UTF-8")

str_count=0
word_count=0

for str in file_obj:
    str_count += 1
    word_count += len(str.split())

file_obj.close()

print(f"Число строк = {str_count}")
print(f"Число слов = {word_count}")