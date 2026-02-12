# Takes a path to individual files and adds all to zip

import os, zipfile

def zip_all(path_to_files, zip_file_path):
    zipped_files = []
    o_dir=os.getcwd()
    with zipfile.ZipFile(zip_file_path, 'a') as zf:
        os.chdir(path_to_files)
        for file in os.listdir(path_to_files):
            zf.write(file, compress_type=zipfile.ZIP_DEFLATED)
            zipped_files.append(file)
        os.chdir(o_dir)
        return zipped_files
    
    
# function call here to zip files
zipped_files = zip_all(r'<PATH TO FOLDER WITH FILES>', r'C://Users/A123/Desktop/My_New_ZipFile.zip')