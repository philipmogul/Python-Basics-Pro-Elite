import sqlite3

def insert(db, db_data):
    db.execute("insert into test_db(user_id, bio) values(? , ?)", (db_data['user_id'], db_data['bio']))
    db.commit()

def retrieve(db, user_id):
    cursor = db.execute("select * from test_db where user_id = ?", (user_id,))
    return cursor.fetchone()

def update(db, db_data):
    db.execute("update test_db set user_id = ? where bio = ?", db_data['user_id'], db_data['bio'])
    db.commit()

def display_rows(db):
    db_data = db.execute("select * from test_db order by user_id")
    for row in db_data:
        print('{}: {}'.format(row['user_id'], row['bio']))


def main():
    print(f"CRUD FUNCTIONS IN PYTHON DB")
    db = sqlite3.connect("./databases/db_file.db")
    db.row_factory = sqlite3.Row
    print(f"DISPLAYING ROWS:")
    display_rows(db)
    print(f"RETRIEVE ROW WHERE user_id = 3")
    print(retrieve(db, 3))

if __name__ == "__main__": main()

