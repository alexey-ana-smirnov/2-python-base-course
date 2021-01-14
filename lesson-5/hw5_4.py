#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

def multiple_replace(target_str, replace_values):
    """
    Функция множественной замены слов в строке по словарю
    target_str: исходная строка
    replace_values: словарь подменяемых слов
    """
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str

file_input = open("5_4.txt","r")
file_output = open("5_4_out.txt","w")

trans = {
"One":"Один",
"Two":"Два",
"Three":"Три",
"Four":"Четыре"
}

for str in file_input:
    file_output.write(multiple_replace(str,trans))

file_input.close()
file_output.close()
