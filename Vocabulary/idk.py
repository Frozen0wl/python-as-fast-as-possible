import pickle
import word

ls =[]
with open('words.pkl', 'rb') as words:
    while True:
        try:
            ls.append(pickle.load(words))
        except:
            break
print(ls)
print("hi")
