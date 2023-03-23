from collections import defaultdict

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def udp_timeline():
    keys = [
        # "cloudflare-dns.com",
        # "mozilla.cloudflare-dns.com",
        "dns.google",
        # "dns.quad9.net",
        #        "dns.adguard.com",
    ]

    udps = []

    for k in keys:
        try:
            df = pd.read_csv(f"result/{k}.csv", header=0)
        except pd.errors.EmptyDataError:
            remove.append(k)
            continue

        plt.plot(df["Duration"][1:], label=f"{k} (DoH)")
        for i in range(3):
            print(f'{df["Duration"][i::3].mean():.4f}')

        for ip in df["DestinationIP"].unique():
            df = pd.read_csv(f"result/udp_{ip}.csv")
            plt.plot(df["Duration"][1:], ls="--", label=f"{ip} (UDP)")

    plt.ylim(0, 0.5)
    plt.ylabel("Duration (s)")
    plt.legend(ncol=4)
    plt.show()


def timeline():
    keys = ["baseline", "unverify", "verify"]
    keys = [
        "baseline",
        "cloudflare-dns.com",
        "mozilla.cloudflare-dns.com",
        "dns.google",
        "dns.quad9.net",
        "dns.adguard.com",
    ]

    for k in keys:
        try:
            df = pd.read_csv(f"result/{k}.csv", header=0)
        except pd.errors.EmptyDataError:
            remove.append(k)
            continue

        plt.plot(df["Duration"], label=k)

    plt.ylabel("Duration (s)")
    plt.ylim(0, 0.5)
    plt.xlim(0, 300)
    plt.legend(ncol=3)
    plt.show()


def main():
    # keys = [s.strip() for s in open("doh_list").readlines()[:18]]
    keys = [
        "cloudflare-dns.com",
        "mozilla.cloudflare-dns.com",
        "dns.google",
        "dns.quad9.net",
        "dns.adguard.com",
        "freedns.controld.com",
    ]
    keys = ["baseline", "unverify", "verify"]
    #    keys = ["baseline"]
    means = defaultdict(list)
    norm_means = defaultdict(list)

    remove = []
    for k in keys:
        try:
            df = pd.read_csv(f"result/{k}.csv", header=0)
        except pd.errors.EmptyDataError:
            remove.append(k)
            continue

        a = df[::3]
        b = df[1::3]
        c = df[2::3]

        means["total"].append(df["Duration"].mean())
        means["louie.lu"].append(a["Duration"].mean())
        means["google.com"].append(b["Duration"].mean())
        means["cs.unc.edu"].append(c["Duration"].mean())
        norm_means["total"].append(
            df["Duration"].mean() - df["ResponseTimeTimeMean"].mean()
        )
        norm_means["louie.lu"].append(
            a["Duration"].mean() - a["ResponseTimeTimeMean"].mean()
        )
        norm_means["google.com"].append(
            b["Duration"].mean() - b["ResponseTimeTimeMean"].mean()
        )
        norm_means["cs.unc.edu"].append(
            c["Duration"].mean() - c["ResponseTimeTimeMean"].mean()
        )

    for r in remove:
        keys.remove(r)

    x = np.arange(len(keys))
    width = 0.2
    multiplier = 0

    fig, ax = plt.subplots(layout="constrained")
    for attr, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attr)
        ax.bar_label(rects, padding=15, rotation=60, fmt="%.4f")
        multiplier += 1

    ax.set_ylabel("Time (s)")
    ax.set_xticks(x + width, keys)
    ax.legend(loc="upper left", ncol=4)
    ax.set_ylim(0, 0.22)
    plt.xticks(rotation=45)
    plt.show()

    multiplier = 0
    fig, ax = plt.subplots(layout="constrained")
    for attr, measurement in norm_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attr)
        ax.bar_label(rects, padding=15, rotation=60, fmt="%.4f")
        multiplier += 1

    ax.set_ylabel("Time (s)")
    ax.set_xticks(x + width, keys)
    ax.legend(loc="upper left", ncol=4)
    #    ax.set_ylim(0.12, 0.32)
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    # main()
    # timeline()
    udp_timeline()
