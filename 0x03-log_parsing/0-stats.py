#!/usr/bin/python3
""" Log parsing """
import sys


def parse_line(line):
    """Parse a log line and extract relevant information"""
    parts = line.split()
    if len(parts) == 9:
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit() and file_size.isdigit():
            return ip_address, int(status_code), int(file_size)
    return None, None, None


def print_statistics(total_file_size, status_codes):
    """Print the total file size and number of lines by status code"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def process_logs():
    """Process log lines from stdin and compute statistics"""
    total_file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    lines_processed = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line)

            if ip_address is not None:
                total_file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)
    print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    process_logs()
