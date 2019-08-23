# INSERT command

import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City', \
                'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Franciso', \
                'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
