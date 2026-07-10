def selection_sort(array):
    for i in range (len(array)):
        min_val = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_val]:
                min_val = j
        
        if min_val != i:
            array[i], array[min_val]  = array[min_val], array[i]

    return array

print(selection_sort([33, 1, 89, 2, 67, 245]))
