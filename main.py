import os
from db.database import Database
from src.pembayaranAdmin import *
from src.barang import *
from src.login import *
from src.users import *
from src.aspirasi import *
from src.kamar import *
db = Database()

for i in range(4):
    if db.open():
        break
    else:
        pass


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
teks_admin = f"""
███╗   ███╗███████╗███╗   ██╗██╗   ██╗   
████╗ ████║██╔════╝████╗  ██║██║   ██║   
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║   
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║   
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝   
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝    
                                         
███████╗████████╗ █████╗ ███████╗███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
███████╗   ██║   ███████║█████╗  █████╗  
╚════██║   ██║   ██╔══██║██╔══╝  ██╔══╝  
███████║   ██║   ██║  ██║██║     ██║     
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝     
                                           
    
    [ 1 ] View Penhuni         
    [ 2 ] Register Penghuni     
    [ 3 ] View Password
    [ 0 ] Keluar
                                                           
"""

teks_view_penghuni = f"""
                    ██╗     ██╗███████╗████████╗                 
                    ██║     ██║██╔════╝╚══██╔══╝                 
                    ██║     ██║███████╗   ██║                    
                    ██║     ██║╚════██║   ██║                    
                    ███████╗██║███████║   ██║                    
                    ╚══════╝╚═╝╚══════╝   ╚═╝                    
                                                                 
██████╗ ███████╗███╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗██╗
██╔══██╗██╔════╝████╗  ██║██╔════╝ ██║  ██║██║   ██║████╗  ██║██║
██████╔╝█████╗  ██╔██╗ ██║██║  ███╗███████║██║   ██║██╔██╗ ██║██║
██╔═══╝ ██╔══╝  ██║╚██╗██║██║   ██║██╔══██║██║   ██║██║╚██╗██║██║
██║     ███████╗██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║
╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                                                                                                                                 
"""

teks_view_password = f"""
                    ██╗     ██╗███████╗████████╗                   
                    ██║     ██║██╔════╝╚══██╔══╝                   
                    ██║     ██║███████╗   ██║                      
                    ██║     ██║╚════██║   ██║                      
                    ███████╗██║███████║   ██║                      
                    ╚══════╝╚═╝╚══════╝   ╚═╝                      
                                                                   
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

"""

teks_register_penghuni = f"""
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   █████╗  ██████╔╝
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                       

"""

# login(db)

def menu_admin():
    print(teks_admin)
    men = None
    while men != "0":
        men = input(f"    [ o ] Pilih menu: ")
        clear()
        match men:
            case "1":
                db.check_connection()
                print(teks_view_penghuni)
                view_all_users(db)
                input("[ x ] Tekan enter untuk kembali")
                clear()
            case "2":
                db.check_connection()
                print(teks_register_penghuni)
                register_user(db)
                input("[ x ] Tekan enter untuk kembali")
                clear()
            case "3":
                db.check_connection()
                print(teks_view_password)
                print(view_password(db))
                input("[ x ] Tekan enter untuk kembali")
                clear()
            case "0":
                os._exit(0)
            case default:
                print("Pilihan tidak tersedia")
        clear()
        menu_admin()


def menu_staff(id_user):
    print("Selamat datang di menu staff!")
    print("1. Edit User")
    print("2. Pembayaran")
    print("3. Aspirasi")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")
    
    if pilihan == '1':
        db.check_connection()
        print(edit_users(db))
        input('Enter untuk kembali')
        clear( )
    
    elif pilihan == '2':
        db.check_connection()
        print(update_status_pembayaran(db))
        input('Enter untuk kembali')
        clear( )

    elif pilihan == '3':
        db.check_connection()
        print("1. jenis barang")
        print("2. Tambah barang")
        print("3. Edit barang")
        print("4. Hapus barang")
        sub_pilihan = input("Masukkan pilihan Anda: ")
        if sub_pilihan == '1':
            print(read_jenis_barang(db))
            input('Enter untuk kembali')
        elif sub_pilihan == '2':
            print(create_jenis_barang(db))
            input('Enter untuk kembali')
        elif sub_pilihan == '3':
            print(edit_jenis_barang(db))
            input('Enter untuk kembali')
        elif sub_pilihan == '4':
            print(delete_jenis_barang(db))
            input('Enter untuk kembali')
        else:
            print("Pilihan tidak valid!")
            print('Tekan enter untuk kembali')
            
    elif pilihan == '4':
        db.check_connection()
        cek_status_transaksi(db)
        input()
    
    else:
        db.check_connection()
        print("Pilihan tidak valid!")
    print('Tekan enter untuk kembali')
    clear()
    menu_staff(id_user)
            
def menu_penghuni(id_user):
    print("Selamat datang di menu penghuni!")
    print("1. Lihat kamar kosong")
    print("2. Lihat Penghuni")
    print("3. Aspirasi")
    print("4. Cek status")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")
    if pilihan == '1':
        db.check_connection()
        print('DAFTAR KAMAR KOSONG')
        print(view_kamar_kosong(db))
        input('Enter untuk kembali')
        clear( )
    elif pilihan == '2':
        db.check_connection()
        print(view_penghuni_kamar(db))
        input('Enter untuk kembali')
    elif pilihan == '3':
        db.check_connection()
        print('SAMPAIKAN ASPIRASI ANDA')
        print(submit_aspirasi(db, id_user, input("Masukkan aspirasi Anda: ")) )
    elif pilihan == '4':
        db.check_connection()
        cek_status_transaksi(db,id_user)
        input()
    else:
        db.check_connection()
        print("Pilihan tidak valid!")
    print('Tekan enter untuk kembali')
    clear()
    menu_penghuni(id_user)

def menu_pengunjung():
    print(print_kamar(db))
    

def menu():
    menu_pengunjung()
    print("Selamat datang di menu pengunjung!")
    log = input("Apakah Anda ingin login? (y/n): ")
    if log == 'y':
        db.check_connection()
        menu_login()
    else:
        db.check_connection()
        menu()

def menu_login():
    try:
        nama_user,role,id_user = login(db)
        print(nama_user,role)
    except:
        return
    if role == "Penghuni" :
        print(f"Halo {nama_user}")
        menu_penghuni(id_user)
    elif role == "Staff" :
        print(f"Halo Admin {nama_user}")
        menu_staff(id_user)
    else:
        print("Login gagal - Coba lagi!")
        input("Tekan enter untuk kembali")
    clear()
menu()
db.close()
