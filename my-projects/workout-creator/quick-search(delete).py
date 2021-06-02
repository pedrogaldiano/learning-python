import sqlite3

connect = sqlite3.connect('exercises-data.db')
db = connect.cursor()

db.execute("SELECT muscle_name FROM muscles")

items = db.fetchall()

for item in items:
    print(item[0])

print(len(items))
db.close()