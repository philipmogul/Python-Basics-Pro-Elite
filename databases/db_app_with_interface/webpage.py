import sqlite3
import sys, os 

def main():
    print(f"WEBPAGE IN PYTHON")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python version: {sys.version}")

    create_webpage()


def create_webpage():
    # LOAD DB VALUES I WILL WORK WITH
    db = sqlite3.connect("./databases/db_app_with_interface/dbinterface.db")
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    #Make html_content with the tables and their values

    html_content = "<html><head><title>Database Tables</title></head><body>"
    html_content += "<h1>Database Tables</h1>"
    for table in tables:
        table_name = table[0]
        html_content += f"<h2>Table: {table_name}</h2>"
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        html_content += "<table border='1'><tr>"
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for column in columns:
            html_content += f"<th>{column[1]}</th>"
        html_content += "</tr>"
        for row in rows:
            html_content += "<tr>"
            for cell in row:
                html_content += f"<td>{cell}</td>"
            html_content += "</tr>"
    html_content += "</table></body></html>"


    with open("webpage.html", "w") as file:
        file.write(html_content)
    print("Webpage created successfully.")





if __name__ == "__main__":
    main()