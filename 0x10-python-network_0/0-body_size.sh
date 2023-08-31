#!/bin/bash
# Displays the size of the body of a response of a URL
curl -s "$1" | wc -c
