#Kelompok 2
#Kelas S1SI-23-01
# Anggota:
# Muhammad Zidan Alfarizi - 102042300196
# Muhammad Nabil Shidqiy - 102042300026
# Muhammad Bintang Wirajudha - 102042300208


#--->Sistem Restoran<---

import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

db_0102 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restoran_ngasal"
)
cursor_0102 = db_0102.cursor()

# cursor = db.cursor()
# cursor.execute("CREATE DATABASE restoran_ngasal")
# print("Database berhasil")

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS menu (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nama VARCHAR(255) NOT NULL,
#         deskripsi TEXT,
#         harga DECIMAL(10, 2) NOT NULL
#     )
# ''')

# print('Table berhasil dibuat')

# cursor.execute("ALTER TABLE menu ADD COLUMN diskon DECIMAL(5, 2) DEFAULT 0")
# cursor.execute("ALTER TABLE menu ADD COLUMN diskon_aktif BOOLEAN DEFAULT FALSE")

def tambah_item_0102(nama_0102, deskripsi_0102, harga_0102, diskon_0102=0):
    cursor_0102.execute('INSERT INTO menu (nama, deskripsi, harga, diskon, diskon_aktif) VALUES (%s, %s, %s, %s, %s)', (nama_0102, deskripsi_0102, harga_0102, diskon_0102, False))
    db_0102.commit()
    print('Item berhasil ditambahkan!')

def lihat_item_menu_0102():
    cursor_0102.execute('SELECT * FROM menu')
    items_0102 = cursor_0102.fetchall()
    
    for item_0102 in items_0102:
        id_0102, nama_0102, deskripsi_0102, harga_0102, diskon_0102, diskon_aktif_0102 = item_0102
        status_diskon_0102 = 'Aktif' if diskon_aktif_0102 else 'Tidak Aktif'
        harga_setelah_diskon_0102 = harga_0102 * (1 - diskon_0102 / 100) if diskon_aktif_0102 else harga_0102
        print(f"ID: {id_0102}, Nama: {nama_0102}, Deskripsi: {deskripsi_0102}, Harga: {harga_0102}, Diskon: {diskon_0102}%, Diskon Aktif: {status_diskon_0102}, Harga Setelah Diskon: {harga_setelah_diskon_0102}")

def update_item_0102(id_0102, nama_0102, deskripsi_0102, harga_0102, diskon_0102):
    cursor_0102.execute('UPDATE menu SET nama = %s, deskripsi = %s, harga = %s, diskon = %s WHERE id = %s', (nama_0102, deskripsi_0102, harga_0102, diskon_0102, id_0102))
    db_0102.commit()
    print('Item berhasil diperbarui!')

def delete_item_0102(id_0102):
    cursor_0102.execute('DELETE FROM menu WHERE id = %s', (id_0102,))
    db_0102.commit()
    print('Item berhasil dihapus!')

def search_item_0102(keyword_0102):
    cursor_0102.execute('SELECT * FROM menu WHERE nama LIKE %s OR deskripsi LIKE %s', ('%' + keyword_0102 + '%', '%' + keyword_0102 + '%'))
    items_0102 = cursor_0102.fetchall()

    for item_0102 in items_0102:
        id_0102, nama_0102, deskripsi_0102, harga_0102, diskon_0102, diskon_aktif_0102 = item_0102
        status_diskon_0102 = 'Aktif' if diskon_aktif_0102 else 'Tidak Aktif'
        harga_setelah_diskon_0102 = harga_0102 * (1 - diskon_0102 / 100) if diskon_aktif_0102 else harga_0102
        print(f"ID: {id_0102}, Nama: {nama_0102}, Deskripsi: {deskripsi_0102}, Harga: {harga_0102}, Diskon: {diskon_0102}%, Diskon Aktif: {status_diskon_0102}, Harga Setelah Diskon: {harga_setelah_diskon_0102}")

def filter_harga_0102(min_harga_0102, max_harga_0102):
    cursor_0102.execute('SELECT * FROM menu WHERE harga BETWEEN %s AND %s', (min_harga_0102, max_harga_0102))
    items_0102 = cursor_0102.fetchall()

    for item_0102 in items_0102:
        id_0102, nama_0102, deskripsi_0102, harga_0102, diskon_0102, diskon_aktif_0102 = item_0102
        status_diskon_0102 = 'Aktif' if diskon_aktif_0102 else 'Tidak Aktif'
        harga_setelah_diskon_0102 = harga_0102 * (1 - diskon_0102 / 100) if diskon_aktif_0102 else harga_0102
        print(f"ID: {id_0102}, Nama: {nama_0102}, Deskripsi: {deskripsi_0102}, Harga: {harga_0102}, Diskon: {diskon_0102}%, Diskon Aktif: {status_diskon_0102}, Harga Setelah Diskon: {harga_setelah_diskon_0102}")

def visualisasi_sebelum_diskon_0102():
    cursor_0102.execute('SELECT nama, harga FROM menu')
    items_0102 = cursor_0102.fetchall()
    nama_0102 = [item[0] for item in items_0102]
    harga_0102 = np.array([item[1] for item in items_0102])

    plt.bar(nama_0102, harga_0102)
    plt.xlabel('Nama Menu')
    plt.ylabel('Harga')
    plt.title('Visualisasi Menu')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualisasi_setelah_diskon_0102():
    cursor_0102.execute('SELECT nama, harga, diskon, diskon_aktif FROM menu')
    items_0102 = cursor_0102.fetchall()
    nama_0102 = [item[0] for item in items_0102]
    harga_0102 = np.array([item[1] for item in items_0102])
    diskon_0102 = np.array([item[2] for item in items_0102])
    diskon_aktif_0102 = np.array([item[3] for item in items_0102])

    harga_setelah_diskon_0102 = [harga * (1 - diskon / 100) if aktif else harga for harga, diskon, aktif in zip(harga_0102, diskon_0102, diskon_aktif_0102)]

    plt.bar(nama_0102, harga_setelah_diskon_0102)
    plt.xlabel('Nama Menu')
    plt.ylabel('Harga Setelah Diskon')
    plt.title('Visualisasi Harga Menu Setelah Diskon')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def aktifkan_diskon_0102(nama_0102, status_0102):
    cursor_0102.execute('UPDATE menu SET diskon_aktif = %s WHERE nama = %s', (status_0102, nama_0102))
    db_0102.commit()
    status_str_0102 = 'diaktifkan' if status_0102 else 'dinonaktifkan'
    print(f'Diskon berhasil {status_str_0102} untuk item dengan nama {nama_0102}!')

def set_diskon_0102(nama_0102, diskon_0102):
    cursor_0102.execute('UPDATE menu SET diskon = %s WHERE nama = %s', (diskon_0102, nama_0102))
    db_0102.commit()
    print(f'Diskon sebesar {diskon_0102}% berhasil diatur untuk item dengan nama {nama_0102}!')

def menu_0102():
    while True:
        print("\nMenu Restaurant")
        print("1. Tambah Item Menu")
        print("2. Lihat Menu")
        print("3. Perbarui Item Menu")
        print("4. Hapus Item Menu")
        print("5. Cari Item Menu")
        print("6. Filter Item Menu Berdasarkan Harga")
        print("7. Visualisasi Harga Sebelum Diskon")
        print("8. Visualisasi Harga Setelah Diskon")
        print("9. Atur Diskon")
        print("10. Aktifkan/Nonaktifkan Diskon")
        print("11. Keluar")
        pilihan_0102 = input("Pilih opsi: ")

        if pilihan_0102 == '1':
            nama_0102 = input("Nama: ")
            deskripsi_0102 = input("Deskripsi: ")
            harga_0102 = float(input("Harga: "))
            diskon_0102 = float(input("Diskon (%): "))
            tambah_item_0102(nama_0102, deskripsi_0102, harga_0102, diskon_0102)
        
        elif pilihan_0102 == '2':
            lihat_item_menu_0102()
        
        elif pilihan_0102 == '3':
            id_0102 = int(input("ID Item: "))
            nama_0102 = input("Nama baru: ")
            deskripsi_0102 = input("Deskripsi baru: ")
            harga_0102 = float(input("Harga baru: "))
            diskon_0102 = float(input("Diskon baru (%): "))
            update_item_0102(id_0102, nama_0102, deskripsi_0102, harga_0102, diskon_0102)
        
        elif pilihan_0102 == '4':
            id_0102 = int(input("ID Item: "))
            delete_item_0102(id_0102)
        
        elif pilihan_0102 == '5':
            keyword_0102 = input("Masukkan kata kunci: ")
            search_item_0102(keyword_0102)
        
        elif pilihan_0102 == '6':
            min_harga_0102 = float(input("Harga minimum: "))
            max_harga_0102 = float(input("Harga maksimum: "))
            filter_harga_0102(min_harga_0102, max_harga_0102)
        
        elif pilihan_0102 == '7':
            visualisasi_sebelum_diskon_0102()
        
        elif pilihan_0102 == '8':
            visualisasi_setelah_diskon_0102()
        
        elif pilihan_0102 == '9':
            nama_0102 = input("Nama Item: ")
            diskon_0102 = float(input("Diskon (%): "))
            set_diskon_0102(nama_0102, diskon_0102)
        
        elif pilihan_0102 == '10':
            nama_0102 = input("Nama Item: ")
            status_0102 = input("Aktifkan diskon? (y/n): ").strip().lower() == 'y'
            aktifkan_diskon_0102(nama_0102, status_0102)
        
        elif pilihan_0102 == '11':
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

menu_0102()

db_0102.close()
