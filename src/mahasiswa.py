
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

def create_alamat(db, jalan, kota, kode_pos, provinsi):
    query = "INSERT INTO alamat (jalan, kota, kode_pos, provinsi) VALUES (%s, %s, %s, %s) RETURNING id_alamat"
    db.execute(query, (jalan, kota, kode_pos, provinsi))
    return db.fetch_one()[0]

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
    try:        
        user_details = {
            'id_user': int(input("Masukkan ID Pengguna: ")),
            'nama_user': input("Masukkan Nama Pengguna: "),
            'no_telepon': input("Masukkan Nomor Telepon: "),
            'jalan': input("Masukkan Jalan: "),
            'kota': input("Masukkan Kota: "),
            'kode_pos': int(input("Masukkan Kode Pos: ")),
            'provinsi': input("Masukkan Provinsi: "),
            'durasi_huni': input("Masukkan Durasi Huni (YYYY-MM-DD): "),
            'nama_universitas': input("Masukkan Nama Universitas: "),
            'nama_fakultas': input("Masukkan Nama Fakultas: "),
            'nama_role': input("Masukkan Peran: "),
            'no_kamar': int(input("Masukkan Nomor Kamar: "))
        }
    
        try:
            # Begin transaction
            db.connection.autocommit = False

            # Create alamat
            id_alamat = create_alamat(db, user_details['jalan'], user_details['kota'], user_details['kode_pos'], user_details['provinsi'])
            
            # Create or get universitas
            id_universitas = create_or_get_universitas(db, user_details['nama_universitas'])
            
            # Create or get fakultas
            id_fakultas = create_or_get_fakultas(db, user_details['nama_fakultas'])
            
            # Create or get role
            id_role = create_or_get_role(db, user_details['nama_role'])
            
            # Create user
            id_user = create_user(db, user_details['id_user'], user_details['nama_user'], user_details['no_telepon'], id_alamat, 
                                  user_details['durasi_huni'], id_universitas, id_fakultas, id_role, user_details['no_kamar'])
            # Commit transaction
            db.connection.commit()
            return id_user

        except Exception as e:
            # Rollback transaction on error
            db.connection.rollback() 
            db.close()
            print("Registrasi Gagal:", e)
            return None
    finally:
        print("Registrasi Berhasil")