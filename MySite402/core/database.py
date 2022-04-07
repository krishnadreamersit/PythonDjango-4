# Database Management System

# Steps
    # Choose Database Application (sqlite, mysql, oracle, etc) - sqlite
    # Create table (DDL)
    # Insert Record
        # Connect
        # Insert

import sqlite3
import sys

DB_NAME = "./mydb.db"

def create_table():
    sql = """
        CREATE TABLE emails(
            email text
        )
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()
        print("Create table successfully")
    except:
        print("Error: ", sys.exc_info()[1])

def insert_record(email):
    sql = "INSERT INTO emails VALUES(?)"
    values = (email, )
    result = False
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()# insert, update, delete
        cursor.close()
        conn.close()
        print("Insert record successfully")
        result = True
    except:
        print("Error: ", sys.exc_info()[1])
        result = False
    return result

def select_all():
    sql = "SELECT * FROM emails"
    emails = []
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        for record in records:
            #emails.append(record)
            print(record) # ('krishna@gmail.com',)
            emails.append(record[0])
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info()[1])
    return emails

# Test
# create_table()
# insert_record('krishna@gmail.com')
# insert_record('john@gmail.com')
# select_all()