# -*- coding: utf-8 -*-
import os, sys, re
import time, datetime
from tkinter import filedialog
from tkinter import Tk
import mongo_dnn


def choose_dir():
    dir = filedialog.askdirectory(
        initialdir="./test_folder", title="Выбор каталога:")
    return dir


def file_worker(paths, file, i):
    global mask
    global f_count
    file_name = os.path.join(paths, file)
    sys.stdout.write('\r %6i:  %s%s ' %
                     (i, file_name, ' ' * (100 - len(file_name))))
    if mask.search(file_name):
        f_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_name))
        f_size = os.path.getsize(file_name)
        ff,extension = os.path.splitext(file_name)
        file_rec = {"file": file,
        			"ext": extension,
        			"path": paths,
        			"file_name": file_name,
        			"f_time": f_time,
        			"f_size": f_size}
        mongo_dnn.ins(file_rec)

        f_count += 1
    
    time.sleep(0.001)


def dir_walker(dir):
    """Walks through the files in dir."""
    mongo_dnn.drop_files()
    os.system('cls')
    print('\nProcessing...\n')
    i = 0
    for paths, dirs, files in os.walk(dir):
        for file in files:
            i += 1
            # file_name = os.path.join(paths,file)
            # file_worker(file_name, i)
            file_worker(paths, file, i)
    print('\n\n Total:' + str(i) + ' files')
    print(' Found: ' + str(f_count) + ' files')


root = Tk()
root.withdraw()

mask = re.compile(r".*\.(jpg|JPG|jpeg|JPEG|MPG|mpg|mp4|MP4|MOV|mov|WMV|wmv|AVI|avi|PNG|" +
                  "png|3gp|3GP|VOB|vob)$")

f_count = 0
dir = choose_dir()
dir_walker(dir)

ext_list = mongo_dnn.list_ext()

for ext in ext_list:
	for i in ext:
		print(ext[i], end = ' ')
	print()	




