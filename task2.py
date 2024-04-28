def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    

    while low <= high:

        mid = (low + high) // 2
        iterations += 1
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return iterations, arr[mid]
        print(low, high, len(arr))

    if low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, None

arr = [0.1, 0.3, 0.5, 0.7, 0.9]
x = 0.6
iterations, upper_bound = binary_search(arr, x)
print(iterations, upper_bound)
