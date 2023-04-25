FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip tcpdump



WORKDIR /app

RUN mkdir -p result

RUN pip install cryptography

COPY . run.sh parser.py query.py analyze.py data doh.py doh_ip doh_list doh_only_ip doh_quote_ip extract_doh.sh LICENSE meter parser_udp.py popular_doh README.md requirements.txt run_udp.sh /app/ 

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["./run.sh"]
