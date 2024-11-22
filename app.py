import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("type") == "single":
            print(data.get("joke"))
        else:
            print(f"{data.get('setup')} - {data.get('delivery')}")
    else:
        print("Erreur lors de la récupération de la blague.")

if __name__ == "__main__":
    get_joke()
