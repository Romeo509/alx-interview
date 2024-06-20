#!/usr/bin/python3

import sys
import re
import signal

LOG_PATTERN = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r' - \[(.*?)\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3})'
    r' (\d+)$'
)
total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def parse_log_line(line):
    ''' Parse a log line and extract status code and file size '''
    match = LOG_PATTERN.match(line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return status_code, file_size
    else:
        return None, None


def print_statistics(total_size, status_counts):
    ''' Print current statistics '''
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    ''' Handle interrupt signal (CTRL + C) '''
    print_statistics(total_size, status_counts)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    line = line.strip()

    status_code, file_size = parse_log_line(line)

    if status_code is not None and file_size is not None:
        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)
