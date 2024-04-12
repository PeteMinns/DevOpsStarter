import requests
import os
from todo_app.data.item import Item

def get_items():
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists"
    params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "cards": "open"
    }

    response = requests.get(url, params=params)
    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            cards.append(item)

    return cards

def add_item(title):
    url = f"https://api.trello.com/1/cards"
    params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "name": title,
        "idList": os.getenv("TRELLO_TO_DO_LIST_ID")
    }

    response = requests.post(url, json = params)

    response.raise_for_status()

def complete_item(id):
    url = f"https://api.trello.com/1/cards/{id}"
    params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_DONE_LIST_ID")
    }

    response = requests.put(url, json = params)

    response.raise_for_status()