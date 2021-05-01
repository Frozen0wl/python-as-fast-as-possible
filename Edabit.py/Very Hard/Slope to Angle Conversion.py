import math
def convert(slope):
    return 90-round((math.degrees(math.asin(slope/math.sqrt(slope**2+1)))))

print(convert(-1))