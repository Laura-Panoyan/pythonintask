# Задача 4. Вариант 23.
# Напишите	программу,	которая	выводит	имя,	под	которым	скрывается	Илья Арнольдович Файзильберг.
#Дополнительно	необходимо	вывести	область	интересов	указанной личности,	место	рождения,	годы	рождения	и	смерти	(если	человек	умер), вычислить	возраст	на	данный	момент	(или	момент	смерти).
#Для	хранения	всех необходимых	данных	требуется	использовать	переменные.
#После	вывода информации	программа	должна	дожидаться	пока	пользователь	нажмет	Enter	для выхода.


# Sergeeva L.A.
# 13.04.17

from datetime import datetime

name = "Илья Арнольдович Файзильберг"
name1 = "Илья Арнольдович Ильф"
intrest = "Писательство"
birth = 1897
death = 1937
age = 39
place = "Одесса, Российская империя"

print(name, "более известен, как русский советский писатель, журналист и сценарист", name1)
print("Место рождения:", place)
print("Год рождения:", birth)
print("Год смерти:", death)
print("Возраст:", age)
print("Область интересов:", intrest)
input("\n\nНажмите Enter, чтобы выйти.")
