from src.database import connect_database

connection = connect_database()

if connection:
    connection.close()
    print("Connection test completed.")