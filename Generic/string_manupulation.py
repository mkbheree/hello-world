#!Strings Advancement
"""A raw string completely ignores all escape characters and prints any backslash that appears in the string """
print(r'this isn\'t that easy to program')

# String interpolation
name = 'AI'
age = 50
print('my name is %s,of age %s' % (name, age))

# String Interpolation using f Strings
print(f'My name is {name}, of age {age+1}')

# Join() and Split()
print('ABC'.join(['x', 'y', 'z']))  # join function operates on list of strings to form a single string
print('My name is Meher'.split())  # splits the string into list of string,by default delimiter is whitespace
print('My name is Meher'.split('M'))
print('hello Meher'.partition('M'))  # partitions the string into before and after the separator
print('Meher'.center(20, '*'))      # rjust(), ljust(), and center() lets you ensure that strings are neatly aligned
print('    Hi Meher   bye'.lstrip())  # we can remove Whitespace with the strip(), rstrip(), and lstrip() Methods

print(ord('A'), chr(101))  # ord() , chr() are used to get the unicode or string resp.


"""
1.upper() and lower() converts the string to uppercase or lowercase resp.

2.The isupper() and islower() methods will return a Boolean True value if the string has at least one letter 
  and all the letters are uppercase or lowercase, respectively
  
3.isalpha() Returns True if the string consists only of letters and isn’t blank

5.4.isalnum() Returns True if the string consists only of letters and numbers and is not blank

6.isdecimal() Returns True if the string consists only of numeric characters and is not blank

7.isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

8.istitle() Returns True if the string consists only of words that begin with an uppercase letter 
  followed by only lowercase letters
"""