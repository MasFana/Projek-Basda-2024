import psycopg2
from .config import config
import os

# ssl._create_default_https_context = ssl._create_unverified_context
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_dir, "database.ini")
config = config(config_file)

class Database:
    def __init__(self, host=None, database=None, user=None, password=None, port=None):
        self.database = database if database else config['database']
        self.user = user if user else config['user']
        self.password = password if password else config['password']
        self.host = host if host else config['host']
        self.port = port if port else config['port']
        self.ssl = "require"
        self.connection = None
        self.cursor = None

    def open(self):
        try:
            self.connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                sslmode='require'
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT version();")
            self.connection.commit()
            return True
            # version = self.cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            return False

    def check_connection(self):
        try:
            # Try to execute a simple command to check if the connection is active
            self.connection.cursor().execute('SELECT 1')
        except Exception as e:
            # If an exception is raised, the connection is not active. Reopen it.
            self.open()

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Terputus dari database.")

    def execute(self, query,params=None):
        try:
            if params != None:
                self.cursor.execute(query,params)
                self.connection.commit()
            else:
                self.cursor.execute(query)
                self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Query gagal:", error)

    def fetch_data(self):
        try:
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.Error) as error:
            print("Fetch data gagal:", error)
            return False
    
    def fetch_one(self):
        try:
            rows = self.cursor.fetchone()
            return rows
        except (Exception, psycopg2.Error) as error:
            return False


# db = Database()

# db.open()
# db.execute("SELECT * FROM users")
# rows = db.fetch_one()
# print(rows)
# db.close()