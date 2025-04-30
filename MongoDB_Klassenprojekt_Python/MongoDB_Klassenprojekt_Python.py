from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = None
collection = None

# Hauptprogrammcode
def main(): 
    # Schreib hier weiter 
    print("Verbingung zu MongoDB")
    list_databases()
    select_or_create_database()
    list_collection()
    select_or_create_collection()
    insert_document()
    display_documents()


def list_databases():
    databases = client.list_database_names()
    print("\nVerfügbare Datenbanken")

    for db in databases: 
        print(f"- {db}")


def select_or_create_database():
    global database
    db_name = input("\nGeben Sie den Namen der Datenbank ein: ").strip()
    database = client[db_name] 
    print(f"Datenbank '{db_name}' ausgewählt (oder wird bei Bedarf erstellt)")

def list_collection():
    if database is None: 
        print("Bitte zuerst eine Datenbank auswähler")
        return
    
    collections = database.list_collection_names()
    print("\nVerfügbare Collections: ")
    for col in collections:
        print(f"- {col}")

def select_or_create_collection():
    global collection
    if database is None:
        print("Bitte zuerst eine Datenbank auswählen")
        return
    
    col_name = input("\nGeben Sie den Namen der Collection ein: ").strip()
    collection = database[col_name]
    print(f"Collection '{col_name}' ausgewählt (oder bei Bedarf erstellt)")

def insert_document():
    if collection is None:
        print("Bitte zuerst eine Collection auswählen")
        return
    
    name = input("\nGeben Sie den Namen ein: ").strip()
    alter_input = input("Geben Sie das Alter ein: ").strip()

    try: 
        alter = int(alter_input)
    except ValueError:
        alter = 0

    document = {"Name": name, "Alter": alter}
    collection.insert_one(document)
    print("Dokument wurde erfolgreich eingefügt")

def  display_documents():
    if collection is None:
        print("Bitte zuerst eine Collection auswählen")
        return
    
    document = collection.find()
    print("\nAlle Dokumente:")
    for doc in document: 
        print(doc)

# Startpunkt
if __name__ == "__main__":
    main()
