import requests

from models.card_set import CardSet


def fetch_sets():
    response = requests.get('https://db.ygoprodeck.com/api/v7/cardsets.php')
    sets = []
    for entry in response.json():
        card_set =CardSet(
            name=entry['set_name'],
            code=entry['set_code'],
            release_date=entry['tcg_date']
        )
        sets.append(card_set)
    