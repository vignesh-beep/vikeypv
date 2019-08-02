def lexicographi_sort(s):
  return sorted(sorted(s), key=str.upper)

 
print(lexicographi_sort('4321'))
