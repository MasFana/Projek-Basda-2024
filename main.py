from email.policy import default
from db.database import Database
from src.login import *
from src.mahasiswa import *
db = Database()
db.open()

teks_admin = f"""
███╗   ███╗███████╗███╗   ██╗██╗   ██╗    ███████╗████████╗ █████╗ ███████╗███████╗
████╗ ████║██╔════╝████╗  ██║██║   ██║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║    ███████╗   ██║   ███████║█████╗  █████╗  
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║    ╚════██║   ██║   ██╔══██║██╔══╝  ██╔══╝  
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝    ███████║   ██║   ██║  ██║██║     ██║     
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝      
    
    
    [ 1 ] View Penhuni         
    [ 2 ] Register Penghuni     
    [ 3 ] View Password
    [ 0 ] Keluar
                                                           
"""
# view_password(db)
# login(db)
def menu_admin():
    print(teks_admin)
    men = None
    men = input(f"    [ o ] Pilih menu: ")
    while men != "0":
        match men:
            case "1":
                view_all_users(db)
            case "2":
                register_user(db)
            case "3":
                view_password(db)
            case "0":
                pass
            case default:
                print("Pilihan tidak tersedia")
            
def menu_penghuni():
    pass
def menu_pengunjung():
    pass
    
def menu_login():
    try:
        nama_user,role = login(db)
    except:
        nama_user,role = None,None

    if role == "penghuni" :
        print(f"Halo {nama_user}")
    else:
        print(f"Halo Admin {nama_user}")
    
menu_admin()
db.close()
