import requests
import re
import os

def filter_time(datetime):
    time = re.search("T(.*)\.", datetime).group(1)
    return time

london = requests.get("http://worldtimeapi.org/api/timezone/Europe/London")
berlin = requests.get("http://worldtimeapi.org/api/timezone/Europe/Berlin")
sydney = requests.get("http://worldtimeapi.org/api/timezone/Australia/Sydney")
los_angeles = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
sao_paulo = requests.get("http://worldtimeapi.org/api/timezone/America/Sao_Paulo")
tokio = requests.get("http://worldtimeapi.org/api/timezone/Asia/Tokyo")
kolkata = requests.get("http://worldtimeapi.org/api/timezone/Asia/Kolkata")

data_london = "London " + london.json()['abbreviation'] + " " + filter_time(london.json()['datetime'])
data_sydney = "Sydney " + sydney.json()['abbreviation'] + " " + filter_time(sydney.json()['datetime'])
data_berlin = "Berlin " + berlin.json()['abbreviation'] + " " + filter_time(berlin.json()['datetime'])
data_los_angeles = "Los Angeles " + los_angeles.json()['abbreviation'] + " " + filter_time(los_angeles.json()['datetime'])
data_sao_paulo = "Sao Paulo " + "BRT" + " " + filter_time(sao_paulo.json()['datetime'])
data_tokio = "Tokio " + tokio.json()['abbreviation'] + " " + filter_time(tokio.json()['datetime'])
data_kolkata = "Kolkata " + kolkata.json()['abbreviation'] + " " + filter_time(kolkata.json()['datetime'])

os.system('cat ascii_world.txt')
print("\n")
print(data_los_angeles + " | " + data_sao_paulo + " | " + data_london + "\n" + data_berlin + " | " + data_kolkata + " | " + data_tokio + " | " + data_sydney)
