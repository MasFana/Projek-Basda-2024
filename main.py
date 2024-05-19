from sys import version
import psycopg2
from DB.config import config

config = config("DB/database.ini")
class Database:
    def __init__(self, host, database, user, password, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT version();")
            self.connection.commit()
            version = self.cursor.fetchone()
            print("Connected to the database.",version)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database.")

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def fetch_data(self):
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
            
db = Database(**config)
db.connect()
db.execute("SELECT * FROM public.mata_kuliah")
db.fetch_data()