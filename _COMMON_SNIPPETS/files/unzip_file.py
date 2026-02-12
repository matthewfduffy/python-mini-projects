# Take a zip file/path to zip file, optional destination path, and unzip all contents

import os, zipfile

def unzip_all(zip_file_path, destination_path=''):
    if not destination_path:
        destination_path = os.getcwd()
    with zipfile.ZipFile(zip_file_path, 'r') as zf:
        zf.extractall(destination_path)
        moved_docs = [file for file in zf.namelist() if file]
        return moved_docs
    

# Edit Function Call Here
unzipped_files = unzip_all('My_ZipFile.zip')  # unzip in current working directory
unzipped_files = unzip_all('My_ZipFile.zip', r'<PATH to DESKTOP>')