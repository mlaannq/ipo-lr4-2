list = input("Введите числа через пробел: ") #запрашиваем у пользователя числа
list1 = [int(a) for a in list.split()]  # прописываем split для разделения элементов пробелом и запятой
list2 = [a**2 for a in list1] # возводим числа от пользователя в квадрат
print("Список возведенный в квадратов:", list2) # выводим числа от пользователя уже в квадрате
