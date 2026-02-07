import sqlite3
db = sqlite3.connect("./databases/db_file.db")
db.row_factory = sqlite3.Row

class db_class():
    def __init__(self):
        print(f"CLASS FOR DB CRUB METHODS IN PYTHON:")

    def create(self, db):
        print(f"CREATED TABLE")


    def update(self, db):
        print(f"UPDATED TABLE")

    def delete(self, db):
        print(f"DELETED FROM TABLE")

db_classobj = db_class()

