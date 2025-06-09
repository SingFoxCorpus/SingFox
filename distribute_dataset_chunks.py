import os
import shutil

# Modify these paths
source_root = 'D:\Devanshi_Himanshi_SingFox\Folder_Datasets'
destination_root = 'D:\Devanshi_Himanshi_SingFox\Testing_Dataset'  # will contain folder1 to folder11
chunk_size = 500
num_main_folders = 10  # folder1 to folder10

def get_language_folders(base_path):
    return [name for name in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, name))]

def copy_chunked_files(src_lang_path, folder_type, language):
    files = [f for f in os.listdir(src_lang_path) if os.path.isfile(os.path.join(src_lang_path, f))]
    files.sort()  # Optional: ensure consistent order
    total_chunks = (len(files) + chunk_size - 1) // chunk_size

    for i in range(total_chunks):
        if i < num_main_folders:
            dest_folder_name = f'Directory {i+1}'
        else:
            dest_folder_name = 'Directory 11'

        dest_folder = os.path.join(destination_root, dest_folder_name, folder_type, language)
        os.makedirs(dest_folder, exist_ok=True)

        chunk = files[i*chunk_size:(i+1)*chunk_size]
        for file_name in chunk:
            src_file = os.path.join(src_lang_path, file_name)
            dst_file = os.path.join(dest_folder, file_name)
            shutil.copy2(src_file, dst_file)

        print(f"Copied {len(chunk)} files to {dest_folder}")

def main():
    for folder_type in ['songs', 'music']:
        source_type_path = os.path.join(source_root, folder_type)
        languages = get_language_folders(source_type_path)

        for lang in languages:
            src_lang_path = os.path.join(source_type_path, lang)
            print(f"Processing {folder_type}/{lang}")
            copy_chunked_files(src_lang_path, folder_type, lang)

if __name__ == '__main__':
    main()
