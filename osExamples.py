import os
import datetime
# Returns file size
print(os.path.getsize("spider.txt"))

# Returns file last modified date in Unix timestamp
print(os.path.getmtime("spider.txt"))
# This is hard to read so we'll import datetime and use some methods to made it legible
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))

# Returns absolute path
print(os.path.abspath("spider.txt"))