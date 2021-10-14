def mergeSort(array):
    lenTop = len(array)-1
    if lenTop>1:
        mitte = lenTop//2
        a=mergeSort(array[:mitte+1])
        b=mergeSort(array[mitte+1:])
        merge(a, b)
    return array


def merge(left, right):
    print(left, right)
    i = 0
    j = 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            print("LEFT", left[i], ": right", right[j])
            arr.append(right[j])
            right.pop(j)
            
        else:
            arr.append(left[i])
            left.pop(i)
    print(left, right)
    print(arr)

def mergeSort(lst, n):
    if n < 2:
        return
    
    mid = n/2
    l = []

# create array and put numbers in it
arr = [3, 1, 56, 21, 5]
# for i in range(10, 1, -1):
#     arr.append(i)

merge(arr, [4, 2, 1])