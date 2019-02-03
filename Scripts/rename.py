"This script renames the python files"

import os

prepath = "../Solutions/"

for file in os.listdir(prepath):
	num, title = file.split('.')
	title.lstrip(" ").rstrip(" ")
	new_name = "-".join(title.split())
	os.rename(prepath + file, prepath + new_name)