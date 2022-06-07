# Create a variable to link to the file we want to read
file = open("t-rexHaiku.txt")
# Print the variable and use the method readline to display the current line of text in the document
print(file.readline())
# Then the read method will display the rest of the text from the current position
print(file.read())
# Close the file
file.close()