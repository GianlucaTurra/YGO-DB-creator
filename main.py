from engine import SQLiteEngine
from modules.fetch_cards import fetch_cards
from modules.fetch_sets import fetch_sets


def main() -> None:
    sql_engine = SQLiteEngine()
    sql_engine.create_tables()
    with (sql_engine.get_session()) as session:
        session.add_all(fetch_sets())
        session.add_all(fetch_cards(session))
        session.commit()


if __name__ == "__main__":
    main()
