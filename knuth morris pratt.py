def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    lps = build_lps(pattern)
    print("Pattern:", pattern)
    print("LPS table:", lps)

    i = 0 
    j = 0  
    
    while i < len(text):
        if text[i] == pattern[j]:
            print("Text index", i, "matches pattern index", j, "->", text[i])
            i += 1
            j += 1

            if j == len(pattern):
                print("Pattern found at index", i - j)
                j = lps[j - 1]
        elif j > 0:
            print("Text index", i, "does not match pattern index", j, "->", text[i], "vs", pattern[j], "-> go back to", lps[j - 1])
            j = lps[j - 1]
        else:
            print("Text index", i, "does not match pattern index 0 -> move on")
            i += 1


kmp_search("ABABABABC", "ABABC")