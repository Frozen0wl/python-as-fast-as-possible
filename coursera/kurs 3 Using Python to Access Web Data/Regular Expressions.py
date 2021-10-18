import re
text = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

y = re.findall('^From (\S+@\S+)', text)
print(y)
x = re.findall('^From \S+(@\S+)', text)
print("\n", x)

atpos = text.find('@')
print(atpos)

print()
z = re.findall('@([^ ]*)', text)
print(z)

v = re.findall('^From .*@([^ ]*)', text)
print(v)
# ^	        Matches the beginning of a line
# $	        Matches the end of the line
# .	        Matches any character
# \s	    Matches whitespace
# \S	    Matches any non-whitespace character
# *	        Repeats a character zero or more times
# *?	    Repeats a character zero or more times (non-greedy)
# +	        Repeats a character one or more times
# +?	    Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# (	        Indicates where string extraction is to start
# )	        Indicates where string extraction is to end
# \         if you want to use one of the punctuations above

