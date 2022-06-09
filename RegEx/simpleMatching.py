import re
# This method checks if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None

print(check_aei("academia")) #should be True
print(check_aei("aerial")) #should be False
print(check_aei("paramedic")) #should be True