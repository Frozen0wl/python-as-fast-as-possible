gui = []
def createGui():
    global gui
    gui = []
    for i in range(5):
        gui.append([])
        for j in range(5):
            gui[i].append(5)
gui.append(2)
createGui()
print(gui)