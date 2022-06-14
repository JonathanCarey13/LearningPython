import re

# This example shows how to extract process ID from a string
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
# This should return just the 12345
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

# Accessing index 1 will return None
# result = re.search(regex, "99 elephants in a [cage]")
# print(result[1])

def extractPid(logLine):
    regex = r"\[(\d+)]"
    result = re.search(regex, logLine)
    if result is None:
        return ""
    return result[1]

# This should return 12345
print(extractPid(log))
# This should retun None
print(extractPid("99 elephants in a [cage]"))