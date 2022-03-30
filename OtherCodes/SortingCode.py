def bubble_sort(arr):
    """
    arr : List[num]
    return : sorted List
    """
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


def selection_sort(arr):
    """
    arr : List[num]
    return : sorted List 
    """
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                minIndex = j
        if not minIndex == i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


def insertion_sort(arr):
    """
    arr : List[num]
    return : sorted List
    """
    for i in range(1,len(arr)):
        num = arr[i]
        compareTemp = i - 1
        while compareTemp >= 0 and num < arr[compareTemp]:
            arr[compareTemp+1] = arr[compareTemp]
            compareTemp -= 1

        arr[compareTemp + 1] = num
    return arr


def merge(left, right):
    """
    sorting arr func
    used in merge sort
    """
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(arr):
    """
    arr : List(num)
    return recursion with merge func
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def quick_sort(arr):
    """
    arr : List[num]
    return : sorted List
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] # set pivot by mid of the arr
    lesserArr, equalArr, greaterArr = [],[],[]
    for num in arr:
        if num < pivot:
            lesserArr.append(num)
        elif num == pivot:
            equalArr.append(num)
        else: # num > pivot
            greaterArr.append(num)
    return quick_sort(lesserArr)+ equalArr + quick_sort(greaterArr)


def quick_selection(arr,k):
    """
    arr : List[num]
    k : k th number in arr(ascending order)
    return kth num (without sorting whole list)
    """
    if len(arr) == 1 and k == 1:
        return arr[0]
    pivot = arr[len(arr)//2] # set pivot by mid of the arr
    lesserArr, equalArr, greaterArr = [],[],[]
    for num in arr:
        if num < pivot:
            lesserArr.append(num)
        elif num == pivot:
            equalArr.append(num)
        else: # num > pivot
            greaterArr.append(num)
    
    if k < len(lesserArr): # k th num is in lesserArr
        return quick_selection(lesserArr,k)
    elif k < len(lesserArr) + len(equalArr): # k th num is in equalArr so return pivot
        return pivot
    else: # k th num is in greaterArr
        return quick_selection(greaterArr,k - len(lesserArr) - len(equalArr))



"""
testing zone
"""
numList = [1,5,2,5,2,3]
numList = merge_sort(numList)
print(numList)
