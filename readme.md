# Most Active Cookie

This project is a command-line tool that processes a cookie log file to find the most active cookie for a specified day. It is written in Python and includes comprehensive error handling, logging, and unit tests.

## Features

- Parses a cookie log file and finds the most active cookie(s) for a given date.
- Supports logging for better traceability and debugging.
- Includes unit tests to verify functionality.

## Requirements

- Python 3.6 or higher

## Usage

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/smellycattt/quantCast.git
   cd quantCast
   ```

2. Run the command-line tool:
    ```python most_active_cookie.py -f <cookie_log_file> -d <date>
    ```
for ex:

    ```python most_active_cookie.py -f cookie_log.csv -d 2018-12-09
    ```

3. Logging 
You can set the logging level using the -l or --log parameter. Available options are DEBUG, INFO, WARNING, ERROR, and CRITICAL. The default logging level is INFO.

Example:  
    ``` python most_active_cookie.py -f cookie_log.csv -d 2018-12-09 -l DEBUG
    ```

4. Testing:
    ```python -m unittest test_most_active_cookie.py
    ```
