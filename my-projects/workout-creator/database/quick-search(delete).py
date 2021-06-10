import sqlite3

connect = sqlite3.connect('exercises-data.db')
db = connect.cursor()
# 
# db.execute('''SELECT * FROM muscles''')

db.execute("SELECT count(exercise), muscle_id FROM exercises GROUP BY muscle_id  ORDER BY count(exercise) ASC")

items = db.fetchall()



for item in items:
    print(item)

# connect.commit()
connect.close()


# (3, aerobic)
# (8, abductors)
# (8, neck)