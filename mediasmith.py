import argparse
import os


# Instantiate the parser
parser = argparse.ArgumentParser(description='#### Mediasmith | Your personal media manager ####')
parser.add_argument("-f", "--file", help="Give path to your media file name here")
parser.add_argument("-x", "--folder", help="Give path to your media folder here")
parser.add_argument("-m", "--mode", help="Give processing mode if just want results for something specific.", choices=['movie', 'tv', 'song', 'auto'], default = 'auto')

args = parser.parse_args()

file_path = args.file
folder_path = args.folder
search_mode = args.mode

def return_file(file_path):
    file_list = []
    file_list.append(file_path)
    return file_list

def return_folder(folder_path):
    folder_list = []
    
    for folder in os.walk(folder_path):
        folder_list.append(folder)

    return folder_list  # returns the list of files in the folder recursively. 

def main():
    
    proc_q = []

    if file_path is not None:
        proc_q = return_file(file_path)

    elif folder_path is not None:
        proc_q = return_folder(folder_path)

    print("It's time to clean up your media stuff\n\t\t\tCleaning the following files/folders:\n", proc_q)
    



if __name__ == "__main__":
    main()
