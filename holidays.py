from random import random
import requests
import datetime
import random

req = requests.get("https://date.nager.at/api/v3/NextPublicHolidaysWorldwide")

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')
holidays = []

for day in req.json():
    if day["date"] == tomorrow:
        holidays.append(day)

if len(holidays) > 0:
    rnd = random.randrange(0, len(holidays)-1)
    country = requests.get("https://date.nager.at/api/v3/CountryInfo/{}".format(holidays[rnd]["countryCode"]))
    print("Tomorrow is " + holidays[rnd]["name"] + " in " + country.json()["commonName"] + "!")