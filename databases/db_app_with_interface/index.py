import sqlite3

def main():
    print(f"DB APP WITH INTERFACE")
    print(f"---------------------")
    print(f"Creating database interface and performing operations...")
    print(f"An interface class is defined to manage database connections and operations, providing a clean and reusable way to interact with the database.")
    db = dbInterface("./databases/db_app_with_interface/dbinterface.db")
    with db:
        db.create_table("users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "age": "INTEGER"})
        db.insert_data("users", {"id": 1, "name": "Alice", "age": 30})
        db.insert_data("users", {"id": 2, "name": "Bob", "age": 25})
        print(db.fetch_data("SELECT * FROM users"))

        db.update_data("users", {"name": "Alice Smith", "age": 31}, "id = 1")
        print(db.fetch_data("SELECT * FROM users WHERE id = 1"))

        db.delete_data("users", "id = 2")
        print(db.fetch_data("SELECT * FROM users"))
    
class dbInterface:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
    
    def close(self):
        if self.conn:
            self.conn.close()
    
    def execute_query(self, query):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def execute_non_query(self, query):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def create_table(self, table_name, columns):
        columns_str = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.execute_non_query(query)

    def insert_data(self, table_name, data):
        columns_str = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
        self.execute_non_query(query, tuple(data.values()))

    def execute_non_query(self, query, params=None):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query, params=None):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __str__(self):
        return f"dbInterface connected to {self.db_name}"
    
    def __repr__(self):
        return f"dbInterface(db_name='{self.db_name}')"
    
    def __del__(self):
        self.close()

    def __call__(self, query, params=None):
        return self.fetch_data(query, params)
    
    def __iter__(self):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = cursor.fetchall()
        self.table_index = 0
        return self
    
    def __next__(self):
        if self.table_index < len(self.tables):
            table_name = self.tables[self.table_index][0]
            self.table_index += 1
            return table_name
        else:
            raise StopIteration
        
    def __len__(self):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        return cursor.fetchone()[0]
    
    def __contains__(self, table_name):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cursor.fetchone() is not None
    
    def __getitem__(self, table_name):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    
    def __setitem__(self, table_name, data):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        for row in data:
            placeholders = ", ".join(["?" for _ in row])
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, tuple(row))
        self.conn.commit()


    def __delitem__(self, table_name):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()

    def update_data(self, table_name, data, where_clause):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def delete_data(self, table_name, where_clause):
        if not self.conn:
            raise Exception("Database not connected")
        cursor = self.conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {where_clause}"
        cursor.execute(query)
        self.conn.commit()
        

if __name__=="__main__": main()