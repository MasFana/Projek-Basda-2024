from db.database import Database
from src.login import login, view_password
db = Database()
db.open()


# view_password(db)
login(db)
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
    

db.close()
