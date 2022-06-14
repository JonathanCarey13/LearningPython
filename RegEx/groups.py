import re
# Establishing our search result
result = re.search(r"(\w*), (\w*)$", "Lovelace, Ada")

# This should return span=(0, 13) and a match for Lovelace, Ada
print(result)

# Since we ran the groups() method, it will return a tuple of 2 elements
print(result.groups())

# We can also access this tuple with indexing.
#  This will return the whole string
print(result[0])
# This will return the first group
print(result[1])
# And this will return the second group
print(result[2])

# And since we can index them, we can format their return.
# This should return the second group first, then the first group
print("{} {}".format(result[2], result[1]))

# Here is a function to see this in action
def rearrangeName(name):
    result = re.search(r"([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrangeName("Simpson, Marge"))
print(rearrangeName("Simpson, Homer"))
# We modified our search from the one above to include the capture of
# any middle initials and special character
print(rearrangeName("Simpson, Homer J."))