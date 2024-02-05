import os

def delete_files_func(path='/path/to/folder', file_extension='.txt'):
    removed_files = []
    path='.'+path
    for file in os.listdir(path):
        if file_extension in file:
            removed_files.append(file)
            os.remove(path+'/'+file)
    print("List of the removed files: ", removed_files)

delete_files_func('/path/folder', file_extension='.txt')