def insertion_sort(arr):
    # loop from 1 to end of array
    for i in range(1, len(arr)):
        temp = arr[i]
​
        j = i
​
        while j > 0 and temp < arr[j - 1]:
            # copy element to left to this position
            arr[j] = arr[j - 1]
​
            j -= 1
​
        arr[j] = temp
​
    return arr