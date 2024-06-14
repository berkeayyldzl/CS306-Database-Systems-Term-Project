from pymongo import MongoClient, errors
from bson.objectid import ObjectId

def connectDB():
    connection_string = "mongodb+srv://berkeayyildizli:berke@cs306project.nnk8ga5.mongodb.net/?retryWrites=true&w=majority&appName=CS306Project"
    try:
        client = MongoClient(connection_string)
        client.server_info()
        db = client.CS306Project
        print("Connection established to our database")
        return db
    except errors.ConnectionError:
        print("Failed to connect to the database")
        return None
    except errors.OperationFailure as e:
        print(f"Authentication failed: {e.details}")
        return None

def createCollection(db, collection_name):
    try:
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        else:
            print("Collection with this name already exists")
    except Exception as e:
        print("An error occurred: ", e)

def insert_into_collection(db, collection_name, data):

    try:
        collection = db[collection_name]
        result = collection.insert_one(data)
        print("Insertion completed successfully")
        print(f"Inserted document ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_all_data(db, collection_name):
    try:
        collection = db[collection_name]
        result = collection.find()
        for document in result:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

def read_some_data(db, collection_name, filter):
    try:
        collection = db[collection_name]
        result = collection.find(filter)
        for document in result:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_record_by_id(db, collection_name, record_id):
    try:
        collection = db[collection_name]
        query = {"_id": ObjectId(record_id)}
        result = collection.delete_one(query)
        if result.deleted_count == 1:
            print(f"Successfully deleted record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def update_record_by_id(db, collection_name, record_id, update_data):
    try:
        collection = db[collection_name]
        query = {"_id": ObjectId(record_id)}
        result = collection.update_one(query, {"$set": update_data})
        if result.matched_count == 1:
            print(f"Successfully updated record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def main():
    db = connectDB()
    print("Welcome to Book & Trip Feedback Portal! Your comments are important for us.")
    while True:
        print("\nPlease pick the option that you want to proceed.")
        print("1 - Create a collection.")
        print("2 - Read all data in a collection.")
        print("3 - Read some part of the data while filtering.")
        print("4 - Insert data.")
        print("5 - Delete data.")
        print("6 - Update data.")
        print("7 - Exit.")
        option = input("Selected option: ")

        if option == "1":
            collection_name = input("Enter the collection name: ")
            createCollection(db, collection_name)
        elif option == "2":
            collection_name = input("Enter the collection name: ")
            read_all_data(db, collection_name)
        elif option == "3":
            collection_name = input("Enter the collection name: ")
            filter_field = input("Enter the field to filter by: ")
            filter_value = input("Enter the value to filter: ")
            if filter_field == "given_star":
                filter_value = int(filter_value)
            filter = {filter_field: filter_value}
            read_some_data(db, collection_name, filter)
        elif option == "4":
            collection_name = input("Enter the collection name: ")
            name = input("Please enter your name: ")
            review_message = input("Enter your review: ")
            given_star = int(input("Enter your star rating (1-5): "))
            data = {
                "name": name,
                "review_message": review_message,
                "given_star": given_star
            }
            insert_into_collection(db, collection_name, data)
        elif option == "5":
            collection_name = input("Enter the collection name: ")
            record_id = input("Enter the record ID to delete: ")
            delete_record_by_id(db, collection_name, record_id)
        elif option == "6":
            collection_name = input("Enter the collection name: ")
            record_id = input("Enter the record ID to update: ")
            update_field = input("Enter the field to update: ")
            update_value = input("Enter the new value: ")
            update_data = {update_field: update_value}
            update_record_by_id(db, collection_name, record_id, update_data)
        elif option == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()