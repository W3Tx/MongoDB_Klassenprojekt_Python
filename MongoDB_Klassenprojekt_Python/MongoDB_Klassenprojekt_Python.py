from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = None

# Hauptprogrammcode
def main(): 
    # Schreib hier weiter 
    print("Verbingung zu MongoDB")
    list_databases()
    select_or_create_database()


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


# Startpunkt
if __name__ == "__main__":
    main()
