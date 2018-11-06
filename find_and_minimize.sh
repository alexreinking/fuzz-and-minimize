#!/bin/bash
./random_input.py $@ > bad_input
if [[ $? -ne 0 ]]; then
    rm bad_input
    exit 1
fi
./bisect_input.py $1 $2 bad_input > bad_input_min
