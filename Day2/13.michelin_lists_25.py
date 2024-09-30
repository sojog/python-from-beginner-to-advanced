

# %%
# 1. Calculating the sum of the elements of a list.
lst = [10, 20, 30, 40, 50]
print("sum:", sum(lst))

# %%
# 2. Finding the largest element in a list.
lst = [10, 20, 30, 40, 50]
print("max:", max(lst))

# %%
# 3. Finding the smallest element in a list.
lst = [10, 20, 30, 40, 50]
print("min:", min(lst))

# %%
# 4. Sorting a list in ascending order.
lst = [10, 20, 50, 30, 40]
lst.sort()
print("sorted list:", lst)

sorted_list = sorted([10, 20, 50, 30, 40])
print(sorted_list, type(sorted_list))

# %%
# 5. Sorting a list in descending order.
lst = [10, 20, 30, 40, 50]
lst.sort(reverse=True)
print("sorted list:", lst)

# %%
# 6. Checking if a value is found in a list.
value_to_find = 30
lst = [10, 20, 30, 40, 50]
for i in lst:
    if i == value_to_find:
        print("Found")
        break
else:
     print("Not found")  

print(value_to_find in lst)       

# %%
# 7. Concatenation of two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# %%
# 8. Removing duplicates from a list.
lst_with_duplicates = [1, 2, 2, 3, 4, 4, 5]

lst_with_no_dupl = []
for i in lst_with_duplicates:
    if i not in lst_with_no_dupl:
        lst_with_no_dupl.append(i)
print(lst_with_no_dupl)

lst_with_no_dupl  = list(set(lst_with_duplicates))
print(lst_with_no_dupl, type(lst_with_no_dupl))
print(lst_with_no_dupl[0])

# %%
# 9. Multiplying each element of a list by a number.
multiplier = 2
lst = [10, 20, 30, 40, 50]
print([ i * multiplier for i in lst])

# %%
# 10. Calculating the product of the elements of a list.
lst = [1, 2, 3, 4, 5]
product = 1
for i in lst:
    product *= i
print(product)

from functools import reduce
def multiply(x, y):
    return x * y
print(reduce(multiply, lst))
print(reduce(lambda x, y: x * y, lst))

# %%
# 11. Reversing a list.
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

print(list(reversed(lst)))
print(lst[::-1])

# %%
# 12. Finding the index of an element in a list.
element_to_find_index = 33
lst = [1, 2, 3, 4, 5, 3, 3]
for index, elem in enumerate(lst):
    if elem == element_to_find_index:
        print(index)
        break
else:
    print(-1)
print(lst.index(element_to_find_index))

# %%
# 13. Removing an item from a list.
element_to_remove = 4
lst = [1, 2, 3, 4, 5, 3, 3]
if element_to_remove in lst:
    lst.remove(element_to_remove)
print(lst)

# %%
# 14. Splitting a list into smaller pieces.
lst = [1, 2, 3, 4, 5, 3, 3, 10, 11]
chunk_size = 3

result = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
print(result)

# %%
# 15. Removing all null elements from a list.
lst_with_nulls = [0, 10, 0, 20, 0, 30]
lst_without_nulls = [ i for i in lst_with_nulls if i]
print(lst_without_nulls)

lst_without_nulls = list(filter(lambda x: bool(x), lst_with_nulls))
print(lst_without_nulls)

lst_without_nulls = list(filter(bool, lst_with_nulls))
print(lst_without_nulls)

# %%
# 16. Determining the most frequent item in a list.
lst = [0, 10, 0, 20, 0, 30, 10, 10]

freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

freq = { i : lst.count(i)  for i in lst }
print(freq)

print(max(freq.values()))
max_frequency = max(freq.values())
most_common = [i for i in freq if freq[i] == max_frequency]
print(most_common)


# %%
# 17. Calculating the average of a list.
lst = [1, 1, 1, 2, 2, 3]
avg = sum(lst) / len(lst)
print(round(avg, 5))
print(f"{avg:1f}")


# %%
# 18. Creating a list with unique elements from two given lists.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list(set(list1 + list2)))

# %%
# 19. Checking if a list is ordered or not.
lst = [1, 2, 3, 4, 6, 11, 20, 40, 55, 100, 120]
print(lst == sorted(lst))

# %%
# 20. Creating a list with pairs of elements from two given lists.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

pairs = list(zip(list1, list2))
print(pairs)

pairs = [(list1[i], list2[i]) for i in range(len(list1))]
print(pairs)

# %%
# 21. Calculating the sum of elements at even positions in a list.
even_list = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(sum(even_list[::2]))


# %%
# 22. Calculating the sum of elements at odd positions in a list.
even_list = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(sum(even_list[1::2]))

# %%
# 23. Multiplying two lists element by element.
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
product = [(list1[i] * list2[i]) for i in range(len(list1))]
print(product)

# %%
# 24. Finding the element closest to a given value in a list.
list_closest = [10, 20, 30, 40]
target_value = 16

closest = min(list_closest, key=lambda x:abs(x -target_value))
print(closest)

# %%
# 25. Rotating a list by n positions to the left.
n = 3
initial_list = [10, 20, 30, 40, 50, 60]
result =  initial_list[n:] + initial_list[:n] 
print(result)