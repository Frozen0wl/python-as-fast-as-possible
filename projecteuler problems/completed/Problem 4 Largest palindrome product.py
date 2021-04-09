def is_palindrome(x):
    sliced = str(x)[::-1]
    return sliced

biggest_palindrome = 0

for i in range(1000):
    for j in range(1000):
        n = i * j
        
        if(is_palindrome(n) == str(n)):
            if(n > biggest_palindrome):
                biggest_palindrome = n
                print(biggest_palindrome)
