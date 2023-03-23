from collections import defaultdict

import click
from scapy.all import *

from meter import flow_session

IP_LIST = ["192.168.88.195", "127.0.0.1"]
IP_LIST.extend([s.strip() for s in open("doh_only_ip")])


def old():
    pf = rdpcap(filename).sessions()

    streams = defaultdict()
    for pkt in pf:
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst

            if src_ip not in IP_LIST or dst_ip not in IP_LIST:
                continue

            # Check if the packet has TCP or UDP layer
            if TCP in pkt:
                src_port = pkt[TCP].sport
                dst_port = pkt[TCP].dport
                print(dir(pkt[TCP]))
                streams[pkt[TCP].stream].append(pkt)

            elif UDP in pkt:
                src_port = pkt[UDP].sport
                dst_port = pkt[UDP].dport
            else:
                src_port = "N/A"
                dst_port = "N/A"

            print(
                f"{pkt.time} - Source IP: {src_ip}, Destination IP: {dst_ip}, Source Port: {src_port}, Destination Port: {dst_port}"
            )

    print(streams)


@click.command()
@click.option("--filename", default="test.pcap")
@click.option("--output_filename", default="test.csv")
def main(filename: str, output_filename: str):
    NewFlowSession = flow_session.generate_session_class("flow", output_filename)
    s = sniff(
        offline=filename,
        session=NewFlowSession,
        filter="tcp or udp and (src or dst host %s)" % " or ".join(IP_LIST),
    )


if __name__ == "__main__":
    main()
