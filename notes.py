# Noteworthy things from Python docs & tutorials:
# 14th February 2016
# mainly from: https://docs.python.org/2.7/tutorial/introduction.html

# In interactive mode, the last printed expression is assigned to
# the variable _. This makes it easy to refer back to the last thing
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)
# 113.06

# Keyboard shortcuts: Ctrl + / comments out selected/current line

# Strings can be within single or double quotes

# "\" can be used to escape quotes
# such as >>> 'doesn\'t' -> "doesn't"
# but print omits enclosing quotes & prints special characters,
# as in >>> print '"Isn\'t", she said' -> "Isn't", she said
# "The string is enclosed in double quotes if the string contains
# a single quote and no double quotes, otherwise it is enclosed in single quotes"

# To NOT interpret/escape special characters with \, use raw strings by adding an r before the first quote: >>> print 'C:\some\name'  # here \n means newline!
# C:\some
# ame
# >>> print r'C:\some\name'  # note the r before the quote
# C:\some\name

# To span multiple lines with string literals, use triple quotes
# eg: $ print """"\
# Usage: thingy [OPTIONS]
#   -h          does this thing here
#   -H hostname something something
# """

# concatenate with +
# such as in outputTesting.py
# or >>> 3 * 'un' + 'ium'
# will give 'unununium'

# two string literals (enclosed between quotes) will be concatenated AUTOMAGICALLY
# >>> 'Py' 'thon'
# returns 'Python'
# useful if you need to break long strings, can just put strings within parentheses
# >>> text = ('put several strings within parentheses ' 'to join them')
# >>> text
# 'put several strings within parentheses to join them'

# Strings are indexed with first character is ZERO

# No character type, it's just a string of size one
# >>> word = "Python"
# word[0] # character in position 0
# 'P'
# >>> word[5]
# 'n'
# indices can be NEGATIVE, they start counting from the right
# >>> word[-1] # last char
# 'n'
# can slice to get a substring (inclusive)
# >>> word[0:2]
# 'Py'
# slice index defaults:
# [:2] is beginning to 2nd position (excluded)
# [4:] is from position 4 (included) to the end
# [-2:] is characters from second-last to end
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# python strings cannot be changed == "immutable"
# cannot assign to indexed position in a string
# >>> word = "python"
# >>> word[0] = "j"
# ... TypeError: 'str' object does not support item assignment
# need to create a new string for this sort of thing
# like >>> 'j' + word[0]

# len() returns length of a string; >>> len(word) will give you 6
# len() can also be used on lists

# lists are comma-separated values between square brackets;
# can contain different types, can be indexed and sliced, concated, etc
# can be nested (contain lists of other lists)
# BUT, lists are a mutable type, content can be changed (unlike strings)
# >>> cubes = [1, 8, 27, 65, 125]
# >>> cubes[3] = 64  # replace the wrong value
# >>> cubes
# [1, 8, 27, 64, 125]

# add items to end of list by using append() method

# remote bits of list by assigning empty list: []

#### start at section 3.2 "First steps towards programming"
# https://docs.plython.org/2.7/tutorial/introduction.html

# 27/02/2016
# strings, numeric, boolean & null
# boolean logic wise, it's about whether it's evaluated as true or false
# FALSE= false, none, 0 (any numerical), empty sequence, empty dictionary or anything returning any of those.
# TRUE= true, not the false things :)

# number types: integer (whole number) or float (floating point number)
# text types: strings or characters
# boolean types: true or false

# Python is a dynamically typed language: variables contain data & python can evaluate variables as different things given different contexts.

# lists or array is a sorted list of other variables

# names of variables can't have spaces, can have underscores, can't start with a number
# no special characters
# phrase of at least 2 words: camelCase & snake_case(<-PEP8 standard)
# variable names will start with a lower case letter unless they're determining a class

# python does indentation to tell it what to do about namespaces and so on.
# 0 indent is one namespace
# 4 indent is next namespace & not accessible by other namespace
#


