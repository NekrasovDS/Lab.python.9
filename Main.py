import pandas as pd
import datetime
import locale

df = pd.read_csv('C:/Python/9_8_1.csv')
for val in df.values:
    for num, item in enumerate(val):
        print(f'{df.columns[num]}: {item}')
    print("\n")


date_str1 = "8 Апрель 2017 00:00"
locale.setlocale(locale.LC_ALL, 'ru_RU')
date_object1 = datetime.datetime.strptime(date_str1, "%d %B %Y %H:%M")


k = 0
result = pd.DataFrame()
date_list = df['Завершено'].tolist()
date_list = [x for x in date_list if x == x]
print(date_list)

for x in date_list:
    if x == "-":
        result = df[(df.get("Завершено", "") == "-")].reset_index()
        date_list.remove("-")
        k += 1
for x in date_list:
    if datetime.datetime.strptime(x, "%d %B %Y %H:%M") > date_object1:
        result = result._append(df[(df.get("Завершено", "") == x)].reset_index())
        k += 1

print(result.sort_values(by='Фамилия'))
print(f'Количество не сдавших: {k}')

df = pd.read_csv('C:/Python/9_8_2.csv')
date_str2 = "22 Май 2017 00:00"
date_object2 = datetime.datetime.strptime(date_str2, "%d %B %Y %H:%M")


k = 0
date_list = df['Завершено'].tolist()
date_list = [x for x in date_list if x == x]
print(date_list)

for x in date_list:
    if x == "-":
        result = df[(df.get("Завершено", "") == "-")].reset_index()
        date_list.remove("-")
        k += 1
for x in date_list:
    if datetime.datetime.strptime(x, "%d %B %Y %H:%M") > date_object2:
        result = result._append(df[(df.get("Завершено", "") == x)].reset_index())
        k += 1

print(result.sort_values(by='Фамилия'))
print(f'Количество не сдавших: {k}')
