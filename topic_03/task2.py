# Додаємо список 
list = [14, 4, 7, 4, 7]

def test_list_methods():
    print("Список:", list)

    # extend() - додає елементи другого списку
    test_list = list.copy()
    test_list.extend([9, 2, 6])
    print("Після extend([9, 2, 6]):", test_list)

    # append() - додає елемент в кінець списку
    test_list = list.copy()
    test_list.append(7)
    print("Після append(7):", test_list)

    # insert() - вставляє елемент на окрему позицію
    test_list = list.copy()
    test_list.insert(2, 8)  # вставляем 8 на позицию с индексом 2
    print("После insert(2, 8):", test_list)

    # remove() - видаляє перше входження елементу
    test_list = list.copy()
    test_list.remove(4)  # видаляэмо перше входження 4
    print("Пысля remove(1):", test_list)

    # clear() - очищую список
    test_list = list.copy()
    test_list.clear()
    print("Після clear():", test_list)

    # sort() - сортирує список
    test_list = list.copy()
    test_list.sort()
    print("Після sort():", test_list)

    # reverse() - розгортає список
    test_list = list.copy()
    test_list.reverse()
    print("Після reverse():", test_list)

    # copy() - повертає копію списку
    test_list = list.copy()
    copied_list = test_list.copy()
    print("Копія спику с copy():", copied_list)

# Запуск тестів
test_list_methods()