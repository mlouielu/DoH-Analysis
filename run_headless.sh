#!/bin/bash

while read url; do
    tcpdump -s0 -w "data/$url_firefox.pcap" &
    sleep 0.3
    python3 -c "import query; query.test_firefox_headless(\"$url\", \"https://youtube.com\")"
    sleep 1
    kill $(pgrep tcpdump)
    python3 parser.py --filename "data/$url_firefox.pcap" --output_filename "result/$url_firefox.csv"
#done < "doh_list"
done < "popular_doh"
exit 0
