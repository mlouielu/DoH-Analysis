#!/bin/bash

while read url; do
    results=$(drill $url | awk '/^[^;]/{print $5}' | sort -u)
    echo "$results" | while read -r line; do echo "$line"; done
done < "doh_list"
