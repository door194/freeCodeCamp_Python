def quick_sort(array):
    # Base case: arrays with 0 or 1 element are already sorted
    if not array:
        return array
    
    # Choose the middle element as the pivot
    pivot = array[len(array) // 2]
    
    # Partition the array into three distinct lists
    left = [num for num in array if num < pivot]
    middle = [num for num in array if num == pivot]
    right = [num for num in array if num > pivot]
    
    # Recursively sort the partitions and combine them
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([20, 3, 14, 1, 5]))
