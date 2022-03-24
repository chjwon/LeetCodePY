def quick_sort(arr):
    """
    arr : List[num]
    return : sorted list
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
