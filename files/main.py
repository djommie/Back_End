__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import glob
import zipfile


def clean_cache():
    path = './files/cache'
    if os.path.exists(path):
        files = glob.glob(path + '/*')
        for f in files:
            os.remove(f)
    else:
        os.mkdir(path)


def cache_zip(target_path, destination_path):
    with zipfile.ZipFile(target_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)


def cached_files():
    file_list = []
    path = './files/cache'
    files = glob.glob(path + '/*')
    for f in files:
        file_list.append(os.path.abspath(f))
    return file_list


def find_password(file_list):
    for file in file_list:
        with open(file, 'r') as f:
            data = f.read()
            if 'password' in data:
                chunks = data.split('\n')
                for chunk in chunks:
                    if 'password' in chunk:
                        return chunk[chunk.find(' ')+1:]
