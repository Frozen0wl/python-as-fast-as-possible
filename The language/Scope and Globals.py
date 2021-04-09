x = 'tim'

def func(name):
    global x # without this the wouldn't change
    x = name

print(x)
func('changed')
print(x)