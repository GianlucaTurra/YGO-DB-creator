# DB Generation script
A simple python script to read data from an API (YGO-pro) and save it to a SQLite file.  

### DB creation
The database entities are managed using SQLAlchemy's ORM, binding the two (Card and CardSet) with a many-to-many bidirectional relationship.
