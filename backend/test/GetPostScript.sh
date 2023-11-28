#!/bin/bash

echo "About to send request..."
curl http://127.0.0.1:5000/requestData
echo "Request sent."

echo "Sending some data back"
curl -Uri http://127.0.0.1:5000/submitResponse -Method POST -ContentType "application/json" -Body '{"key":"value"}'
echo "Sent data."