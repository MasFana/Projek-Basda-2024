import pandas as pd
def read_jenis_barang(db):
    try:
        query = "SELECT * FROM jenis_barang"
        db.execute(query)
        rows = db.fetch_data()
        df = pd.DataFrame(rows, columns=['id_jenis_barang', 'nama_jenis_barang'])
        print(df)
    
    except Exception as e:
        print("Gagal membaca jenis_barang:", e)
def create_jenis_barang(db):
    read_jenis_barang(db)
    nama_jenis_barang = input("Masukkan nama jenis_barang: ")
    try:
        query = "INSERT INTO jenis_barang (nama_jenis_barang) VALUES (%s) RETURNING id_jenis_barang"
        db.execute(query, (nama_jenis_barang,))
        result = db.fetch_one()
        if result is not None and not isinstance(result, bool):
            id_jenis_barang = result[0]
            db.connection.commit()
            print("Jenis Barang berhasil ditambahkan dengan ID:", id_jenis_barang)
            return id_jenis_barang
        else:
            print("Nama jenis_barang sudah ada.")
            return None
    except Exception as e:
        db.connection.rollback()
        print("Gagal menambahkan jenis_barang:", e)
        return None
    
    
def edit_jenis_barang(db):
    read_jenis_barang(db)
    id_jenis_barang = input("Masukkan ID jenis_barang yang akan diubah: ")
    nama_jenis_barang = input("Masukkan nama jenis_barang baru: ")
    try:
        query = "UPDATE jenis_barang SET nama_jenis_barang = %s WHERE id_jenis_barang = %s"
        db.execute(query, (nama_jenis_barang, id_jenis_barang))
        db.connection.commit()
        print("Jenis Barang berhasil diubah.")
    except Exception as e:
        db.connection.rollback()
        print("Gagal mengubah jenis_barang:", e)
def delete_jenis_barang(db):
    read_jenis_barang(db)
    id_jenis_barang = input("Masukkan ID jenis_barang yang akan dihapus: ")
    try:
        query = "DELETE FROM jenis_barang WHERE id_jenis_barang = %s"
        db.execute(query, (id_jenis_barang,))
        db.connection.commit()
        print("Jenis Barang berhasil dihapus.")
    except Exception as e:
        db.connection.rollback()
        print("Gagal menghapus jenis_barang:", e)



def read_barang(db):
    try:
        query = "SELECT id_barang,nama_barang,kondisi_barang,no_kamar, j.id_jenis_barang, j.nama_jenis_barang FROM barang JOIN jenis_barang j ON barang.id_jenis_barang = j.id_jenis_barang"
        db.execute(query)
        rows = db.fetch_data()
        df = pd.DataFrame(rows, columns=['id_barang','nama_barang','kondisi_barang','no_kamar','id_jenis_barang','nama_jenis_barang'])
        print(df)
    
    except Exception as e:
        print("Gagal membaca barang:", e)
        

def create_barang(db):
    read_barang(db)
    nama_barang = input("Masukkan nama barang: ")
    kondisi_barang = input("Masukkan kondisi barang: ")
    no_kamar = input("Masukkan no kamar: ")
    read_jenis_barang(db)
    read_jenis_barang(db)
    id_jenis_barang = input("Masukkan id jenis barang: ")
    try:
        query = "INSERT INTO barang (nama_barang, kondisi_barang, no_kamar, id_jenis_barang) VALUES (%s, %s, %s, %s) RETURNING id_barang"
        db.execute(query, (nama_barang, kondisi_barang, no_kamar, id_jenis_barang))
        id_barang = db.fetch_one()[0]
        db.connection.commit()
        print("Barang berhasil ditambahkan dengan ID:", id_barang)
        return id_barang
    except Exception as e:
        db.connection.rollback()
        print("Gagal menambahkan barang:", e)
        return None

def edit_barang(db):
    read_barang(db)
    id_barang = input("Masukkan ID barang yang akan diubah: ")
    nama_barang = input("Masukkan nama barang baru: ")
    kondisi_barang = input("Masukkan kondisi barang baru: ")
    no_kamar = input("Masukkan no kamar baru: ")
    read_jenis_barang(db)
    id_jenis_barang = input("Masukkan id jenis barang baru: ")
    try:
        query = "UPDATE barang SET nama_barang = %s, kondisi_barang = %s, no_kamar = %s, id_jenis_barang = %s WHERE id_barang = %s"
        db.execute(query, (nama_barang, kondisi_barang, no_kamar, id_jenis_barang, id_barang))
        db.connection.commit()
        print("Barang berhasil diubah.")
    except Exception as e:
        db.connection.rollback()
        print("Gagal mengubah barang:", e)
        
def delete_barang(db):
    read_barang(db)
    id_barang = input("Masukkan ID barang yang akan dihapus: ")
    try:
        query = "DELETE FROM barang WHERE id_barang = %s"
        db.execute(query, (id_barang,))
        db.connection.commit()
        print("Barang berhasil dihapus.")
    except Exception as e:
        db.connection.rollback()
        print("Gagal menghapus barang:", e)