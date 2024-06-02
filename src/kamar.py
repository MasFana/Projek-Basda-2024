import pandas as pd

def view_kamar_kosong(db):
    query = """
    SELECT k.no_kamar, k.status
    FROM kamar k
    WHERE k.status = 'Tersedia'
    """
    db.execute(query)
    data = db.fetch_data()
    df = pd.DataFrame(data, columns=['Nomor Kamar', 'Status'])
    print("Kamar Kosong:")
    print(df)

def view_penghuni_kamar(db):
    try:
        query = """
        SELECT k.no_kamar, u.nama_user
        FROM kamar k
        LEFT JOIN users u ON k.no_kamar = u.no_kamar
        WHERE k.status = 'Tersedia'
        """
        db.execute(query)
        data = db.fetch_data()
        
        if not data:
            print("Tidak ada kamar yang dihuni.")
            return
        
        df = pd.DataFrame(data, columns=['Nomor Kamar', 'Nama Penghuni'])
        print("Kamar yang Dihuni:")
        print(df)
        try:
            no_kamar = int(input("Masukkan nomor kamar untuk melihat detail penghuni: "))
        except ValueError:
            print("Nomor kamar harus berupa angka.")
            return
        
        # Pengecekan nomor kamar valid
        if not df['Nomor Kamar'].astype(str).str.contains(str(no_kamar)).any():
            print("Nomor kamar tidak valid.")
            return

        query_detail = """
        SELECT u.id_user, u.nama_user, u.no_telepon, a.jalan, a.kota, a.kode_pos, a.provinsi,
        u.durasi_huni, un.nama_universitas, f.nama_fakultas, r.nama_role
        FROM users u
        JOIN alamat a ON u.id_alamat = a.id_alamat
        LEFT JOIN universitas un ON u.id_universitas = un.id_universitas
        LEFT JOIN fakultas f ON u.id_fakultas = f.id_fakultas
        LEFT JOIN role r ON u.id_role = r.id_role
        WHERE u.no_kamar = %s
        """
        db.execute(query_detail, (no_kamar,))
        penghuni_data = db.fetch_data()

        if not penghuni_data:
            print("Tidak ada penghuni untuk kamar ini.")
            return

        detail_columns = ['ID Pengguna', 'Nama Pengguna', 'Nomor Telepon', 'Jalan', 'Kota', 'Kode Pos', 'Provinsi',
                          'Durasi Huni', 'Universitas', 'Fakultas', 'Peran']
        penghuni_df = pd.DataFrame(penghuni_data, columns=detail_columns)

        print("\nDetail Penghuni untuk Kamar Nomor", no_kamar)
        print(penghuni_df)
    except Exception as e:
        print("Error:", e)
