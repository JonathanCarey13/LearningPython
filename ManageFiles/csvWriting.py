import csv
hosts = [["workstation.local", "192.167.24.34"], ["webserver.cloud", "10.2.4.6"]]
with open("hosts.csv", "w") as cvsHosts:
    writer = csv.writer(cvsHosts)
    writer.writerows(hosts)