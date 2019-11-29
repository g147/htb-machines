#!/bin/bash

ports="3456 8234 62431"
host="10.10.10.83"

for x in $ports
do
	nmap -Pn -p $x $host
	sleep 1
done
ssh prometheus@${host}

