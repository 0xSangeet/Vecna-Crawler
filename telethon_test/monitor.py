import os
import json
from alert import send_alert

def start_monitoring():
    dbs = [x for x in os.listdir() if x.endswith('.txt') and x != 'links.txt']

    with open('info.json', 'r') as f:
            data = json.load(f)
            if len(data) != 0:
                to_monitor = [[x['chat_id'], x['email']] for x in data]
                print(to_monitor)
                print("Emails fetched.")
            else:
                print('No emails to monitor.')

    for db in dbs:
        with open(db, 'r') as f:
            data = f.readlines()
            for line in data:
                for each_val in to_monitor:
                    if each_val[1] in line.replace('\n', ''):
                        print(f"Leak detected for email: {each_val[1]}")
                        send_alert(each_val[1], each_val[0])

start_monitoring()