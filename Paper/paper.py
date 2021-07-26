import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = (input())
answer = ""
for unary in input().split():
    answer += unary

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(int(answer))