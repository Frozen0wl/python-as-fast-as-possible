import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

# game loop
while True:
    pos = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    x1=0
    y1=0

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    
    # the location of the next window Batman should jump to.
    if pos == "UR":
        x1 = x+1
        h=y-1
        y-=1
        x=int((x1+w)/2)
    elif pos == "U":
        y=int((y1+h)/2)
        h=y+1
    
    if pos == "DR":
        x1 = x+1
        y1=y+1
        y+=1
        x=int((x1+w)/2)
    if pos == "D":
        y1=y+1
        y=int((y1+h)/2)
        
    print(w,h,x1,y1,x,y,file=sys.stderr, flush=True)
    print(x, y)
