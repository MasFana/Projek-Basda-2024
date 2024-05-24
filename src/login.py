from db.database import Database
db = Database()

def login(db):
    nama_user = input("Nama: ")
    password = input("Nim/ID Staff: ")
    query = "SELECT u.nama_user, r.nama_role from users u JOIN role r ON u.id_role = r.id_role WHERE LOWER(u.nama_user) = LOWER(%s) AND u.id_user = %s;"
    db.execute(query, (nama_user, int(password)))
    data = db.fetch_data()
    data = data[0] if data else False
    if data:
        print(f"Login berhasil ",data)
        return data
    else:
        print("Login gagal")
        return data
        
    