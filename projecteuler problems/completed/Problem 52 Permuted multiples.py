list = []
dic = {}
i = 0

def split(word):
    return [char for char in word]

def sort(list):
    for i in range(len(list)):
        for j in range(1, len(list)-i):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]

    return list

while True:
    i += 1
    list = split(str(i))
    list = sort(list)
    for j in range(2, 7):
        dic[str(j)+"x"] = split(str(j*i))
    for items in dic:
        dic[items] = sort(dic[items])
    bool = True
    for items in dic:
        for j in range(len(list)):
            if dic[items][j] == list[j]:
                continue
            else:
                bool = False
    if bool == True:
        print("solution", i)
        break

    if i % 10000 == 0:
        print(i)
    
        
        
        
        
    
    







