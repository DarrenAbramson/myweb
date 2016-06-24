import csv
import subprocess
import time

with open('myweburls.csv', 'rb') as csvfile:
    httlauncher = csv.DictReader(csvfile)
    for row in httlauncher:
        url = row['url']
        name = str.split(url, "/")[3]
        print name
        print url
        subprocess.call(["httrack", url, "-O", name + "/\"" , "\"myweb.dal.ca/*\"", "-v"])
        time.sleep(2)
