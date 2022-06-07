# This will open and immediately delete whatever contents the file had because we are opening it the "write" mode
with open("writingArea.txt", "w") as file:
    # This writes a string to the file
    file.write("I think crabs are pretty neat animals.")
# Normally I'd put print(file) here but I didn't so I can practice printing the file the command console instead