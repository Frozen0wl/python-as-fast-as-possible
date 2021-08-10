a=int(input())+int(input())%7
print(a%7 if a>0 else 7)

a=int(input())+int(input())
while a>7:a-=7
print(a)