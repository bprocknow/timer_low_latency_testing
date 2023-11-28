#!/bin/bash

echo "Sending some data back"
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://127.0.0.1:5000/submitResponse
echo "Sent data."