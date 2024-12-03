from typing import List
from sqlalchemy import Column, Date, Integer, String
from db import Base
from sqlalchemy.orm import relationship

from models.card import Card
from models.card_association import card_association


class CardSet(Base):
    __tablename__ = "card_set"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    code = Column(String, unique=True)
    release_date = Column(Date)
    cards = relationship("Card", secondary=card_association, back_populates="card_sets")
