#!/usr/bin/python3
"""Module containing script that reads stdin and computes metrics"""
import sys


def update_metrics(line, status_codes, total_size):
    """Updates the metrics based on a line of log data.

    Args:
        line (str): A line from the log.
        status_codes (dict): A dictionary
        holding the count of status codes.
        total_size (int): The current total size of files processed.

    Returns:
        int: The updated total size of files processed.
    """
    lines = line.split(" ")
    if len(lines) > 4:
        code = lines[-2]
        size = int(lines[-1])
        if code in status_codes:
            status_codes[code] += 1
        total_size += size
    return total_size


def print_statistics(total_size, status_codes):
    """Prints the statistics of the log data.

    Args:
        total_size (int): The total size of files processed.
        status_codes (dict): A dictionary holding the count of status codes.
    """
    print("File size: {}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


def main():
    """Main function that reads from stdin and computes metrics."""
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    total_size = 0
    total_num = 0

    try:
        for line in sys.stdin:
            total_size = update_metrics(line, status_codes, total_size)
            total_num += 1
            if total_num == 10:
                total_num = 0
                print_statistics(total_size, status_codes)
    except Exception:
        pass
    finally:
        print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
