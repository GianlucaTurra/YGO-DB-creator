from sqlalchemy import Column, ForeignKey, Integer, Table

from db import Base


card_association = Table(
    "card_association",
    Base.metadata,
    Column("card_id", Integer, ForeignKey("card.id"), primary_key=True),
    Column("card_set_id", Integer, ForeignKey("card_set.id"), primary_key=True),
)
