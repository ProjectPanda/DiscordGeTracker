#
#  Author: Panda
#  Date: 03/15/20
#
import requests


def get_price(self):
    item_name = self
    api_url = 'https://api.zenyte.com/runelite/items/prices'

    r = requests.get(api_url)
    item_json = r.json()

    for i in item_json:
        if i['name'].lower() == item_name.lower():
            return format(i['price'], ',d')


def get_small_icon(self):
    item_name = self
    api_url = 'https://api.zenyte.com/runelite/items/prices'

    r = requests.get(api_url)
    item_json = r.json()

    for i in item_json:
        if i['name'].lower() == item_name.lower():
            item_id = i['id']
            return f'https://static.runelite.net/cache/item/icon/{item_id}.png'


def get_large_icon(self):
    item_name = self
    api_url = 'https://api.zenyte.com/runelite/items/prices'

    r = requests.get(api_url)
    item_json = r.json()

    for i in item_json:
        if i['name'].lower() == item_name.lower():
            item_id = i['id']
            return f'http://services.runescape.com/m=itemdb_oldschool/obj_big.gif?id={item_id}'
