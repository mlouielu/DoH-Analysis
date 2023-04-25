#!/bin/bash

while read url; do
    tcpdump -i enp0s3 -s0 -w "data/$url.pcap" "tcp and (`cat doh_only_ip | awk '{printf "dst host %s or ", $0}' | sed 's/ or $//g'` or `cat doh_only_ip | awk '{printf "src host %s or ", $0}' | sed 's/ or $//g'`)" &
    sleep 0.3
    python3 -c "import query; query.test(\"$url\")"
    sleep 1
    kill $(pgrep tcpdump)
    python3 parser.py --filename "data/$url.pcap" --output_filename "result/$url.csv"
done < "doh_list"
#done < "popular_doh"
exit 0

tcpdump -i enp0s3 -s0 -w data/baseline.pcap &
sleep 0.3
python3 -c "import query; query.baseline()"
sleep 1
kill $(pgrep tcpdump)
python3 parser.py --filename data/baseline.pcap --output_filename result/baseline.csv

exit 0


tcpdump -i enp0s3 -s0 -w data/verify.pcap &
python3 -c "import query; query.verify()"
kill $(pgrep tcpdump)
python3 parser.py --filename data/verify.pcap --output_filename result/verify.csv

tcpdump -i enp0s3 -s0 -w data/unverify.pcap &
python3 -c "import query; query.unverify()"
kill $(pgrep tcpdump)
python3 parser.py --filename data/unverify.pcap --output_filename result/unverify.csv
