import csv
f = open("csvExample.csv")
csvF = csv.reader(f)
for row in csvF:
    username, identifer, firstname, lastname = row
    print("Username: {}, Identifer: {}, Firstname: {}, Lastname: {}".format(username, identifer, firstname, lastname))
f.close()