a = [12, 11, 13, 5, 6]

def recursive(arr):
    if(len(arr) <= 1):
        return
    
    recursive(arr[:len(arr)-1:])
    
    if arr[len(arr)-1] > arr[len(arr)-2]:
        arr[len(arr)-1], arr[len(arr)-2] = arr[len(arr)-2], arr[len(arr)-1]


print(recursive(a))