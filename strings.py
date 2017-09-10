import random
import sys
import os

# Comment

'''
Multi
line
'''

print("Hello World")

name = "Caleb"

print(name)
name = 15

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

# Order of operation matters!

quote = "\" Always remember you are unique"

multi_line_quote = '''just
like everyone else'''

# conjoin strings
new_string = quote + multi_line_quote

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print('\n' *5)

print("I dont like ", end="")
print("newlines")
