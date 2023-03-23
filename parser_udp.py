import csv

import click
import numpy as np
from scapy.all import *


@click.command()
@click.option("--filename", default="test.pcap")
@click.option("--output_filename", default="test.csv")
def main(filename: str, output_filename: str):
    pf = rdpcap(filename)

    times = []
    for pkt in pf:
        if IP in pkt:
            times.append(pkt.time)
    times = np.array(times)
    duration = times[1::2] - times[::2]

    with open(output_filename, "w") as f:
        w = csv.writer(f)
        w.writerow(["Duration"])
        for d in duration:
            w.writerow([d])


if __name__ == "__main__":
    main()
