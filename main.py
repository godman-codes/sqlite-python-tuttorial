# import sqlite3

# #connect to database
# conn = sqlite3.connect('customer.db')

# #create cursor
# c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE customers (
#       first_name text,
#       last_name text,
#       email text
#    )""")

#insert data into table
# c.execute("""INSERT INTO customers VALUES (
#    'Mary',
#    'Brown',
#    'Mary@codemy.com'
# )
#          """)

# # Insert a lot of data into the data base
# many_customer = [
#    ('Wes', 'Brown', 'Wes@brown.com'),
#    ('Steph', 'Kuewa', 'Steph@kuewa.com'),
#    ('Dan', 'Pas', 'dan@pas.com')
#    ]

# c.executemany("""INSERT INTO customers VALUES (?,?,?)
#             """, many_customer)

# #query select from database
# # c.execute("SELECT rowid, * FROM customers")
# #select where
# # c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
# #select where like
# # c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
# # print(c.fetchone())
# # print(c.fetchmany(3))

# #update Records
# # c.execute("""UPDATE customers SET first_name = 'Bob'
# #          Where last_name = 'Elder'
# #          """)

# #update Records with specific id
# # c.execute("""UPDATE customers SET first_name = 'Margret'
# #          Where rowid = 3
# #          """)

# #deleting a record
# # c.execute("DELETE from customers WHERE rowid = 6")

# #ordering records
# # c.execute("SELECT rowid, * FROM customers ORDER BY first_name")

# # query the database and/or
# # c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'br%' OR rowid = 3")

# #limit the results of a query
# # c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")

# #DROP TABLE
# c.execute("DROP TABLE customers")
# conn.commit()


# # conn.commit()
# c.execute("SELECT rowid, * FROM customers")

# items = c.fetchall()

# for item in items:
#    print(item) 

# print('command executed successfully')

# #Datatypes:
# # NULL
# #INTEGER
# #REAL
# #TEXT
# #BLOB

#commit our command 
# conn.commit()


# #Close our connection
# conn.close()



