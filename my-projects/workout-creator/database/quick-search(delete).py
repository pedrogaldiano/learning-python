import sqlite3

connect = sqlite3.connect('exercises-data.db')
db = connect.cursor()

# db.execute('''DELETE FROM muscles WHERE muscle_id = 2''')

# db.execute("SELECT * FROM muscles")

items = db.fetchall()



for item in items:
    print(item)

connect.commit()
connect.close()

