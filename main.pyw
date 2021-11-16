import time
from datetime import datetime as dt
# test host file
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.youtube.com", "youtube.com", "www.espn.com", "espn.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('This time is during working hours')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            # creates a list from the lines of the file
            content = file.readlines()
            # place the pointer before the content in the first line
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Outside of working hours.")
    time.sleep(5)
