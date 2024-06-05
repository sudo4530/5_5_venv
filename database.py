import os
import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query: str, query_type: str) -> list or str:
        db = psql.connect(
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )

        cursor = db.cursor()
        # query = "SELECT * FROM user"
        data = ["insert", "delete", "update", "alter"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted data"

        else:
            return cursor.fetchall()
