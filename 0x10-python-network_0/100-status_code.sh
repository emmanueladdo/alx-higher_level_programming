#!/bin/bash 
#Sends a request to URL paased as an arg and displays status code
curl -o /dev/null -I -s -w "%{http_code}\n" "$1"
