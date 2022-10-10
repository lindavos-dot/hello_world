__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

cwd = os.getcwd()
cache_folder = os.path.join(cwd, "cache")

# 1. clean_cache

def clean_cache():
    if os.path.exists(cache_folder):
        shutil.rmtree(cache_folder)
    return os.mkdir(cache_folder)


# clean_cache()

# 2. cache_zip

def cache_zip(zip_path, dir_path):
    with zipfile.ZipFile(zip_path, "r") as unpack_zip:
        return unpack_zip.extractall(path = dir_path)


# cache_zip("", "")
# resultaat: 999 bestanden nu ook in cache

# 3. cached_files

def cached_files():
    list_abs_paths = []
    files = os.listdir(cache_folder)
    for file in files:
        if file not in list_abs_paths:
            list_abs_paths.append(os.path.abspath(os.path.join(cache_folder, file)))
    return list_abs_paths


# print(cached_files())

# 4. find_password

def find_password(paths):
    for files in paths:
        with open(files, "r") as read_file:
            for line in read_file:
                if "password" in line:
                    return line.split()[1]

    
print(find_password(cached_files()))