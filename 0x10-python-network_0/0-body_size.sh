#!/bin/bash
# sends a request to that URL
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
