def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    smaller = []
    bigger = []

    for number in numbers[1:]:
        if number < pivot:
            smaller.append(number)
        else:
            bigger.append(number)

    print("List:", numbers, "| pivot:", pivot, "| smaller:", smaller, "| bigger:", bigger)

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


values = [27, 13, 1, 15, 64, 33, 49]
print("Start:", values)
final = quick_sort(values)
print("Final:", final)