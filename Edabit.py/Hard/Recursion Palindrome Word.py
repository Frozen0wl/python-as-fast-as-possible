def is_palindrome(wrd):
    if len(wrd) <= 1:
        return True
    elif wrd[0] != wrd[-1]:
        return False
    else:
        return is_palindrome(wrd[1:-1])

print(is_palindrome("i i i"))