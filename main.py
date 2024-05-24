from db.database import Database
from src.login import login
db = Database()
db.open()


try:
    nama_user,role = login(db)
except:
    nama_user,role = None,None
    
if role == :
    print("Halo penghuni")
else:
    print("Halo Admin")
    

db.close()
