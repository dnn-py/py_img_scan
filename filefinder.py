# -*- coding: utf-8 -*-
import os
import sys
import re
from time import sleep
from tkinter import filedialog
from tkinter import Tk


def choose_dir():
	dir  = filedialog.askdirectory(initialdir = "./test_folder", title = "Выбор каталога:")
	return dir


def file_worker(paths,file, i):
	# sys.stdout.write('\r %6i:  %s%s ' % (i, file_name, ' ' * (100 - len(file_name)) ))
	global mask
	global f_count
	file_name = os.path.join(paths,file)
	if mask.search(file_name) :
		print(file_name)
		f_count+=1
	else:
		print(file_name)

	sleep(0.0001)
	

def dir_walker(dir):
	"""Walks through the files in dir."""
	os.system('cls') 
	print('\nProcessing...\n')
	i = 0
	for paths, dirs, files in os.walk(dir):
		for file in files:
			i += 1
			# file_name = os.path.join(paths,file)
			# file_worker(file_name, i)
			file_worker(paths,file, i)
	print('\n\n Total:' + str(i) + ' files')
	print(' Found: ' + str(f_count) + ' files', end ='\r')	



root = Tk()
root.withdraw() 

mask = re.compile(r".*\.(jpg|JPG|jpeg|JPEG|MPG|mpg|mp4|MP4|MOV|mov|WMV|wmv|AVI|avi|PNG|pdf|" +
	"psd|PSD|)$")
f_count = 0
dir = choose_dir()	
dir_walker(dir)





