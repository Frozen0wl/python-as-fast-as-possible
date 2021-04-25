x = {'key' : 4}

print(x['key'])

x['key2'] = 5

x[2] = 8
print(x)

print(list(x.values()))
print(list(x.keys()))
del x[2]
print(x)

for key, value in x.items():
    print(key, value)

print()

for key in x:
    print(key, x[key])




