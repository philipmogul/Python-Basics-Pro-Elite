import sqlite3
db = sqlite3.connect("./databases/db_file.db")
db.row_factory = sqlite3.Row

def main():
    print(f"DB CLASS FOR CRUB METHODS IN PYTHON!")
    db_classobj.create(db)
    db_classobj.insert(db)
    db_classobj.showtable(db)
    db_classobj.update(db)
    db_classobj.showtable(db)
    db_classobj.delete(db)
    db_classobj.showtable(db)

class db_class():
    def __init__(self):
        print(f"CLASS FOR DB CRUB METHODS IN PYTHON:")

    def create(self, db):
        print(f"CREATED TABLE")
        # I will create a table here 
        create = """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )"""
        db.execute(create)
        db.commit()

    def insert(self, db):
        print(f"INSERTED INTO TABLE")
        insert = """INSERT INTO users(name, email) VALUES(?, ?)"""
        db.execute(insert, ('John Doe', 'john@example.com'))
        db.execute(insert, ('Jane Doe', 'jane@example.com'))
        db.execute(insert, ('Jim Doe', 'jim@example.com'))
        db.execute(insert, ('Jack Doe', 'jack@example.com'))
        db.commit()

    def showtable(self, db):
        print(f"SHOWING TABLE")
        show = """SELECT * FROM users"""
        data = db.execute(show)
        for row in data:
            print(row['id'], row['name'], row['email'])

    def update(self, db):
        print(f"UPDATED TABLE")
        update = """UPDATE users SET name = ? WHERE id = ?"""
        db.execute(update, ('New Name', 1))
        db.commit()

    def delete(self, db):
        print(f"DELETED FROM TABLE")
        delete = """DELETE FROM users WHERE id = ?"""
        db.execute(delete, (1,))
        db.commit()


db_classobj = db_class()
if __name__ == "__main__": main()

