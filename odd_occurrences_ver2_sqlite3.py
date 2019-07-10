# https://judge.softuni.bg/Contests/Practice/Index/945#0
#           odd_occurences_ver2_sqlite3.py

#           Odd Occurrences
# Write a program that extracts from a given sequence of words
# all elements that present in it odd number of times (case-insensitive).
# •	Words are given in a single line, space separated.
# •	Print the result elements in lowercase, in their order of appearance.

import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
inp = input().split()
c.execute('''CREATE TABLE names_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                dateTime text DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')))''')

for s in inp :
    sql_cmd = f'''INSERT INTO names_list (name) VALUES ('{s.lower()}')'''
#    print(sql_cmd)
    c.execute(sql_cmd)

conn.commit()
c.execute("SELECT DISTINCT name, COUNT(name), id FROM names_list GROUP BY name HAVING MIN(id) ORDER BY id")
res = c.fetchall()

str_lst = []
for s in res:
    if int(s[1]) % 2 != 0:
        str_lst.append(s[0])

print(', '.join(str_lst))
conn.close()