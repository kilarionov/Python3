import sqlite3
#           install_persons_db.py
DB_NAME = 'persons.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

c.execute('''CREATE TABLE contacts (
                names text,
                city text,
                phone text)''') # ??? phones
conn.commit()

print(f'SUCCESS => {DB_NAME}')
print('\tcontacts')
print('\t\tnames, city, phone')


