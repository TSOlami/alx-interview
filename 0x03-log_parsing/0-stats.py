#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics based on the provided input format.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesnt appear or is not an integer,
dont print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys


total_size = 0  # Initialize the total file size to 0

# Store the count of all status codes in a dictionary
status_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

count = 0  # Keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        # Check if the line follows the expected format
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code received exists in the dictionary and increment its count
            if status_code in status_count.keys():
                status_count[status_code] += 1

            # Update total size
            total_size += file_size

            # Update count of lines
            count += 1

        # If count reaches 10, print statistics and reset count
        if count == 10:
            count = 0  # Reset count
            print('File size: {}'.format(total_size))

            # Print status code counts
            for key, value in sorted(status_count.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    # Print final statistics after loop completion or interruption
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_count.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
