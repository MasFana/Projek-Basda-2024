from db.database import Database

class Barang:
    def __init__(self):
        self.db = Database()

    def get_barang(self):
        return self.db.get_barang()
    
    def get_barang_by_id(self, id):
        return self.db.get_barang_by_id(id)
    
    def add_barang(self, data):
        return self.db.add_barang(data)
    
    def update_barang(self, id, data):
        return self.db.update_barang(id, data)
    
    def delete_barang(self, id):
        return self.db.delete_barang(id)
    
    def get_barang_by_user(self, id):
        return self.db.get_barang_by_user(id)
    