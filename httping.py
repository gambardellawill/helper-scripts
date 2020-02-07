# -*- coding: utf-8 -*-

import time
import requests
import argparse

parser = argparse.ArgumentParser('httping: allows the user to make requests to HTTP/S servers ping-style.')

parser.add_argument('-c', '--count', dest='count', type=int, required=False, help='', default=-1)
parser.add_argument('-i', '--interval', dest='interval', type=int, required=False, help='', default=1)
parser.add_argument("host", type=str)


def httping(host):
    response = requests.get(host)
    print("{}: got {} and took {} seconds to complete.".format(host, response.status_code, response.elapsed))


if __name__ == "__main__":
    args = parser.parse_args()

    if args.count == -1:
        try:
            while True:
                httping(args.host)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            exit(0)
    else:
        for tick in range(0, args.count):
            httping(args.host)
            time.sleep(args.interval)