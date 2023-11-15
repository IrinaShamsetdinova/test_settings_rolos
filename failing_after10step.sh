#!/bin/bash

for i in $(seq 1 15); do
    echo "$i"
    sleep 10

    if [ "$i" -eq 10 ]; then
        exit 1
    fi
done