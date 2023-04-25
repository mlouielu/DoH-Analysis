FROM ubuntu:20.04

RUN apt update && apt install tzdata -y
ENV TZ="America/New_York"

RUN apt-get install -y python3 python3-pip tcpdump firefox curl iproute2

# Install chrome
RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

WORKDIR /app

RUN mkdir -p result

RUN pip install cryptography
RUN pip install selenium

#COPY . run.sh parser.py query.py analyze.py doh.py doh_ip doh_list doh_only_ip doh_quote_ip extract_doh.sh LICENSE meter parser_udp.py popular_doh README.md requirements.txt run_udp.sh /app/
COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["./run.sh"]
