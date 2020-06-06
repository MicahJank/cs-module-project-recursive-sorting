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
    # base case is when the all the initial arr items each are there own arrays - i can know this if the length of the array is 1
    if len(arr) > 1:
        # find the mid of the arr and then use that to split the array into to halves
        mid = int(len(arr) / 2)
        arrA = arr[0:mid]
        arrB = arr[mid:]
        
        # arrA will recurse all the way down until it cant halve itself anymore - after that it will start bubbling up
        arrA = merge_sort(arrA)
        # then arrB will do the same thing until it cannot halve itself anymore
        arrB = merge_sort(arrB)

        # finally arr can be assigned the value of merging arrA and arrB which will piece back together all the halfs but this time sorted
        arr = merge(arrA, arrB)


    return arr    
 

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    
    i = 0
    while 


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
