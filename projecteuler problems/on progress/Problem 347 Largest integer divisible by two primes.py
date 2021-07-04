import math
# A function to print all prime factors of
# a given number n
# def primeFactors(n):
#     lst = []
#     while n > 1:
#         for i in range(2, math.sqrt(n)+1):
#             while n % i == 0:
#                 n = n/i
#                 lst.append(i)
#     return lst

def primeFactors(n):
    lst = []
    while n % 2 == 0:
        n = n/2
        lst.append(2)
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = n/i
            lst.append(i)
    if n > 2:
        lst.append(n)
    return remDuplicates(lst)


def remDuplicates(lst):
    pureLst = []
    for item in lst:
        if item not in pureLst:
            pureLst.append(item)
    return pureLst

def M(num):
    dic = {}
    for i in range(1, num):
        x = primeFactors(i)
        if len(x) != 2:continue
        #print(i, x)
        dic[i] = x
    return(dic)

def flipDic(dic):
    flipped = {}

    for key, value in dic.items():
        print(key, value)
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    return flipped

flipped = {}
dic = {6: [2, 3.0], 10: [2, 5.0], 12: [2, 3.0], 14: [2, 7.0], 15: [3, 5.0], 18: [2, 3], 20: [2, 5.0], 21: [3, 7.0], 22: [2, 11.0], 24: [2, 3.0], 26: [2, 13.0], 28: [2, 7.0], 33: [3, 11.0], 34: [2, 17.0], 35: [5, 7.0], 36: [2, 3], 38: [2, 19.0], 39: [3, 13.0], 40: [2, 5.0], 44: [2, 11.0], 45: [3, 5], 46: [2, 23.0], 48: [2, 3.0], 50: [2, 5], 51: [3, 17.0], 52: [2, 13.0], 54: [2, 3], 55: [5, 11.0], 56: [2, 7.0], 57: [3, 19.0], 58: [2, 29.0], 62: [2, 31.0], 63: [3, 7], 65: [5, 13.0], 68: [2, 17.0], 69: [3, 23.0], 72: [2, 3], 74: [2, 37.0], 75: [3, 5], 76: [2, 19.0], 77: [7, 11.0], 80: [2, 5.0], 82: [2, 41.0], 85: [5, 
17.0], 86: [2, 43.0], 87: [3, 29.0], 88: [2, 11.0], 91: [7, 13.0], 92: [2, 23.0], 93: [3, 31.0], 94: [2, 47.0], 95: [5, 19.0], 96: [2, 3.0], 98: [2, 7], 99: [3, 11.0]}
for key, value in dic.items():
    print(key, value)
    if value not in flipped:
        flipped[value] = [key]




