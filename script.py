import requests
import json

catalog = requests.get('https://api.mene.com/catalog').json()

items = {}
for item in catalog:
    ratio = 0
    try:
        ratio = item['grams'] / item['price']
    except:
        ratio = 0

    items[str(ratio)] = {
                            'price': item['price'],
                            'grams': item['grams'],
                            'ratio': ratio,
                            'name': item['title'],
                            'stock': item['variants'][0]['inStock']
                        }

new = []
for key in sorted(items.keys()):
    new.append(items[key])

with open('data.txt', 'w') as outfile:
    json.dump(new, outfile)
