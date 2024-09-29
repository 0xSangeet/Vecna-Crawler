import os
from termcolor import colored
from alert import send_alert


print(colored(r'''
 _   _                         _____                    _           
| | | |                       /  __ \                  | |          
| | | | ___  ___ _ __   __ _  | /  \/_ __ __ ___      _| | ___ _ __ 
| | | |/ _ \/ __| '_ \ / _` | | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
\ \_/ /  __/ (__| | | | (_| | | \__/\ | | (_| |\ V  V /| |  __/ |   
 \___/ \___|\___|_| |_|\__,_|  \____/_|  \__,_| \_/\_/ |_|\___|_|   
                                                                
''', 'red'))
print(colored('[+] Crawler running...', 'green'))

dbs = [x for x in os.listdir() if x.endswith('.txt') and (x != 'links.txt' and x != 'to_monitor.txt')]

with open('to_monitor.txt', 'r') as f:
    emails = [x.replace('\n', '') for x in f.readlines()]

if len(emails) != 0:
    print("Emails fetched.")
else:
    print('No emails to monitor.')

for db in dbs:
    with open(db, 'r') as f:
        data = f.readlines()
        for line in data:
            for each_val in emails:
                if each_val in line.replace('\n', ''):
                    print(f"Leak detected for email: {each_val}")
                    send_alert(each_val)
