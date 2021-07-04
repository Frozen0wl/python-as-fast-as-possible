a = []
def insertion(arr):
    enter = None
    while True:
        enter = input("Enter String: ")
        if enter == "!":
            break
        a.append(enter)
        
    for i in range(1, len(arr)):
        j = i-1
        while j>=0 and arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            i -= 1
    
    for i in range(0, len(arr)):
        print(arr[i])

insertion(a)

# komplexität = n^2/4