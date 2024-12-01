from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from db import Base
from models.card import Card
from models.card_association import card_association
from models.card_set import CardSet


class SQLiteEngine:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///ygo-custom.db")

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return sessionmaker(self.engine)()
