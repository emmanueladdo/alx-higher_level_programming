#!/bin/bash
# Sends a GET request to a given URL with a header and displays the response
curl -s -H "X-School-User-Id: 98" "$1"
