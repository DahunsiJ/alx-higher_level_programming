#!/bin/bash
# Script that sends a POST request to a URL, and displays response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
