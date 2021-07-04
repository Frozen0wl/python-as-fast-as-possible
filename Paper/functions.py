def aaa(a):
    a+2
    if a == 100:
        return
    else:
        aaa(2)
        print(a)

aaa(3)