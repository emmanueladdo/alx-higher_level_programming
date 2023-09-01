#!/bin/bash
# Send a POST request with JSON data and display the response body
curl -sH "Content-Type: application/json" -d @"$2" "$1"
