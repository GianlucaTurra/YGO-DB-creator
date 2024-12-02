import requests

from models.card import Card


def fetch_cards():
    monster_types = {'Normal Monster', 'Effect Monster', 'Fusion Monster', 'Ritual Monster', 'Synchro Monster', 'XYZ Monster'}
    response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
    data = response.json()['data']
    cards = []
    for entry in data:
        card = Card(
            name=entry['name'],
            type=entry['type'],
            race=entry['race'],
            desc=entry['desc']
        )
        try:
            card.archetype = entry['archetype']
        except KeyError:
            pass
        if entry['type'] in monster_types:
            card.attack = entry['atk']
            card.defence = entry['defence']
            card.attribute = entry['attribute']
            card.level = entry['level']
        for card_set in entry['card_sets']:
            pass  # TODO: handle set with search
        card.image = entry['card_images']['image_url_small']
        cards.append(card)
    return cards
    