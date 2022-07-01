import sqlite3



def show_all():
   """
   Query the database and return all records
   """
   #connect to database
   conn = sqlite3.connect('customer.db')

   #create cursor
   c = conn.cursor()

   #query the database
   c.execute("SELECT rowid, * FROM customers")
   items = c.fetchall()
   for item in items:
      print(item)

   #commit our command
   conn.commit()

   #close our connection 
   conn.close()

def add_record(first_name, last_name, email):
   """
   Add a record to the database
   """
   #connect to database
   conn = sqlite3.connect('customer.db')

   #create cursor
   c = conn.cursor()

   records_to_add = (first_name, last_name, email)

   #insert the record
   c.execute("INSERT INTO customers VALUES (?,?,?)", records_to_add)

   #commit our command
   conn.commit()

   #close our connection 
   conn.close()

def add_many(list):
   """
   Add more than one record to the database at once
   """
   #connect to database
   conn = sqlite3.connect('customer.db')

   #create cursor
   c = conn.cursor()

   #insert the records
   c.executemany("INSERT INTO customers VALUES (?,?,?)", list)

   #commit our command
   conn.commit()

   #close our connection
   conn.close()

def delete_one(id):
   """
   Delete a record from the database
   """
   #connect to database
   conn = sqlite3.connect('customer.db')

   #create cursor
   c = conn.cursor()

   #delete the record
   c.execute("DELETE from customers WHERE rowid = (?)", id)

   #commit our command
   conn.commit()

   #close our connection
   conn.close()


#lookup with where
def email_lookup(email):
   """
   lookup a record from the database using where
   """
   #connect to database
   conn = sqlite3.connect('customer.db')

   #create cursor
   c = conn.cursor()

   #delete the record
   c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))

   #fetch 
   items = c.fetchall()

   for item in items:
      print(item)

   #close our connection
   conn.close()