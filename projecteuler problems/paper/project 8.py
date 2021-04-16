def foo():
    max_product = 0
    num = "string of input number"
    for e,n in enumerate(num):
        product = reduce((lambda x,y: x*y),map(int,(num[e:e+13])))
        if product > max_product: 
            max_product = product
    return max_product

a = foo()
