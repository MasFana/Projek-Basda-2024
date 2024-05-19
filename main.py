from db.database import Database

db = Database()

db.connect()
db.execute("SELECT * FROM public.mata_kuliah")
db.fetch_data()