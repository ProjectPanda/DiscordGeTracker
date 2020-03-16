#
#  Author: Panda
#  Date: 03/15/20
#
import requests


def get_item(self):
    item_name = self
    item_url = 'https://api.zenyte.com/runelite/items/prices'

    r = requests.get(item_url)
    item_json = r.json()

    for i in item_json:
        if i['name'].lower() == item_name.lower():
            return format(i['price'], ',d')
