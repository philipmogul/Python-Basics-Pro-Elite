import sqlite3

def main():
    print(f"DB CRUD WITH PYTHON")
    db = sqlite3.connect("./databases/db_file.db")
    db.row_factory = sqlite3.Row
    db_data = db.execute("select * from test_db order by user_id desc")
    for row in db_data:
        print("{} , {}".format(row['user_id'], row['bio']))

if __name__=="__main__": main()
