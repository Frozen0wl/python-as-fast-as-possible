import os
path = '/Users/melih/Desktop/codes/BookPages/Right'
files = os.listdir(path)

def rename():
    for x in files:
        name =x[x.find("Seite")+6:]
        name ="S"+(7-len(name))*'0'+str(name)
        os.rename(os.path.join(path, x), os.path.join(path, name))
def correctName():
    i = 2
    for file in files:
        os.rename(os.path.join(path, file), os.path.join(path, f'{i}.jpg'))
        i += 2
def addzero():
    for file in files:
        name = file
        if len(name) < 7:
            name = (7-len(name))*'0'+str(name)
        os.rename(os.path.join(path, file), os.path.join(path, name))

# run all the commands in order
# start with rename() run the command and replace rename() with correctName() and so on...