import sqlite3
import csv
import sys
# . -> current folder
# ../ -> one folder back

DB_NAME = '../db.sqlite3'

def migrate_data():
    # Create table on sqlite database
    """
    result = create_table()
    if result:
        print("Create table successfully")
    else:
        print("Error to create table")
    """

    # Read records from csv file
    csv_file = open("./countries.csv")
    csv_reader = csv.reader(csv_file)
    header_row = next(csv_reader)# return header row (first row)
    print(header_row)
    cid = 1;
    for row in csv_reader:
        record = (cid, row[0].strip(), row[1].strip(), int(row[2]), int(row[3]))
        # print(record) # insert into database table
        print(insert_record(record))
        cid+=1

    # Insert records on table of sqlite database


# Create table on sqlite database

def create_table():
    result = False
    sql = """
        CREATE TABLE IF NOT EXISTS countries(
            cid integer PRIMARY KEY,
            country Text,
            region Text,
            population integer,
            area int
        )
    """
    conn = None
    currsor = None
    try:
        conn = sqlite3.connect(DB_NAME)
        currsor = conn.cursor()
        currsor.execute(sql)
        currsor.close()
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        del currsor
        del conn
        del sql
    return result

def insert_record(record):
    result = False
    sql = """INSERT INTO app2_1_country values(?, ?, ?, ?, ?)"""
    conn = None
    currsor = None
    try:
        conn = sqlite3.connect(DB_NAME)
        currsor = conn.cursor()
        currsor.execute(sql, record)
        conn.commit() # Record save
        currsor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info()[1])
    finally:
        del currsor
        del conn
        del sql
    return result

migrate_data()