# Задача 30:  Заполните массив элементами арифметической прогрессии.
#  Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры.
#  Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1= int(input("Введите первый элемент прогрессии: "))
# d= int(input("Введите разность прогрессии: "))
# n=int(input("Введите количество элементов прогрессии: "))
# progression = []
# for i in range(1,n+1):
#     an=a1+(i-1)*d
#     progression.append(an)
#     print(progression)

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


arr = [1, 6, 7, 9, 10, 11, 30]
min_value = 10
max_value = 20
def element_index(arr,min_value,max_value):
    index = []
    for i in range(len(arr)):
        if min_value <=arr[i] <=max_value:
            index.append(i)

    return(index)

result = element_index(arr,min_value,max_value)
print (result)

