def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = create_generator() # create a generator
print(mygenerator) # mygenerator is an object!
# <generator object create_generator at 0xb7555c34>

for i in mygenerator:
    print(i)