# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use for loop to iterate through database
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)

print()
# OR

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    # fetchall() retrieves all records from query (returns a tuple)
    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
