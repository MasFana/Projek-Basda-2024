import pandas as pd

def submit_aspirasi(db, id_user, aspirasi_text):
    try:
        query = "INSERT INTO aspirasi (id_user, isi_aspirasi) VALUES (%s, %s) RETURNING id_aspirasi"
        db.execute(query, (id_user, aspirasi_text))
        id_aspirasi = db.fetch_one()[0]
        db.connection.commit()
        print("Aspirasi berhasil dikirim dengan ID:", id_aspirasi)
        input("Tekan Enter untuk melanjutkan...")
        return id_aspirasi
    except Exception as e:
        db.connection.rollback()
        print("Gagal mengirim aspirasi:", e)
        input("Tekan Enter untuk melanjutkan...")
        return None

def read_aspirasi(db):
    try:
        query = "SELECT * FROM aspirasi"
        db.execute(query)
        rows = db.fetch_data()
        df = pd.DataFrame(rows, columns=['id_aspirasi', 'isi_aspirasi','tanggal_aspirasi'," id_user"])
        # align dataframes and edit tanggal aspirasi to datetime
        df['tanggal_aspirasi'] = df['tanggal_aspirasi'].dt.tz_localize('UTC').dt.tz_convert('Asia/Jakarta').dt.strftime('%Y-%m-%d %H:%M:%S')       
        print(df)
        input("Tekan Enter untuk melanjutkan...")
    except Exception as e:
        print("Gagal membaca aspirasi:", e)
        input("Tekan Enter untuk melanjutkan...")

