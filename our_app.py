import database

#addd a record to the database
# database.add_record('Tobi', 'Faseun', 'Tobi@faseun.com')

#delete a record by using rowid as string
# database.delete_one('6')

# items = [('Kemi', 'Faseun', 'Kemi@faseun.com'),
#          ('Bolaji', 'Olawole', 'Bolaji@olawole.com'),
#          ('Godman', 'Abnormal', 'Godman@Abnormal.com')]

# database.add_many(items)

#query data base using where identifier will be email
database.email_lookup('Tobi@faseun.com')

#show all records in the database
# database.show_all()

