def first_non_repeating_letter(string):
    
    # counter = 0
    # for i in string:
    #     for j in string:
    #         if i.lower() == j.lower():
    #             counter += 1
    #             if counter > 1:
    #                  break
    #         counter = 0
    #     else:
    #         return i
        

    dic = {}
    for char in string:
        if char.lower() in dic:
            dic[char.lower()] += 1
        else:
            dic[char.lower()] = 1
    for char in string:
        if dic[char.lower()] == 1 :
            return char
    return ""


print(first_non_repeating_letter('a'), 'a')
print(first_non_repeating_letter('stress'), 't')
print(first_non_repeating_letter('moonmen'), 'e')

print(first_non_repeating_letter(''), '')

print(first_non_repeating_letter('abba'), '')
print(first_non_repeating_letter('aa'), '')

print(first_non_repeating_letter('~><#~><'), '#')
print(first_non_repeating_letter('hello world, eh?'), 'w')

print(first_non_repeating_letter('sTreSS'), 'T')
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')