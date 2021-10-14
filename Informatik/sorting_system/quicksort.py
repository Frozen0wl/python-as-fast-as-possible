arr=[2, 5, 3, 9, 4, 7, 6, 10]

def quicksort(min, max):
    if max-min < 1:
        return
    pivot = arr[max]
    top = max
    bot = min

    condition = True
    while condition:
        while arr[top] > pivot:
            top -= 1
        while arr[bot] < pivot:
            bot += 1
        
        if top >= bot:
            arr[top], arr[bot] = arr[bot], arr[top]
            bot += 1
            top -= 1
        condition = top>=bot
    
    print("d>", arr)
    quicksort(min, top)
    print("b>", arr)

    quicksort(bot, max)
    print("a>", arr)



quicksort(0, len(arr)-1)
print(arr)
