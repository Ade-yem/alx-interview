#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys


def print_stats(file_size, stats):
    """prints the stats"""
    print(f"File size: {file_size}")
    for k, v in stats.items():
        if stats[k] > 0:
            print(f"{k}: {v}")
        stats[k] = 0


def main():
    """entry point"""
    file_size = 0
    count = 0
    stats = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            line = line.split()
            if len(line) != 9:
                continue
            code = line[7]
            if code in stats.keys():
                stats[code] += 1
            file_size += int(line[8])
            count += 1
            if count > 0 and count % 10 == 0:
                print_stats(file_size, stats)
    except (IndexError, KeyboardInterrupt) as e:
        print_stats(file_size, stats)


if __name__ == "__main__":
    main()