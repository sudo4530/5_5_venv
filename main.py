from database import Database

def project():
    service = input("""1. Users
            >>> """)
    if service == "1":
        query = "SELECT * FROM users"
        print(Database.connect(query, "select"))

if __name__ == "__main__":
    project()