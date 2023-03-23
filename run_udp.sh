#!/bin/bash

while read url; do
    tcpdump -i wlan0 -s0 -w "data/udp_$url.pcap" "udp and (`cat doh_only_ip | awk '{printf "dst host %s or ", $0}' | sed 's/ or $//g'` or `cat doh_only_ip | awk '{printf "src host %s or ", $0}' | sed 's/ or $//g'`)" &
    sleep 0.3
    python -c "import query; query.test_udp(\"$url\")"
    sleep 1
    kill $(pgrep tcpdump)
    python parser_udp.py --filename "data/udp_$url.pcap" --output_filename "result/udp_$url.csv"
#done < "doh_list"
done < "popular_doh"
exit 0
