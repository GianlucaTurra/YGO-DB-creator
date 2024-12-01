from engine import SQLiteEngine


def main() -> None:
    sql_engine = SQLiteEngine()
    sql_engine.create_tables()


if __name__ == "__main__":
    main()
