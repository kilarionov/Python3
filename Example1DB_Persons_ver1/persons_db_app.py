#       persons_db_app.py
import sqlite3


def menu() :
    print('0. Exit')
    print('1. Name Search')
    print('2. City Search')
    print('3. Phone Search')
    print('4. Show All Contacts')
    print('5. Add New Contact')
    inp = input('Choose One?')
    if len(inp) == 0 :
        return 'Invalid Choice'
    else :
        return inp[0]


def exitMe() :
    conn.close()


def search_by_name() :
    names = input('To Search by\nNames ?')
    sql_cmd = f"SELECT names, city, phone FROM contacts WHERE names LIKE '%{names}%' ORDER BY names, city, phone"
    c.execute(sql_cmd)
    print(*c.fetchall())


def search_by_city() :
    city = input('To Search by\nCity ?')
    sql_cmd = f"SELECT city, names, phone FROM contacts WHERE city LIKE '%{city}%' ORDER by city, names, phone"
    c.execute(sql_cmd)
    print(*c.fetchall())


def search_by_phone() :
    phone = input('To Search by\nPhone Number ?')
    sql_cmd = f"SELECT phone, names, city FROM contacts WHERE phone LIKE '%{phone}%' ORDER by phone, names, city"
    c.execute(sql_cmd)
    print(*c.fetchall())


def show_all_contacts() :
    c.execute("SELECT names, city, phone FROM contacts ORDER BY names, city, phone")
    print(*c.fetchall())


def add_contact() :
    names = input('Names ?').title()
    city = input('City ?')
    phone = input('Phone ?')
    sql_cmd = f"INSERT INTO contacts VALUES ('{names}', '{city}', {phone}, CURRENT_TIMESTAMP)"
    c.execute(sql_cmd)
    conn.commit()


DB_NAME = 'persons.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

c.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
            names text NOT NULL,
            city text,
            phone text UNIQUE NOT NULL,
            dateTime text)
            ''')  # ??? phones

while True :
    choise = menu()
    if choise == '0' :
        exitMe()
        break
    elif choise == '1' :
        search_by_name()
    elif choise == '2' :
        search_by_city()
    elif choise == '3' :
        search_by_phone()
    elif choise == '4' :
        show_all_contacts()
    elif choise == '5' :
        add_contact()

print('YOU EXIT SUCCESSFULLY')
