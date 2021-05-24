import sqlite3

connection = sqlite3.connect('customer.db')
c = connection.cursor()

c.execute('''
          CREATE TABLE customers(
          first_name text,
          last_name text,
          email test)
          ''')
          
# c.execute('''
#           INSERT INTO customers
#           VALUES('Joah', 'PSer', 'jo@gmail.com')
#           ''')
          
# c.execute('''
#           INSERT INTO customers
#           VALUES('Sarah', 'Fisz', 'sarh@gmail.com')
#           ''')
         
# many_customers = [
#                   ('Zé', 'Silva', 'zes_silva@gmail.com'),
#                   ('Paulo', 'Freire', 'paulof@gmail.com'),
#                   ('Ricardo', 'Bacon', 'ricbac@gmail.com')
#                   ]

# c.executemany('''
#           INSERT INTO customers
#           VALUES (?,?,?)
#           ''', many_customers)

c.execute("SELECT * FROM customers")
clients = c.fetchall()

for client in clients:
    print(client)

connection.commit()
connection.close()