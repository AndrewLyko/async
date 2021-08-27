import requests
import time

start_time = time.time()

for number in range(1, 100):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()

print("--- %s seconds ---" % (time.time() - start_time))
