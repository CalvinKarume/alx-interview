#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

import sys

CACHE = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
TOTAL_SIZE = 0
COUNTER = 0


def process_line(line):
    """Process a single log line"""
    line_list = line.split(" ")
    if len(line_list) > 4:
        code = line_list[-2]
        size = int(line_list[-1])
        if code in CACHE:
            CACHE[code] += 1
        globals()['TOTAL_SIZE'] += size
        globals()['COUNTER'] += 1


def print_statistics():
    """Print metrics every 10 lines or on interruption"""
    print('File size: {}'.format(TOTAL_SIZE))
    for key, value in sorted(CACHE.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            process_line(line)
            if COUNTER == 10:
                COUNTER = 0
                print_statistics()

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics()

