a = [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 1],
]
def tallest_skyscraper(lst):
    
    biggest = 0
    for i in range(len(a[1])):
        counter = 0
        for j in range(len(a)):
            if lst[j][i] == 1:
                counter +=1

            if counter > biggest:
                biggest = counter
    print(biggest)


tallest_skyscraper(a)
