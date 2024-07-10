import requests
import time


for i in range(10):
    with open('check.txt','a') as fl:
        url = "https://alma.plus/"

        check = requests.get(url)
        print(check.status_code,file=fl)
        time.sleep(1)
