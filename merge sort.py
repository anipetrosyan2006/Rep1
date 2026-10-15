def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result = result + left[i:] + right[j:]

    print("Merge", left, "and", right, "->", result)
    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)


values = [27, 13, 1, 15, 64, 33, 49]
print("Start:", values)
final = merge_sort(values)
print("Final:", final)