def encrypt(word):
    word = word[::-1]
    newword = ''
    dic = {'a' : '0', 'e' : '1', 'i' : '2', 'o' : '2', 'u' : '3'}
    for i in word:
        if i in dic:
            newword += dic[i]
        else:
            newword += i
    newword += 'aca'
    return(newword)

print(encrypt('hallo'))

