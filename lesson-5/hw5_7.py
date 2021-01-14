#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.

import json

firms_d={}
average_profit=0

with open("5_7.txt","r",encoding="UTF-8") as file_input:
    for str in file_input:
        (name,type,proceeds,costs) = str.split()
        proceeds, costs=map(int,[proceeds,costs])
        profit = proceeds - costs
        if proceeds > costs:
            average_profit += profit
            firms_d[name] = profit
        else:
            firms_d[name] = profit

average_profit = average_profit/len([name for name in firms_d if firms_d[name]>0])

with open("5_7.json","w",encoding="UTF-8") as file_output:
    json.dump([firms_d,{'average_profit':average_profit}],file_output)

