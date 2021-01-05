from time import sleep
from glob import glob
import os, shutil

name = 'screenshot'
types = ('*.png','*.jpeg','*.jpg','*.gif')

destination = './screenshots'

def img_file_exists():
    return [file for f_ in [glob(e) for e in types] for file in f_ if name in file.lower()]

def move_files(files: list):
    for file in files:
        print(f"Moving \"{file}\"...")

        if not os.path.exists(destination+"/"+file):
            shutil.move(file, destination)
            print(f"Done!")

        else:
            base, extension = os.path.splitext(file)
            
            i = 1
            while True:
                new_file = base + "_" + str(i) + extension
                if not os.path.exists(destination+"/"+new_file):
                    os.rename(file, new_file)
                    shutil.move(new_file, destination)
                    print(f"Renamed \"({file}\" to {new_file}\nDone!")
                    break
                i += 1

def main():
    desktop = img_file_exists()
    if not desktop:
        sleep(10)
    else:
        move_files(desktop)

if __name__ == "__main__":
    while True:
        main()