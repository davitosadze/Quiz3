import requests
import sqlite3
import json
from sqlite3 import Error


response = requests.get("https://jsonplaceholder.typicode.com/posts")

def attributes():
    print(response.status_code) #STATUS OF RESPONSE E.G. (200OK, 404NOT FOUND, 405 METHOD NOT ALLOWED
    print(response.headers) #RETURNS RESPONSE HEADERS
    print(response.headers['Content-Type']) #RETURN EXACT RESPONSE HEADER

def savetoJson():
    text = response.text
    toJson = json.loads(text)   #CONVERT TO JSON

    with open('test.json', 'w') as f:
        json.dump(toJson, f, indent=4) #SAVE TO JSON


def chemtvisSaintereso():
    text =  response.text
    toJson = json.loads(text)
    for t in toJson:
        print(t["id"], t["title"]) #RETURN ALL ITEM IDs and TITLES


def createDatabase(db):
    try:
        conn = sqlite3.connect(db) #CONNECTION OR CREATION OF DATABASE
        cursor = conn.cursor()

        sql = '''CREATE TABLE TestTable( 
           id INT PRIMARY KEY,
           jsonTitle VARCHAR(255),
           jsonId INT
        )''' #CREATE NEW TABLE FOR TEST DATA
        cursor.execute(sql)
        insertData(db) #INSERT TEST DATA TO DB
    except Error as e:
        print(e)

def insertData(db): #FUNCTION FOR INSERTING DATA TO DATABASE INSERT ONLY TITLE AND ID FROM API
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    text = response.text
    toJson = json.loads(text)
    for t in toJson:
        object = (t["title"], t["id"])
        cursor.execute('INSERT INTO TestTable (jsonTitle,jsonId) VALUES (?,?)', object)
        conn.commit()

#SIMPLY CALL FUNCTIONS

# attributes()
# savetoJson()
# chemtvisSaintereso()
# createDatabase() #CREATE DATABASE FUNCTION AUTOMATICALLY INSERT DATA TO TABLES
