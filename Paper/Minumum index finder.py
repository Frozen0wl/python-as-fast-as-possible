a = [1, 2, 3, 4, 5, 6, 7, 8]

def minIndex(arr, s, e):
     
    sml = 10
    mindex = 0
     
    for i in range(s, e):
        if (sml > arr[i]):
            sml = arr[i]
            mindex = i
             
    return mindex
 
def fun2(arr, start_index, end_index):
     
    if (start_index >= end_index):
        return
         
    # minIndex() returns index of minimum value in
    # array arr[start_index...end_index]
    min_index = minIndex(arr, start_index, end_index)
    arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
    fun2(arr, start_index + 1, end_index)

print(fun2(a, 1, 6))