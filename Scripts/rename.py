"This script renames the python files to #-problem-title format"

import os

prepath = "../Solutions/"
blacklist = [".DS_Store", "-DS_Store"]

for file in os.listdir(prepath):
	if file in blacklist:	continue
	new_name = file.replace(" ", "-").replace(".", "-")
	#print os.path.join(prepath, file), os.path.join(prepath, new_name)
	os.rename(os.path.join(prepath, file), os.path.join(prepath, new_name))