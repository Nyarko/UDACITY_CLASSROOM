import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=66Oh!6My!6')
"""
Since the current user isn't an account on the PostgreSQL,
you'll have to insert the 'user' and 'password' on connect above. 
"""

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

connection.commit()

connection.close()
cursor.close()
