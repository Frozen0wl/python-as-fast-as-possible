def simplify(txt):
    a, b = txt.split("/")
    a, b = int(a), int(b)
    return a, b

    
print(simplify("1/3"))