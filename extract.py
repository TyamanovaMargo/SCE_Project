import os
import shutil

def extract_txt_files(src_dir, dest_dir):
    # Создаем папку назначения, если ее нет
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Проходим по всем подпапкам в исходной папке
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.txt'):
                # Полный путь к исходному файлу
                file_path = os.path.join(root, file)
                # Полный путь к файлу назначения
                dest_path = os.path.join(dest_dir, file)
                # Перемещаем файл
                shutil.move(file_path, dest_path)
                print(f"Файл {file_path} перемещен в {dest_path}")

# Укажите путь к исходной папке и папке назначения
src_directory = '/Users/margotiamanova/Desktop/identification/Fantastica_DATASET_Rulut/NEGATIVE'
dest_directory = '/Users/margotiamanova/Desktop/identification/Fantastica_DATASET_Rulut/NEGATIVE'

extract_txt_files(src_directory, dest_directory)
