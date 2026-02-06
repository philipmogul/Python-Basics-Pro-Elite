import sqlite3

def main():
    print(f"DATABASES IN PYTHON!")
    print(f"We will use SQLite3, since it comes with Python.")
    db = sqlite3.connect("./databases/db_file.db") #Will create this db file 
    db.row_factory = sqlite3.Row # Will help in targeting all or specific column names
    db.execute("drop table if exists test_db")
    db.execute("create table test_db (user_id int, bio text)")
    db.execute("insert into test_db(user_id, bio) values(?, ?)", (1, 'Phil'))
    db.execute("insert into test_db(user_id, bio) values(?, ?)", (2, 'Value'))
    db.execute("insert into test_db(user_id, bio) values(?, ?)", (3, 'Nonchalant'))
    db.execute("insert into test_db(user_id, bio) values(?, ?)", (4, 'Max'))
    db.execute("insert into test_db(user_id, bio) values(?, ?)", (5, 'Cool'))
    db.commit()
    db_data = db.execute("select * from test_db order by user_id")
    for rows in db_data:
        print(rows['user_id'], rows['bio'])

    


if __name__ == "__main__": main()