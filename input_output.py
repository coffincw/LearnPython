import random
import sys
import os

test_file = open("test.txt", "wb")

print(test_file.mode) #file mode ie. wb

print(test_file.name)

test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()

