# CRM Campaign Top Songs

This solution is designed to compute the top 50 songs most listened to in each country and, optionally, the top 50 songs most listened to by each user in the last 7 days as part of a CRM campaign.

## Requirements

- Python (3.6 or above)

## Installation

download the source code files.

Install the required Python dependencies using the following command in your shell:
pip install python 3.x

Configure the necessary parameters in the script:

LOGS_FOLDER: Path to the directory containing the log files.
OUTPUT_FOLDER: Path to the directory where the output files will be saved.


Run the script using the following command:
pip3 test_top50.py
The script will process the log files for the current day and generate the following output files in the specified OUTPUT_FOLDER:

country_top50_YYYYMMDD.txt: Contains the top 50 songs most listened to in each country.
user_top50_YYYYMMDD.txt : Contains the top 50 songs most listened to by each user.
