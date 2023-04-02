def binary_search_index(list_of_numbers, number, left, right):
    if left > right:  # если левая граница превысила правую,
        return right  # значит элемент отсутствует

    if number <= list_of_numbers[0]:
        return 'Введеное вами число, меньше либо равно наименьшему числу в списке. Перезапустите программу.'
    if number > list_of_numbers[-1]:
        return len(list_of_numbers) - 1

    middle = (right + left) // 2  # находим середину
    if list_of_numbers[middle] == number:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif number < list_of_numbers[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search_index(list_of_numbers, number, left, middle - 1)
    else:  # иначе в правой
        return binary_search_index(list_of_numbers, number, middle + 1, right)


numbers = input('Введите целые числа через пробел: ')
list_of_numbers = list(map(int, numbers.split(" ")))
for i in range(len(list_of_numbers)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(list_of_numbers)):
        if list_of_numbers[j] < list_of_numbers[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        list_of_numbers[i], list_of_numbers[idx_min] = list_of_numbers[idx_min], list_of_numbers[i]

number = int(input('Введите целое число: '))
left = 0
right = len(list_of_numbers)-1

# запускаем алгоритм на левой и правой границе
print(binary_search_index(list_of_numbers, number, left, right))

