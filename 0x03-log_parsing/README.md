0x03. Log Parsing
Project Overview

This project involves creating a Python script to parse HTTP request logs in real-time. The script reads log entries from standard input, extracts specific metrics, and prints these metrics periodically. The focus is on parsing data streams, processing logs, and computing statistics efficiently.
Key Features

    Real-time Log Parsing: The script reads HTTP request logs line-by-line from standard input.
    Metric Computation: It computes the total file size and counts the occurrences of various HTTP status codes.
    Periodic Reporting: The script prints metrics after every 10 lines of input or upon receiving a keyboard interrupt (CTRL + C).
    Error Handling: The script gracefully handles unexpected input formats and interruptions.

Usage

To run the script, use the following command:

bash

./0-generator.py | ./0-stats.py

Where 0-generator.py is a script that generates random HTTP request logs, and 0-stats.py is your log parsing script.
Input Format

The script expects log entries in the following format:

php

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    IP Address: The IP address of the client making the request.
    Date: The date and time of the request.
    Request: The HTTP request line.
    Status Code: The HTTP status code returned by the server.
    File Size: The size of the file returned to the client.

Example Output

After processing every 10 lines or upon receiving a keyboard interrupt, the script prints:

arduino

File size: <total size>
<status code>: <number>

For example:

yaml

File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3

Key Concepts
File I/O in Python

The script reads from sys.stdin line-by-line to handle real-time data input efficiently.
Signal Handling in Python

The script uses a try-except block to handle keyboard interruptions (CTRL + C), ensuring metrics are printed even if the script is interrupted.
Data Processing

The script parses each log entry to extract the IP address, date, request, status code, and file size, and then updates the relevant metrics.
Regular Expressions

Regular expressions are used to validate and extract data from each log entry.
Dictionaries in Python

Dictionaries are used to count occurrences of each status code and to accumulate the total file size.
Exception Handling

The script includes error handling to manage unexpected input formats and ensure robust execution.
License

This project is licensed under the terms of the MIT license.
