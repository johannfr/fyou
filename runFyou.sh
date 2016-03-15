#!/bin/bash

echo "P 180" | nc localhost 7989
sleep 2
echo "P 0" | nc localhost 7989
