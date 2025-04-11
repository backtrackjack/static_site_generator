import os
import shutil


def copy_to_directory(src, dest):
    print(f"Copying {src} to {dest}")
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source {src} does not exist.")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    if not os.path.exists(dest) and not os.path.isfile(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        item_src = os.path.join(src, item)
        item_dest = os.path.join(dest, item)
        if os.path.isfile(item_src):
            print(f"Copying file {item_src} to {item_dest}")
            shutil.copy(item_src, item_dest)
        else:
            copy_to_directory(item_src, item_dest)
