def find_position(sorted_part, value):
    for index in range(len(sorted_part)):
        if sorted_part[index] > value:
            return index
    return len(sorted_part) 
    
def insertion_sort_steps(numbers):
    result = [] 

    for number in numbers:
        position = find_position(result, number)
        result.insert(position, number)
        print("Take", number, "-> insert at position", position, "->", result)

    return result


values = [2, 8, 4, 10, 3, 5, 6, 1]
print("Start:", values)
final = insertion_sort_steps(values)
print("Final:", final)