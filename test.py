from db.database import Database
from src.pembayaranAdmin import *
from src.kamar import *
from src.login import *
db = Database()
db.open()
print(view_password(db))
db.close()