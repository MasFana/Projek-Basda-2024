from db.database import Database

class Aspirasi:
    def __init__(self):
        self.db = Database()

    def get_aspirasi(self):
        self.db.connect()
        self.db.execute("SELECT * FROM aspirasi")
        a = self.db.fetch_data()
        self.db.disconnect()
        return a
    
    def get_aspirasi_by_id(self, id):
        self.db.connect()
        self.db.execute(f"SELECT * FROM aspirasi WHERE id = {id}")
        a = self.db.fetch_data()
        self.db.disconnect()
        return a
    
    def add_aspirasi(self, data):
        self.db.connect()
        a = self.db.execute(f"INSERT INTO aspirasi (id_user, judul, deskripsi) VALUES ({data['id_user']}, '{data['judul']}', '{data['deskripsi']}')")
        self.db.disconnect()
        
        