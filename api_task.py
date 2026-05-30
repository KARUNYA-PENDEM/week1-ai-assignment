import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("===== RANDOM JOKE =====")
    print("Setup:", data["setup"])
    print("Punchline:", data["punchline"])

else:
    print("Failed to fetch data.")