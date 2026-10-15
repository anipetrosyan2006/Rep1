def build_last_position(pattern):
    last = {}
    for index in range(len(pattern)):
        last[pattern[index]] = index
    return last


def boyer_moore_search(text, pattern):
    last = build_last_position(pattern)
    print("Pattern:", pattern)
    print("Last positions:", last)

    shift = 0

    while shift <= len(text) - len(pattern):
        print("\nPattern placed at index", shift)

        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            print("  Text index", shift + j, "matches pattern index", j, "->", pattern[j])
            j -= 1

        if j < 0:
            print("  Pattern found at index", shift)
            shift += 1
        else:
            bad = text[shift + j]
            print("  Mismatch: text has", bad, "but pattern has", pattern[j])

            position = last.get(bad, -1)
            move = max(1, j - position)
            print("  Last position of", bad, "in pattern:", position, "-> shift by", move)
            shift += move


boyer_moore_search("ABABABABC", "ABABC")