def create_alamat(db, jalan, kota, kode_pos, provinsi):
    query = "INSERT INTO alamat (jalan, kota, kode_pos, provinsi) VALUES (%s, %s, %s, %s) RETURNING id_alamat"
    db.execute(query, (jalan, kota, kode_pos, provinsi))
    return db.fetch_one()[0]

def create_universitas(db, nama_universitas):
    query = "INSERT INTO universitas (nama_universitas) VALUES (%s) RETURNING id_universitas"
    db.execute(query, (nama_universitas,))
    return db.fetch_one()[0]

def create_fakultas(db, nama_fakultas):
    query = "INSERT INTO fakultas (nama_fakultas) VALUES (%s) RETURNING id_fakultas"
    db.execute(query, (nama_fakultas,))
    return db.fetch_one()[0]

def create_role(db, nama_role):
    query = "INSERT INTO role (nama_role) VALUES (%s) RETURNING id_role"
    db.execute(query, (nama_role,))
    return db.fetch_one()[0]

def check_universitas_exists(self, nama_universitas):
        query = "SELECT id_universitas FROM universitas WHERE lower(nama_universitas) = lower(%s)"
        self.execute(query, (nama_universitas,))
        return self.fetch_one()

def check_fakultas_exists(self, nama_fakultas):
        query = "SELECT id_fakultas FROM fakultas WHERE lower(nama_fakultas) = (%s)"
        self.execute(query, (nama_fakultas,))
        return self.fetch_one()

def check_role_exists(self, nama_role):
        query = "SELECT id_role FROM role WHERE lower(nama_role) = lower(%s)"
        self.execute(query, (nama_role,))
        return self.fetch_one()

def create_or_get_universitas(db, nama_universitas):
    existing = db.check_universitas_exists(nama_universitas)
    if existing:
        return existing[0]
    return create_universitas(db, nama_universitas)

def create_or_get_fakultas(db, nama_fakultas):
    existing = db.check_fakultas_exists(nama_fakultas)
    if existing:
        return existing[0]
    return create_fakultas(db, nama_fakultas)

def create_or_get_role(db, nama_role):
    existing = db.check_role_exists(nama_role)
    if existing:
        return existing[0]
    return create_role(db, nama_role)

def create_user(db, id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar):
    query = """
    INSERT INTO users (id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_user
    """
    db.execute(query, (id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar))
    return db.fetch_one()

def create_user(db, id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar):
    query = """
    INSERT INTO users (id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_user
    """
    db.execute(query, (id_user, nama_user, no_telepon, id_alamat, durasi_huni, id_universitas, id_fakultas, id_role, no_kamar))
    return db.fetch_one()

    
def register_user(db):
    user_details = {
        'id_user': 1234567890123456,
        'nama_user': 'John Doe',
        'no_telepon': '081234567890',
        'jalan': 'Jalan Merdeka',
        'kota': 'Jakarta',
        'kode_pos': 10110,
        'provinsi': 'DKI Jakarta',
        'durasi_huni': '2024-12-31',
        'nama_universitas': 'Universitas Indonesia',
        'nama_fakultas': 'Fakultas Teknik',
        'nama_role': 'penghuni',
        'no_kamar': 101
    }
    
    
    
    try:
        # Begin transaction
        db.connection.autocommit = False

        # Create alamat
        id_alamat = db.create_alamat(user_details['jalan'], user_details['kota'], user_details['kode_pos'], user_details['provinsi'])
        
        # Create universitas
        id_universitas = db.create_universitas(user_details['nama_universitas'])
        
        # Create fakultas
        id_fakultas = db.create_fakultas(user_details['nama_fakultas'])
        
        # Create role
        id_role = db.create_role(user_details['nama_role'])
        # Create user
        id_user = db.create_user(user_details['id_user'], user_details['nama_user'], user_details['no_telepon'], id_alamat, 
                                 user_details['durasi_huni'], id_universitas, id_fakultas, id_role, user_details['no_kamar'])
        # Commit transaction
        db.connection.commit()
        return id_user

    except Exception as e:
        # Rollback transaction on error
        db.connection.rollback()
        db.close()
        print("Registration failed:", e)
        return None
    
    