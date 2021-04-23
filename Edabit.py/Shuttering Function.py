def stutter(word):
    return (word[:2]+"... "+word[:2]+"... "+word+"?")

print(stutter("incredible"))

# optional solution
def stutter2(wrod):
    return '{0}... {0}... {1}?'.format(wrod[:2], wrod)

print(stutter2("hello"))


