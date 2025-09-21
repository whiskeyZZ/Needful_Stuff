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
        
def main():
    independence_day, country, flag = get_data() 
    print("On average every five days a country celebrates Independence from Great Britain")
    time.sleep(1)
    print(independence_day + " it is...")
    time.sleep(1)
    print(flag + flag + country + flag + flag + " !!!")

main()
