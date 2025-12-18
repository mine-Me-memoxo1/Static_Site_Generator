import os
import shutil


def src_to_dest(src=os.path.abspath('./static'), dest=os.path.abspath('./public')):
    if not os.path.exists(src):
        raise ValueError('Source path does not exist')
    elif os.path.isfile(src):
        raise ValueError('Input path is not a directory')
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    print(f'Copying files from {src} to {dest}')
    print(f'Copying all of {os.listdir(src)}')
    files = os.listdir(src)
    for file in files:
        ab_path = os.path.abspath(os.path.join(src, file))
        if os.path.isfile(ab_path):
            new_file_path = shutil.copy(ab_path, dest)
            print(f'{new_file_path} successfully copied')
        else:
            new_dir_path = os.path.join(dest, file)
            src_to_dest(ab_path, new_dir_path)
    
