import timeit
from copy import deepcopy
from numpy.random import randint


def timeSort(func, number=1):
    """Функція знаходження часу роботи функцій.

    Застосовується через модуль timeit."""
    return timeit.timeit(str(func))


def cocktailSort(arr):
    """Функція сортування перемішуванням."""

    counter_if, counter_replace = 0, 0
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    if key_sort:
        while swapped:
            swapped = False
            for i in range(start, end):
                counter_if += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    counter_replace += 1
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                counter_if += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    counter_replace += 1
                    swapped = True
            start += 1
    elif not key_sort:
        while swapped:
            swapped = False
            for i in range(start, end):
                counter_if += 1
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    counter_replace += 1
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                counter_if += 1
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    counter_replace += 1
                    swapped = True
            start += 1

    # повернення параметрів у залежності від вибору користувача
    return arr, counter_if, counter_replace


def shellSort(arr):
    """Функція сортування Шелла."""

    counter_if, counter_replace = 0, 0
    n = len(arr)
    gap = n // 2

    if key_sort:
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                counter_if += 2
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    counter_replace += 1
                    j -= gap
                arr[j] = temp
            gap //= 2

    if not key_sort:
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                counter_if += 2
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    counter_replace += 1
                    j -= gap
                arr[j] = temp
            gap //= 2

    # повернення параметрів
    return arr, counter_if, counter_replace


def heapSort(arr):
    """Функція пірамідальним сортуванням."""

    counter_if, counter_replace = 0, 0
    n = len(arr)

    if key_sort:
        def heapify(arr, n, i):
            """Функція процесу для перетворення у двійкову кучу піддерева з кореневим вузлом i, що є індексом в arr[].
                n - розмір кучі."""

            nonlocal counter_if, counter_replace
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                counter_replace += 1
                counter_if += 2
                heapify(arr, n, largest)

        for i in range(int(n / 2) - 1 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            counter_replace += 1
            heapify(arr, i, 0)

    elif not key_sort:
        def heapify(arr, n, i):
            """Функція процесу для перетворення у двійкову кучу піддерева з кореневим вузлом i, що є індексом в arr[].
                n - розмір кучі."""

            nonlocal counter_if, counter_replace
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] < arr[smallest]:
                smallest = l
            if r < n and arr[r] < arr[smallest]:
                smallest = r
            if smallest != i:
                (arr[i], arr[smallest]) = (arr[smallest], arr[i])
                counter_replace += 1
                counter_if += 2
                heapify(arr, n, smallest)

        for i in range(int(n / 2) - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            counter_replace += 1
            heapify(arr, i, 0)

    return arr, counter_if, counter_replace


while True:
    # користувач обирає як створити масив чисел
    key_choise = input('F - згенерувати рандомні числа;\n'
                       'T - ввести власноруч до 30 чисел;\n>>> ')
    if key_choise == 'F':
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

    # ключ сортуваня, якщо True - за зростанням, False - за спаданням
    sort = input(f'T - відсортувати за зростанням;\n'
                 f'F - відсортувати за спаданням;\n>>> ')
    if sort == 'T':
        key_sort = True
    else:
        key_sort = False

    # створюються глибокі копії основного масиву
    array1, array2, array3 = deepcopy(array), deepcopy(array), deepcopy(array)

    # # отримання результатів функцій сортування
    cocktail_result = cocktailSort(array1)
    shell_result = shellSort(array2)
    heap_result = heapSort(array3)

    print(f'\n<<<Сортування перемішуванням>>>\n'
          f'Масив:\n{cocktail_result[0]}\n'
          f'Число порівнянь: {cocktail_result[1]}\n'
          f'Число обмінів: {cocktail_result[2]}\n'
          f'Час роботи: {timeSort(cocktailSort(array1))}')

    print(f'\n<<<Сортування Шелла>>>\n'
          f'Масив:\n{shell_result[0]}\n'
          f'Число порівнянь: {shell_result[1]}\n'
          f'Число обмінів: {shell_result[2]}\n'
          f'Час роботи: {timeSort(shellSort(array2))}')

    print(f'\n<<<Пірамідальне сортування>>>\n'
          f'Масив:\n{heap_result[0]}\n'
          f'Число порівнянь: {heap_result[1]}\n'
          f'Число обмінів: {heap_result[2]}\n'
          f'Час роботи: {timeSort(heapSort(array3))}')

    if input('\nEnter - continue\n'
             'something - break\n'):
        break
