import requests

req = requests.get("https://uselessfacts.jsph.pl/random.json")

fact = req.json()["text"]

print(fact)