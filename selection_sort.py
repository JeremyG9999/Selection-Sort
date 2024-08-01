def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        print(array)
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
size = len(data)
selectionSort(data, size)
print(data)
#   https://www.programiz.com/dsa/selection-sort
# finding the smallest element from the list and swapping it with the first element in the unsorted list
# this continues until the entire list is completely sorted