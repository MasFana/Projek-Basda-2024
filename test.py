from db.database import Database
from src.pembayaranAdmin import *
from src.kamar import *
db = Database()
db.open
view_kamar_kosong(db)
db.close()