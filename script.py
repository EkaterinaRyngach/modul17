def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        x = array[: middle]
        for i in x:
            if i == element:
                x.remove(element)
        index_1 = (len(x) - 1)

        y = array[middle:]
        for n in y:
            if n <= element and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_2 = array.index(f)

        return [index_1, index_2]

    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def sort_array(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x


array = list(map(int, input("Введите последовательность чисел через пробел").split()))
element = int(input("Введите произвольное число"))

print(array)
print(element)

sort_array(array)

if element < array[0]:
    print('0')
elif element == array[0]:
    print('1')
elif element >= array[len(array) - 1]:
    print(len(array) - 1)
else:
    if array.count(element):
        index_left, index_right = binary_search(array, element, 0, len(array))
        print(index_left, index_right)
    else:
        array.append(element)
        sort_array(array)
        print(array)
        index_left, index_right = binary_search(array, element, 0, len(array))
        print(index_left, index_right - 1)


