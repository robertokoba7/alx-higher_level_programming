#!/bin/bash
#display the size of the body of the http response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
