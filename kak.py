import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        BD = sqlite3.connect('leadeers.db')
        return BD
    except Error:
        print(Error)

def sql_table(BD):
    cursed = BD.cursor()
    cursed.execute("CREATE TABLE records(id Integer PRIMARY KEY, name text, rec integer)")
    BD.commit()

BD = sql_connection()
# sql_table(BD)

def sql_insert_leader(BD, entities):
    cursed = BD.cursor()
    cursed.execute('INSERT INTO records(id, name, rec) VALUES(?, ?, ?)', entities)
    BD.commit()
name='Zeta'
entities = (1, name, 10000000000000000)
#sql_insert_leader(con, entities)

def row_len(BD):
    cursed = BD.cursor()
    cursed.execute('SELECT * FROM records ORDER BY rec DESC')
    rows = cursed.fetchall()
    #print(len(rows))

def sql_fetch(BD):
    cursed = BD.cursor()
    cursed.execute('SELECT name, rec FROM records ORDER BY rec DESC LIMIT 3')
    rows = cursed.fetchall()
    #for row in rows:
        #print(row)