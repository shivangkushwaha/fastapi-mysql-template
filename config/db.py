import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file
class MySQLConnector:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")


    def connect(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        self.cursor = self.cnx.cursor(dictionary=True)

    def disconnect(self):
        self.cursor.close()
        self.cnx.close()

    def execute_query(self, query, data = None):
        """Execute an insert or select query."""
        self.connect()

        is_select_query = query.strip().lower().startswith("select")
        if data:
            self.cursor.execute(query, data)
            self.cnx.commit()
            result = self.cursor.rowcount if not is_select_query else None
        else:
            self.cursor.execute(query,data)
            if is_select_query:
                result = self.cursor.fetchall()
            else:
                result = self.cursor.rowcount
        self.disconnect()
        return result
    
mysql_connector = MySQLConnector()

