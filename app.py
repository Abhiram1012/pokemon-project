import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Pokemon:", data["name"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("Base Experience:", data["base_experience"])
else:
    print("API Failed")