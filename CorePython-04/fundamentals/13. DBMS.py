# DBMS
    # Connect
    # Insert Record
    # Select Record
    # Update Record
    # Delete Record

# Connect
import sqlite3
import sys


def connect_db(db_name):
    result = False
    try:
        conn = sqlite3.connect(db_name)
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        return result


def create_table():
    result = False
    sql = """
        CREATE TABLE IF NOT EXISTS persons(
            pid integer,
            fname text,
            caddress text
        )
    """
    try:
        conn = sqlite3.connect("mydb.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        return result

def insert_record(record):
    result = False
    sql ="""
        INSERT INTO persons(pid, fname, caddress) values (?, ?, ?)
    """
    try:
        conn = sqlite3.connect("mydb.db")
        curosr = conn.cursor()
        curosr.execute(sql, record)
        conn.commit()
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        return result


def select_all():
    result = False
    sql = "SELECT * FROM persons"
    try:
        conn = sqlite3.connect("mydb.db")
        cursor = conn.cursor()
        records = cursor.execute(sql)
        for record in records:
            print(record)
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        return result


def search_record(pid):
    result = False
    sql = "SELECT * FROM persons WHERE pid=?"
    values = (pid, )
    try:
        conn = sqlite3.connect("mydb.db")
        cursor = conn.cursor()
        records = cursor.execute(sql, values)
        for record in records:
            print(record)
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        return result


# Test
# print(connect_db("mydb.db"))
# print(create_table())

# Exploring mydb.db
# https://sqliteonline.com/

# print(insert_record([1, 'Amulya', 'KTM']))
# print(insert_record([2, 'John', 'BHK']))

# print(select_all())
# print(search_record(100))





