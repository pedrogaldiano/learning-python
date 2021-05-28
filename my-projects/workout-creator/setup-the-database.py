# Populate the exercises table in the relational database
# Use the inner join to print out all the database
# Check if it woked properly
import sqlite3

cnn = sqlite3.connect('table-all.db')
c = cnn.cursor()
c.execute("SELECT * FROM exercises GROUP BY name")
items = c.fetchall()


cnn2 = sqlite3.connect('exercises-relational-database.db')
c2 = cnn2.cursor()


for item in items:
    
    name = item[0]
    # print(name)
    c2.execute("SELECT id FROM utilities WHERE utility = ?", [item[1]])
    util = c2.fetchone()
    # print(util)
    c2.execute("SELECT id FROM mechanics WHERE mechanic = ?", [item[2]])
    mech = c2.fetchone()
    c2.execute("SELECT id FROM forces WHERE force = ?", [item[3]])
    forc = c2.fetchone()
    c2.execute("SELECT id FROM targets WHERE target = ?", [item[4]])
    targ = c2.fetchone()
    c2.execute("SELECT id FROM synergists WHERE synergist = ?", [item[5]])
    syne = c2.fetchone()

    insertion = ('''
    INSERT INTO exercises
    (exercise_name, utility_id, mechanic_id, force_id, target_id, synergist_id)
    VALUES (?, ?, ?, ?, ?, ?)
    ''')
    
    c2.execute(insertion, (name, util[0], mech[0], forc[0], targ[0], syne[0]))
    
    
    
show_all_data = '''
SELECT
exercise_name, u.utility, m.mechanic, 
f.force, t.target, s.synergist

FROM exercises e

INNER JOIN utilities u
    ON e.utility_id = u.id
INNER JOIN mechanics m
    ON e.mechanic_id = m.id
INNER JOIN forces f
    ON e.force_id = f.id
INNER JOIN targets t 
    ON e.target_id = t.id
INNER JOIN synergists s
    ON e.synergist_id = s.id
'''

c2.execute(show_all_data)
items = c2.fetchall()
for item in items:
    print(item)
print(len(items))


cnn2.commit()
cnn2.close()
cnn.close()