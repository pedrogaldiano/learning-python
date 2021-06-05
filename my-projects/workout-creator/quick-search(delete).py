import sqlite3

connect = sqlite3.connect('exercises-data.db')
db = connect.cursor()

db.execute("SELECT * FROM muscles WHERE muscle_name = '' ")

items = db.fetchall()



for item in items:
    print(item)

print(len(items))
db.close()