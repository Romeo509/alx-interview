#!/usr/bin/python3
import sys
from collections import defaultdict


def parse_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None

    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])

    try:
        status_code_int = int(status_code)
    except ValueError:
        return None

    allowed_status_codes = {'200', '301', '400', '401',
                            '403', '404', '405', '500'}
    if status_code not in allowed_status_codes:
        return None

    return (status_code, file_size)


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")

    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            parsed = parse_line(line)

            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
