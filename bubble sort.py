def bubble_sort_demo(numbers):
    data = numbers.copy()
    size = len(data)

    for i in range(size):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print("After pass", i + 1, ":", data)

    return data


values = [27, 13, 1, 15, 64, 33, 49]
print("Start:", values)
result = bubble_sort_demo(values)
print("Final:", result)
