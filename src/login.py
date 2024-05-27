# import sys
# import os
import pandas as pd
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from db.database import Database
# base = Database()

def login(db):
    nama_user = input("Nama: ")
    password = input("Password: ")
    password = decrypt(password, nama_user[0])
    print(password)
    query = "SELECT u.nama_user, r.nama_role from users u JOIN role r ON u.id_role = r.id_role WHERE LOWER(u.nama_user) = LOWER(%s) AND u.id_user = %s;"
    db.execute(query, (nama_user, password))
    data = db.fetch_data()
    data = data[0] if data else False
    if data:
        print(f"Login berhasil ",data)
        return data
    else:
        print("Login gagal")
        return data
        
def view_password(db):
    query = "SELECT id_user,nama_user FROM users;"
    db.execute(query)
    data = db.fetch_data()
    if data:
        data = [list(t) for t in data]
        for i,d in enumerate(data):
            data[i].append(encrypt(d[0], d[1][0]))
            dat = pd.DataFrame(data, columns=["id_user","nama_user","password"])
            return dat
    else:
        return False
        
def encrypt(int_list, key):
    int_list = map(int,list(str(int_list)))
    key_value = ord(key) - ord('a')
    encrypted_list = [chr((i + key_value) % 26 + ord('a')) for i in int_list]
    encrypted_list = "".join(encrypted_list)
    return encrypted_list

def decrypt(encrypted_list, key):
    encrypted_list = list(encrypted_list)
    key_value = ord(key) - ord('a')
    decrypted_list = [(ord(i) - ord('a') - key_value) % 26 for i in encrypted_list]
    decrypted_list = int("".join([str(i) for i in decrypted_list]))
    return decrypted_list

# encrypted = encrypt(232410103047, "j")
# print(encrypted)
# decrypted = decrypt(encrypted, "z")
# print(decrypted)
# base.open()

# print(view_password(base))

# base.close()