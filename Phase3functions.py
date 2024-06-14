from connect import create_connection

def print_users(): #printing function

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def print_payment_methods(): #printing function

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PaymentMethod")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def create_user(name, email, password): #creates a new user

    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO User (name, email, password) VALUES (%s, %s, %s)"
    print(f"Executing query: {query} with values ({name}, {email}, {password})")
    cursor.execute(query, (name, email, password))
    connection.commit()
    print("User created successfully")
    cursor.close()
    connection.close()

def read_users(): #reads all users just like the printing function

    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM User"
    print(f"Executing query: {query}")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def update_user(uid, name=None, email=None, password=None): #updates the wanted user

    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE User SET "
    params = []
    if name:
        query += "name = %s, "
        params.append(name)
    if email:
        query += "email = %s, "
        params.append(email)
    if password:
        query += "password = %s, "
        params.append(password)
    query = query.rstrip(', ')
    query += " WHERE uid = %s"
    params.append(uid)
    print(f"Executing query: {query} with values {tuple(params)}")
    cursor.execute(query, tuple(params))
    connection.commit()
    print("User updated successfully")
    cursor.close()
    connection.close()

def delete_user(uid): #deletes the wanted user

    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM User WHERE uid = %s"
    print(f"Executing query: {query} with value ({uid},)")
    cursor.execute(query, (uid,))
    connection.commit()
    print("User deleted successfully")
    cursor.close()
    connection.close()

def create_payment_method(type, uid): #creates a new payment method for a user

    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO PaymentMethod (type, uid) VALUES (%s, %s)"
    print(f"Executing query: {query} with values ({type}, {uid})")
    cursor.execute(query, (type, uid))
    connection.commit()
    print("Payment method created successfully")
    cursor.close()
    connection.close()

def read_payment_methods(): #just like the print function

    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM PaymentMethod"
    print(f"Executing query: {query}")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()

def update_payment_method(pid, type=None, uid=None): #updates the wanted payment method

    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE PaymentMethod SET "
    params = []
    if type:
        query += "type = %s, "
        params.append(type)
    if uid:
        query += "uid = %s, "
        params.append(uid)
    query = query.rstrip(', ')
    query += " WHERE pid = %s"
    params.append(pid)
    print(f"Executing query: {query} with values {tuple(params)}")
    cursor.execute(query, tuple(params))
    connection.commit()
    print("Payment method updated successfully")
    cursor.close()
    connection.close()

def delete_payment_method(pid): #deletes the wanted payment method

    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM PaymentMethod WHERE pid = %s"
    print(f"Executing query: {query} with value ({pid},)")
    cursor.execute(query, (pid,))
    connection.commit()
    print("Payment method deleted successfully")
    cursor.close()
    connection.close()
