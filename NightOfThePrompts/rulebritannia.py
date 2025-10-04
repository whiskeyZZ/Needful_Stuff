import time
from datetime import datetime, timedelta
import json

def load():
    with open('data.json', 'r') as f:
        return json.load(f)

def get_data():
    data = load()
    date = datetime.now()
    date_string = date.strftime("%d. %B")
    next_indepence_day = ""
    country_name = ""
    flag = ""
    found = False
    first_round = True
    while True:
        for d in data:
            if d["date"] == date_string:
                if first_round:
                    next_indepence_day = "Today"
                else:
                    next_indepence_day = "On " + d["date"]
                country_name = d["country"]
                flag =  d["flag"]
                found = True
                break
        if found:
            break
        else:
            delta = timedelta(days=1)
            date = date + delta
            date_string = date.strftime("%d. %B")
            first_round = False
    return next_indepence_day, country_name, flag

def get_ascii():
    with open('flag.txt', 'r') as ascii:
        return ascii.read().split("\n")

def main():
    independence_day, country, flag = get_data()
    ascii_list = get_ascii()
    count = 0
    for l in ascii_list:
        if count == 17:
            print(l + " On average every five days a country celebrates Independence from Great Britain")
        elif count == 18:
            print(l + " " + independence_day + " it's:")
        elif count == 19:
            print(l + " " + flag + flag + country + flag + flag + " !!!")
        else:
            print(l)
        count = count + 1

main()
