#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

def print_statistics(total_size, status_codes):
    print("File size:", total_size)
    for status_code, count in sorted(status_codes.items()):
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            line = line.strip()
            parts = line.split()
            if len(parts) != 9 or parts[6].isdigit() is False:
                continue
            
            ip_address, _, _, _, _, request, status_code, file_size = parts
            if request != '"GET /projects/260 HTTP/1.1"':
                continue

            total_size += int(file_size)

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if i % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
