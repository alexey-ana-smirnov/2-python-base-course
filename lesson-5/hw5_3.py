#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

file = open("5_3.txt","r")

total_salary = 0
person_count=0
low_salary_list=[]

for str in file:
    (lastname, salary) = str.split("\t")
    person_count += 1
    total_salary += int(salary)
    if int(salary)<20000:
        low_salary_list.append(str)

file.close()

if len(low_salary_list)>0:
    print("Сотрудники с заплатой ниже 20000 рублей:")
    print(*low_salary_list)
else:
    print("Все сотрудники имеют зарплату выше 20000 рублей:")

print(f"\nCредняя зарплата {total_salary/person_count:.2f} рублей")