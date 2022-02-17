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

# ['Amulya Koirala', 'Kathmandu, Nepal', 1]
def update_record(record):
    # full record update based on pid
    # (1, 'Amulya', 'KTM')
    result = False
    sql = """
            UPDATE persons SET fname=?, caddress=? WHERE pid=?
        """
    try:
        conn = sqlite3.connect("mydb.db")
        cursor = conn.cursor()
        cursor.execute(sql,record)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        del sql
        return result

# Task-13.1
    # Partial record update - Home Work
        # Update fullname only based on pid
        # Update caddress only based on pid

def delete_record(pid):
    result = False
    sql = """
        DELETE FROM persons WHERE pid=?                
    """
    values = (pid, )
    try:
        conn = sqlite3.connect("mydb.db")
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        del sql
        del values
        return result

# Test
# print(connect_db("mydb.db"))
# print(create_table())

# Exploring mydb.db
# https://sqliteonline.com/

# print(insert_record([1, 'Amulya', 'KTM']))
# print(insert_record([2, 'John', 'BHK']))
# print(insert_record([3, 'XYZ', 'ABC']))

# print(select_all())
# print(search_record(100))

# Update Record
# print(select_all())
# (1, 'Amulya', 'KTM')
# record = ['Amulya Koirala', 'Kathmandu, Nepal', 1]
# print(update_record(record))

# Delete Record
# print(select_all())
# print(delete_record(3))
# print(select_all())

# Task-13.2
    # Implement CRUD using MySQL
        # Connect, Insert, Select, Update, Delete
    # Gather the info to connect with Oracel, MSSQL, PostgreSQL, MangoDB, etc

# Task-13.3
"""
---------- Main Menu ------------
1. Add New Record 
2. Display All
3. Search Record (based on id)
4. Search and Edit
5. Search and Delete
0. Exit
-----------------------------------
Enter your choice (0-> Exit) : _1
-----------------------------------
Enter New Student Info
ID : _1
NAME : Amulya Koirala
CLASS : BSIT
SECTION: A
OBTAIN MARKS:
SUB-1 : 67
SUB-2 : 76
SUB-3 : 98
--------------------------------------
TOTAL : ___
AVERAGE : ___
RESULT : ___
GRADE : ___
REMARKS: ___
---------- Main Menu ------------
1. Add New Record 
2. Display All
3. Search Record (based on id)
4. Search and Edit
5. Search and Delete
0. Exit
-----------------------------------
Enter your choice (0-> Exit) : _1
-----------------------------------
"""