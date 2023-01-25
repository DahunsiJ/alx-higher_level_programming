#!/bin/bash
# Script that sends a JSON POST request and displays response body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
