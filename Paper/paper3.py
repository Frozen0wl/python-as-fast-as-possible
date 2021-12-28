import bisect

def get_interval(x):
    intvals = [5000, 7500, 10000, 20000, 30000, 40000, 50000]
    i = bisect.bisect_right(intvals,x)
    return intvals[i-1]

print (get_interval(5500))