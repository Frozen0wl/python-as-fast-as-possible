a = [1, 2, 3, 4, -1]
def insertion(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j>=0 and arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            i -= 1
            print(arr)

insertion(a)

# komplexität = n^2/4