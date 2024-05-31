import argparse
import logging
from collections import defaultdict
from datetime import datetime

def setup_logging(log_level=logging.INFO):
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Find the most active cookie for a specific day.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Filename of the cookie log file')
    parser.add_argument('-d', '--date', type=str, required=True, help='Date to find the most active cookie (format: YYYY-MM-DD)')
    parser.add_argument('-l', '--log', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='Set the logging level')
    return parser.parse_args()

def process_log_file(filename, date):
    """
    Processes the cookie log file and returns the most active cookies for the specified date.

    Args:
        filename (str): The path to the log file.
        date (str): The date to find the most active cookies (format: YYYY-MM-DD).

    Returns:
        list: A list of the most active cookies for the specified date.
    """
    cookie_counts = defaultdict(int)
    target_date = datetime.strptime(date, '%Y-%m-%d').date()

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines[1:]:  # Skip the header row
            cookie, timestamp = line.strip().split(',')
            log_date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z').date()
            if log_date == target_date:
                cookie_counts[cookie] += 1
    except FileNotFoundError:
        logging.error("File not found: {}".format(filename))
        return []
    except ValueError as e:
        logging.error("Value error: {}".format(e))
        return []
    except Exception as e:
        logging.error("An error occurred: {}".format(e))
        return []

    max_count = max(cookie_counts.values(), default=0)
    most_active_cookies = [cookie for cookie, count in cookie_counts.items() if count == max_count]

    return most_active_cookies

def main():
    args = parse_arguments()
    setup_logging(log_level=getattr(logging, args.log))

    logging.info("Processing log file: {} for date: {}".format(args.file, args.date))
    most_active_cookies = process_log_file(args.file, args.date)

    if most_active_cookies:
        logging.info("Most active cookies found: {}".format(most_active_cookies))
        for cookie in most_active_cookies:
            print(cookie)
    else:
        logging.info("No cookies found for the specified date.")

if __name__ == '__main__':
    main()
