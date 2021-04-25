# compare the first number with all of the others. if it is the smallest put it in first place and do the same with second, if not try with second one. 5 * 4 = 20 comparisons
# compare the first two numbers if they in order leave them as they are, otherwise swap them. repeat this process until there are no swaps: for n nums n*(n-1)/2 comparisons
# compare the second and third number if third is greater then second swap and compare second with first. do the same thing with the rest of the books until the last one: (4 * 5/2)/2 = 5 comparisons in average
# pick the middle value, all numbers smaller to array a, others array b . -quicksort
count = 0
a = [2, 3, 5, 1, 3]



for i in range(len(a)):
    for j in range(1, len(a)-i):
        count+=1
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]

   
print(a)
print(f'{count} comparisons')


# temp = 0
# num = len(a) - 1
# for i in range(len(a)):
#     for j in range(1, len(a)):
#         if(a[i]<a[j]):
#             temp += 1
#     if temp == num:
#         a[i], a[0] = a[0], a[i]
#     num - 1

# print(a)



