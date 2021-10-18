file = open("mbox-short.txt")
dic = {}
for line in file:
    if line.startswith('From '):
        words = line.split()
        word = words[5]
        word.split(';')
        word = (word[0:2])
        dic[word] = dic.get(word, 0) + 1
       

lst = []
for k, v in dic.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)
for key, val in lst:
    print(key, val)