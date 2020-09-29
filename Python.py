#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
import subprocess


form=cgi.FieldStorage()
data=form.getvalue("fname")
output=subprocess.getstatusoutput(data)
print(output)
    
