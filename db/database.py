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
                # sslmode='require'
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT version();")
            self.connection.commit()
            version = self.cursor.fetchone()
            print("Koneksi database berhasil.",version)
        except (Exception, psycopg2.Error) as error:
            print("Koneksi database gagal:", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Terputus dari database.")

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query berhasil!")
        except (Exception, psycopg2.Error) as error:
            print("Query gagal:", error)

    def fetch_data(self):
        rows = self.cursor.fetchall()
        return rows            
