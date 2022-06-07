# Set variable to text document
file = open("spider.txt")
# Readlines function takes every line and puts them into a list
lines = file.readlines()
# The list is made so we can close the file now while still having access to the list I've just made
file.close()
lines.sort()
print(lines)