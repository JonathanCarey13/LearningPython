import csv
with open("csvDictionary.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{}'s birthday is {}.".format(row["name"], row["birthday month"])))