def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)


print(sorted(set(input("Type some sentence here: "))))
 
