#!/usr/bin/python3

import sys  # Import the sys module for standard input and output operations

def print_stats(total_size, status_count):
    # Function to print the calculated statistics
    print("File size: {}".format(total_size))  # Print the total file size
    sorted_status_codes = sorted(status_count.keys())  # Get the sorted status codes
    for code in sorted_status_codes:
        count = status_count[code]
        print("{}: {}".format(code, count))  # Print each status code and its count

def main():
    total_size = 0  # Initialize the total file size to 0
    status_count = {}  # Initialize a dictionary to store status code counts

    try:
        for idx, line in enumerate(sys.stdin, 1):
            # Loop through each line from standard input and enumerate line numbers

            split_line = line.split()  # Split the line into words
            if len(split_line) < 9:
                continue  # Skip lines with less than 9 words

            status_code = split_line[-2]  # Get the status code from the second-to-last word
            file_size = int(split_line[-1])  # Get the file size from the last word

            if status_code.isdigit():  # Check if status code is a digit
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    # Check if status code is one of the specified values
                    total_size += file_size  # Add the file size to the total
                    status_count[status_code] = status_count.get(status_code, 0) + 1
                    # Increment the count for the corresponding status code

            if idx % 10 == 0:
                # After every 10 lines, print the statistics so far
                print_stats(total_size, status_count)

        print_stats(total_size, status_count)
        # Print the final statistics at the end of the input
        
    except KeyboardInterrupt:
        # Handle the case of keyboard interruption (CTRL + C)
        print_stats(total_size, status_count)
        # Print the current statistics when the interruption occurs

if __name__ == "__main__":
    main()  # Call the main function if the script is run directly