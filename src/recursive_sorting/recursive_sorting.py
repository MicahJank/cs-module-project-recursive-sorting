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

    # start2 is the position in the array where the second half of the array starts
    # the first half goes from start up to mid so the second half will be from mid+1 to end
    start2 = mid + 1

    # arr[mid] is the last element for the first half of the array - arr[start2] is the first element in the second half
    # I know i am trying to sort the first half and the second half so that what i am left with is a single sorted array
    # i also know that the array from arr[start]-arr[mid] will be sorted and arr[start2]-arr[end] will be sorted
    # so with that in mind i can check the last element in the first half with the first element in the second half
    # if the arr[mid] is less that or equal then i can just return since that must mean that they are sorted already
    if arr[mid] <= arr[start2]:
        return
   
    # check the two havles of the array and if either of the pointers (start and start2) have reached there respective ends
    # then the loop will end
    while start <= mid and start2 <= end:
        # if the arr position in the first half is less than or equal to the arr in the second half that means we dont
        # need to change the array because the lesser value is already first
        if arr[start] <= arr[start2]:
            # so we can just increase the left half pointer
            start += 1
        else:
            # if the value in the second half is more than in the first that means we need to get that value moved to the left side
            # first grab that value that we want to move
            value = arr[start2]
            # grab the index of the second half of the array - we can use this when we want to make room on the left side for the new
            # value
            index = start2

            # using the index we can move elements over by 1 until we reach the position where we want to replace the value
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            # once we have reached that position then we can now assign the new value that position
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    # the base case for this function since i will be using recursion
    # i check to see if the left is smaller than the right - if it is it means the recursion has reached a point where
    # the left pointer and right pointer has overlapped and passed (or are equal) in which case that means the array 
    # i am trying to sort has a length of 1 which is when the recursion should stop
    if l < r:
        # find the middle of the array using the l and r variables
        mid = l + (r - l)//2
        # print("mid, left, right", mid, l, r)
        # first i use recursion to keep halving the left side of the array
        merge_sort_in_place(arr, l, mid)
        # next halve the right half the array with recursion until its down to 1 item
        merge_sort_in_place(arr, mid+1, r)
        # last can start merging all the pieces of the array together
        merge_in_place(arr, l, mid, r)
  
   
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
