import mysql.connector

# Establish a connection to the MySQL database
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}
conn = mysql.connector.connect(**config)


def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


while True:
    query = input('MySQL Shell> ')

    if query.lower() == 'exit':
        break

    result = execute_query(query)
    for row in result:
        print(row)

conn.close()
