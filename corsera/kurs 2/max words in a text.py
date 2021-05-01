name = input('Enter file: ')
file = open(name)
dic = {}
for line in file:
    if line.startswith('From '):
        words = line.split()
        secondword = words[1]
        dic[secondword] = dic.get(secondword, 0) + 1
maxnumber = None
maxperson = None
for keys, values in dic.items():
    if maxnumber == None or maxnumber < values:
        maxnumber = values
        maxperson = keys
print(maxperson, maxnumber)