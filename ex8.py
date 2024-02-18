#add new pip => requests
# first find JSON file and open it in json validator to be more organized
# responses 200 that mean the website work very will
# (data["data"]["timings"]["Fajr"]) => this attributes should be from json file and the same letter character cases
import requests

responses = requests.get("https://api.aladhan.com/v1/timingsByCity/18-02-2024?city=Amman&country=Jordan&method=8")

if responses.status_code ==200 :
    data = responses.json()
    #print(data)
    print(data["data"]["timings"]["Fajr"])
    print(data["data"]["timings"]["Dhuhr"])

    print()
else:
    print("Faild to load web API")