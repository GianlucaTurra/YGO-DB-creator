import requests
from sqlalchemy.orm import Session

from models.card import Card

from models.card_set import CardSet


MONSTER_TYPES = {
    "Normal Monster",
    "Effect Monster",
    "Fusion Monster",
    "Ritual Monster",
    "Synchro Monster",
    "XYZ Monster",
}


def read_archetype(entry: dict) -> str | None:
    try:
        return entry["archetype"]
    except KeyError:
        return None


def read_monster_cards(entry: dict, card: Card) -> Card:
    card.attack = entry["atk"]
    try:
        card.defence = entry["def"]
    except KeyError:
        card.defence = None  # type: ignore
    card.attribute = entry["attribute"]
    card.level = entry["level"]
    return card


def read_card_sets(entry: dict, card: Card, session: Session) -> Card:
    seen = set()
    for card_set in entry["card_sets"]:
        if card_set["set_name"] in seen:
            continue
        seen.add(card_set["set_name"])
        card_s = session.query(CardSet).filter_by(name=card_set["set_name"]).first()
        if card_s:
            card.card_sets.append(card_s)
    return card


def fetch_cards(session: Session):
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    data = response.json()["data"]
    cards = []
    for entry in data:
        card = Card(
            name=entry["name"],
            type=entry["type"],
            race=entry["race"],
            desc=entry["desc"],
        )
        card.archetype = read_archetype(entry)  # type: ignore
        if entry["type"] in MONSTER_TYPES:
            card = read_monster_cards(entry, card)
        try:
            card = read_card_sets(entry, card, session)
        except KeyError:
            continue
        card.image = entry["card_images"][0]["image_url_small"]
        cards.append(card)
    return cards
