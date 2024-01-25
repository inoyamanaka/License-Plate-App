import os
import pandas as pd

def list_files_in_folder(folder_path):
    try:
        # Mendapatkan daftar file dalam folder
        files = os.listdir(folder_path)

        # Menampilkan nama file
        print("Daftar file di folder '{}':".format(folder_path))
        for file_name in files:
            print(file_name)

        # Menyimpan daftar file dalam file Excel
        df = pd.DataFrame({'Nama File': files})
        excel_file_path = os.path.join(folder_path, 'daftar_file.xlsx')
        df.to_excel('D:/python/license-plate-application/daftar_file.xlsx', index=False)

        print("Daftar file telah disimpan dalam file Excel: {}".format(excel_file_path))

    except FileNotFoundError:
        print("Folder '{}' tidak ditemukan.".format(folder_path))
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

# Ganti path_folder dengan path folder yang ingin Anda list
path_folder = "D:/Dataset/Plat kendaraan/K4"
list_files_in_folder(path_folder)
