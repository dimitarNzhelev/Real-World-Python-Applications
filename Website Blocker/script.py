import time
from datetime import datetime as dt

host_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print(True)
        with open(host_path, 'r+') as f:
            content = f.read()
            print('in')
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + " " + website + "\n")
    else:
        print(False)
        with open(host_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()

    time.sleep(5)