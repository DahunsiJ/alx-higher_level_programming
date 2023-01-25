#!/bin/bash
# Script that sends a request to a URL and shows the size of response body
curl -s "$1" | wc -c
