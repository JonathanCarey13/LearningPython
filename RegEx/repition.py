import re

# This should matchjust ghost
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# This should match just scary
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# We can use the method findall() to find all instances of
# our search, instead of the just the first occurance in the string.
# This should return scary, ghost and appea, but not the whole word
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# Using \b would specify the limit of characters for each word
# so this should return just scary and ghost, and omit appea unlike above
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

# We can also set specific rangers
# this should return any characters between 5-10 characters, regardless of the complete word
print(re.findall(r"\w{5,10}", "I really like watermellons"))
# They can be opened ended too
# this should return anything 5 characters or more
print(re.findall(r"\w{5,}", "I really like watermellons"))
# This should return characters that start with s and have at least 20 characters
# so this should match just strawberries and not watermellons
print(re.findall(r"w\w{,20}", "I really like watermellons"))