from db.database import Database
from src.login import *
from src.mahasiswa import *
db = Database()
db.open()


# view_password(db)
# login(db)
def menu_admin():
    pass
def menu_penghuni():
    pass
def menu_pengunjung():
    pass
    
def menu_login():
    try:
        nama_user,role = login(db)
    except:
        nama_user,role = None,None

    if role == "penghuni" :
        print(f"Halo {nama_user}")
    else:
        print(f"Halo Admin {nama_user}")
    
    
print(db.execute("SELECT * FROM fakultas"))
print(db.fetch_data())

print(check_fakultas_exists(db, "Fakultas Teknik"))
# print(create_fakultas(db, "Fakultas Teknik"))
db.close()
