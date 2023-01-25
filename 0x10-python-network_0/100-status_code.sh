#!/bin/bash
# Script that displays only the status code of a response from URL request.
curl -s -o /dev/null -w "%{http_code}" "$1"
