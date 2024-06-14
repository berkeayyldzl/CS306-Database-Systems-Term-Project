import mysql.connector
from mysql.connector import errorcode

def create_connection():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="32893205002",
            database="CS306Project"
        )
        print("Connection established")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        connection.close()
