import pickle
from word import word

def saveWord(word):
    with open('words.pkl','ab') as words:
        pickle.dump(word, words)

ls = []

with open('words.pkl', 'rb') as words:
    while True:
        try:
            ls.append(pickle.load(words))
            print(ls[-1].word)
        except:
            break        

for item in ls:
    print(item.word)
