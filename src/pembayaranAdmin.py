import pandas as pd

def update_status_pembayaran(db):
    db.check_connection()

    try:
        id_transaksi = int(input("Masukkan ID Transaksi: "))
        status_transaksi_input = input("Masukkan Status Transaksi (True untuk Sudah Bayar, False untuk Belum Bayar): ").strip().lower()
        
        # Konversi input status transaksi menjadi boolean
        if status_transaksi_input == 'true':
            status_transaksi = True
        elif status_transaksi_input == 'false':
            status_transaksi = False
        else:
            raise ValueError("Status Transaksi harus 'True' atau 'False'.")
        
        query = "UPDATE transaksi SET status_transaksi = %s WHERE id_transaksi = %s"
        db.execute(query, (status_transaksi, id_transaksi))
        print(f"Status pembayaran untuk transaksi ID {id_transaksi} telah diperbarui menjadi {'Sudah Bayar' if status_transaksi else 'Belum Bayar'}.")
    except ValueError as ve:
        print("Input tidak valid:", ve)
    except Exception as e:
        db.connection.rollback()
        print("Gagal memperbarui status pembayaran:", e)

# Contoh penggunaan fungsi update_status_pembayara



# def cek_status_transaksi(db,nim):
#     query = "select * from transaksi where id_user =232410103047"
#     db.execute(query)
#     data = db.fetch_data()
#     df = pd.DataFrame(data, columns=['a', 'NIM','c','Status Pembayaran'])
#     print(df[['NIM','Status Pembayaran']])

def cek_status_transaksi(db,nim):
    db.check_connection()
    query = f"select * from transaksi where id_user = {nim}"
    db.execute(query) 
    data = db.fetch_data()
    print(data)
    df = pd.DataFrame(data, columns=['id', 'NIM','Total Pembayaran','Status Pembayaran'])
    print(df)



