import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=66Oh!6My!6')
"""
Since the current user isn't an account on the PostgreSQL,
you'll have to insert the 'user' and 'password' on connect above. 
"""

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

"""
Below is how to populate a table using '%s' and passing in tuples,
these tuples are passed as the second paramater
This turns the string into a "Template"
"""
cursor.execute('INSERT INTO table2 (id, completed)' +
'VALUES (%s, %s);', (1, True))

"""
The second method is the method of Stream Composition,
where named string parameters '%(any)s' are used. 
Hence, a dictionary '{}' is used as the second parameter,
where the named variables are used.

NB: We are passing in SQL and data into the cursor.execute.
"""
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 2,
    'completed': False
}

cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 (id, completed)' +
'VALUES (%s, %s);', (3, True))

cursor.execute('SELECT * from table2;')

result = cursor.fetchmany(2)
print('fetchmany',result)

result2 = cursor.fetchone()
print('fetchone', result2)

result2 = cursor.fetchone()
print('fetchone', result2)


cursor.execute('SELECT * from table2;')

result2 = cursor.fetchone()
print('fetchone', result2)


connection.commit()

connection.close()
cursor.close()
