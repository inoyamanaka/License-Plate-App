import os
import openpyxl

# Mendefinisikan path folder yang ingin di-listing
folder_path = "output/K1/"

# Mendapatkan list isi folder
folder_contents = os.listdir(folder_path)

# Membuat file Excel baru
wb = openpyxl.Workbook()
sheet = wb.active

# Menulis judul kolom ke file Excel
sheet["A1"] = "Nama File"

# Menulis isi folder ke file Excel
for idx, file_name in enumerate(folder_contents, start=2):
    sheet[f"A{idx}"] = file_name

# Menyimpan file Excel
excel_file_path = "list_kendaraan.xlsx"
wb.save(excel_file_path)

print(f"Listing folder {folder_path} berhasil disimpan ke dalam file Excel: {excel_file_path}")
