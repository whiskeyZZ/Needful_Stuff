from random import random
import requests
import datetime
import random

req = requests.get("https://date.nager.at/api/v3/NextPublicHolidaysWorldwide")

today = datetime.date.today()
today = today.strftime('%Y-%m-%d')
holidays = []

for day in req.json():
    if day["date"] == today:
        holidays.append(day)



if len(holidays) > 0:
    rnd = random.randrange(0, len(holidays))
    country = requests.get("https://date.nager.at/api/v3/CountryInfo/{}".format(holidays[rnd]["countryCode"]))
    print("Today is " + holidays[rnd]["name"] + " in " + country.json()["commonName"] + "!")
