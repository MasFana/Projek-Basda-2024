from db.database import Database
from src.pembayaranAdmin import *
from src.kamar import *
from src.login import *
from src.users import check_universitas_exists
from src.pembayaranAdmin import *
from src.aspirasi import *
from src.barang import *
db = Database()
db.open()

create_jenis_barang(db)
db.close()