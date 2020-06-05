# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    arrA_pointer = 0
    arrB_pointer = 0
    while arrA_pointer < len(arrA) and arrB_pointer < len(arrB):
        if arrA[arrA_pointer] < arrB[arrB_pointer]:
            merged_arr[i] = arrA[arrA_pointer]
            arrA_pointer += 1
        else:
            merged_arr[i] = arrB[arrB_pointer]
            arrB_pointer += 1
        
        i += 1
    else:
        if arrA_pointer < len(arrA):
            while arrA_pointer < len(arrA):
                merged_arr[i] = arrA[arrA_pointer]
                arrA_pointer += 1
                i += 1

        if arrB_pointer < len(arrB):
            while arrB_pointer < len(arrB):
                merged_arr[i] = arrB[arrB_pointer]
                arrB_pointer += 1
                i += 1
            

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here


    return arr
 

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
