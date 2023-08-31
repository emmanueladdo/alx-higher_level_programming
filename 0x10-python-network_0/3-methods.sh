#!/bin/bash
# Displays all HTTP methods that the server will accept
curl -sI "$1" | awk -F': ' '/^Allow/{print $2}'
