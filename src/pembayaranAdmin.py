import pandas as pd

def view_status_pembayaran(db,id=None):
    db.check_connection()
    if id is not None:
        query = f"SELECT * FROM transaksi WHERE id_transaksi = {id}"
    else:
        query = "SELECT * FROM transaksi"
    db.execute(query)
    data = db.fetch_data()
    df = pd.DataFrame(data, columns=['id_transaksi', 'id_user','total_pembayaran','status_transaksi'])
    print(df)

def update_status_pembayaran(db):
    db.check_connection()
    # id_transaksi = input("Masukkan ID Transaksi kosongi untuk semua: ")
    # if id_transaksi == "":
    #     view_status_pembayaran(db, id=None)
    # else:
    #     view_status_pembayaran(db, id=id_transaksi)
    view_status_pembayaran(db, id=None)
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

def cek_status_transaksi(db,nim=None):
    db.check_connection()
    if nim is not None:        
        query = f"select * from transaksi where id_user = {nim}"

    else:
        query = "select * from transaksi"
    db.execute(query)
    data = db.fetch_data()
    df = pd.DataFrame(data, columns=['id', 'NIM','Total Pembayaran','Status Pembayaran'])
    print(df)



