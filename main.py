list = input("Введите числла через пробел:") #запрашиваем у пользователя числа
list1 = [int(a) ** 2 for a in list.split()] #перебираем каждый элемент из списка, возводим в квадрат и разделяем запятой
print(list1) #вывод пользователю
