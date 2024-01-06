import os

def count_shared_files(folder1, folder2):
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    shared_files = files1.intersection(files2)

    return len(shared_files), shared_files

folder_path1 = 'output/K2'
folder_path2 = 'result/draw_text/K2'

count, shared_files = count_shared_files(folder_path1, folder_path2)

print(f"Total shared files: {count}")
print(f"Shared files: {shared_files}")
