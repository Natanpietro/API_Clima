import requests

API_KEY = "913e6ec015f2c3b11877a6790afc9b3d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cidade = input("Escreva o nome da cidade que você quer saber o clima: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={cidade}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    tempo = data['weather'][0]['description']
    print(tempo)
    temperatura = round(data['main']['temp'] - 273.15, 2)
    print(temperatura, "ºC")
else:
    print("Erro!")