def selection_sort_demo(numbers):
    data = numbers.copy()

    for i in range(len(data)):
        smallest = i
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest]:
                smallest = j

        data[i], data[smallest] = data[smallest], data[i]

        print("After step", i + 1, ":", data)

    return data


values = [27, 13, 1, 15, 64, 33, 49]
print("Start:", values)
result = selection_sort_demo(values)
print("Final:", result)