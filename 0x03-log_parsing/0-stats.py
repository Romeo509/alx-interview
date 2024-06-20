#!/usr/bin/python3
"""Module containing script that reads stdin and computes metrics"""
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
total_num = 0

try:
    for line in sys.stdin:
        lines = line.split(" ")

        if len(lines) > 4:
            code = lines[-2]
            size = int(lines[-1])

            if code in status_codes.keys():
                status_codes[code] += 1

            total_size += size
            total_num += 1

        if total_num == 10:
            total_num = 0
            print("File size: {}".format(total_size))

            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print("{}: {}".format(k, v))

except Exception:
    pass

finally:
    print("File size: {}".format(total_size))

    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))
