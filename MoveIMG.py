import os
from os import rename 
import shutil
from time import sleep

# image name and type to find, change for better options
name_image = 'screenshot'
file_types = ('.png','.jpeg','.jpg','.gif')

# source directory and destination, change for better options
source = '/Users/Joshua/Desktop/'
destination = '/Users/Joshua/Desktop/screenshots'


    
# find file if contains 'screenshot' and file types (images). Constantly used throughout the code
def img_file_exists():
    return [file for file in os.listdir() if name_image in file.lower() if file.endswith(file_types)]

def move_file(file: str, renamed = False):
    shutil.move(source+file, destination)

    if not renamed:
        print(f'Moved {file} to {destination}')
    else:
        print(f'Renamed it to {file} and moved to {destination}')


# Finds a file that exists in the destination folder, renames it and moves to the destination if move_file() --> error
def rename_file_move(img_file):
    num_count = 0
    old_img = img_file

    # add an integer before "." for renaming
    while img_file in os.listdir(destination):
        
        if '.jpeg' not in img_file:  # Check wheter it is .jpeg (-5 indexes) or not (.png or .jpg which is only -4 indexes)
            img_file = f'{img_file[:-5]}{num_count}{img_file[-4:]}'
        else:
            img_file = f'{img_file[:-6]}{num_count}{img_file[-5:]}'
        num_count += 1
        
    os.rename(source+old_img,source+img_file)

    move_file(img_file, renamed=True)
        
    
def main():
    while not img_file_exists():
        sleep(1)
    for file in img_file_exists():
        try:
            move_file(file)
        except:
            rename_file_move(file)

if __name__ == "__main__":
    while True:
        main()