from sqlalchemy import Column, Integer, String
from db import Base
from sqlalchemy.orm import relationship

from models.card_association import card_association


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)
    race = Column(String)
    attack = Column(Integer)
    defence = Column(Integer)
    level = Column(Integer)
    attribute = Column(String)
    archetype = Column(String)
    card_sets = relationship("CardSet", secondary=card_association, back_populates="cards")
    image = Column(String)
    desc = Column(String)
