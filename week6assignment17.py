#Create a function to find the common elements
def find_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements

#Create both lists
listA = {5, 2, 4, 6, 9}
listB = {4, 5, 6, 7, 8}

result = find_common_elements(listA, listB)
print("Common elements: ", result)