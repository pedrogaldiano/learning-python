# Create one singe table to store all the information
import sqlite3

conn = sqlite3.connect('table-all.db')

c = conn.cursor()

c.execute('CREATE TABLE exercises(name TEXT, utility TEXT, mechanic TEXT, force TEXT, target TEXT, synergist TEXT)')
print('Table exercises created')
conn.commit()
conn.close()