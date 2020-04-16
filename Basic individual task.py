import timeit
from copy import deepcopy
from numpy.random import randint


def timeSort(func, number=1):
    """Функція знаходження часу роботи функцій.

    Застосовується через модуль timeit."""
    return timeit.timeit(str(func))


def bubbleSort(arr):
    """Функція бульбашкового сортування."""

    # лічильники порівнянь та обмінів
    counter_if, counter_replace = 0, 0
    n = len(arr)

    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                counter_replace += 1
            counter_if += 1
    # повернення параметрів у залежності від вибору користувача
    if choise:
        return arr, counter_if, counter_replace
    else:
        return None, counter_if, counter_replace


def selectionSort(arr):
    """Функція сортування вибором."""

    # лічильники
    counter_if, counter_replace = 0, 0
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
                counter_replace += 1
            counter_if += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # повернення параметрів
    if choise:
        return arr, counter_if, counter_replace
    else:
        return None, counter_if, counter_replace


def insertionSort(arr):
    """Функція сортування вставками."""

    # лічильники
    counter_if, counter_replace = 0, 0
    n = len(arr)

    for i in range(1, n):
        keys = arr[i]

        j = i - 1
        while j >= 0 and keys < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            counter_replace += 1
        arr[j + 1] = keys
        counter_if += 1

    # повернення параметрів
    if choise:
        return arr, counter_if, counter_replace
    else:
        return None, counter_if, counter_replace


# користувач обирає як створити масив чисел
key = input('F - згенерувати рандомні числа;\n'
            'T - ввести власноруч до 30 чисел;\n>>> ')
if key == 'F':
    # логічний ключ чи обрав користувач вводити свій масив, чи наповнити рандомно
    choise = False

    # створення масиву з рандомними числами в діапазоні [0, 100], розміром, який введе сам користувач
    array = list(randint(low=1, high=1000, size=int(input('Введіть розмір масиву: '))))
else:
    choise = True

    # якщо розмір введеного масиву користувачем буде більшим 30, то він буде вводити доки не буде <= 30
    while True:
        array = list(map(int, input('Введіть до 30 чисел через пробіл:\n').split()))
        if len(array) <= 30:  #
            break

# створюються глибокі копії основного масиву
array1, array2, array3 = deepcopy(array), deepcopy(array), deepcopy(array)

# отримання результатів функцій сортування
bubble_result = bubbleSort(array1)
selection_result = selectionSort(array2)
insertion_result = insertionSort(array3)

# логічний ключ вибору користувача
# якщо він True, то будуть виведені відсортовані масиви в напрямку зростання, та навпраки
if choise:
    print(f'\nВідсортований масив у напряму спадання:\n{bubble_result[0]}\n'
          f'Відсортований масив у напряму зростання:\n{selection_result[0]}')

print(f'\n<<<Сортування бульбашкою>>>\n'
      f'Число порівнянь: {bubble_result[1]}\n'
      f'Число обмінів: {bubble_result[2]}\n'
      f'Час роботи: {timeSort(bubbleSort(array1))}')

print(f'\n<<<Сортування вибором>>>\n'
      f'Число порівнянь: {selection_result[1]}\n'
      f'Число обмінів: {selection_result[2]}\n'
      f'Час роботи: {timeSort(selectionSort(array2))}')

print(f'\n<<<Сортування вставками>>>\n'
      f'Число порівнянь: {insertion_result[1]}\n'
      f'Число обмінів: {insertion_result[2]}\n'
      f'Час роботи: {timeSort(insertionSort(array3))}')
