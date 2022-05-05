import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database 
    If you pass the file name as :memory: to the connect() function of the sqlite3 module, it will create a new database that resides in the memory (RAM) instead of a database file on disk.
    eg conn = sqlite3.connect(':memory:')"""
    conn = None
    try:
        path = "./db/" + db_file + ".db"
        conn = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"Blog")
