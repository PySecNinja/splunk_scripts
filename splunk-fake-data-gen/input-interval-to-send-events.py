'''
USAGE - The script is a Python program that submits fake events to a Splunk 
        instance at regular intervals. It uses the Splunk SDK to connect to a 
        Splunk service, then prompts the user to input the number of minutes 
        between each event submission. It then generates fake data using the 
        Faker library, constructs an event payload with a timestamp and the 
        fake data, and submits the event payload to Splunk. The program repeats 
        this process indefinitely, with a pause between each event submission 
        equal to the specified number of minutes. The program prints a message 
        when each event is submitted.

AUTHOR - https://github.com/Ahendrix9624
'''
# Import required libraries
import os
import splunklib.client as client
import splunklib.results as results
import time
import json
from faker import Faker

# Create a Faker object to generate fake data
fake = Faker()

# Set connection parameters using environmental variables
HOST = "localhost"
PORT = "8089"
USERNAME = os.environ.get('SPLUNK_USERNAME')
PASSWORD = os.environ.get('SPLUNK_PASSWORD')

# Set constants for index, sourcetype, and source
INDEX_NAME = 'main'
SOURCETYPE = 'mysourcetype'
SOURCE = 'mysource'

# Set constants for key-value pairs
FIELD1_KEY = 'host'
FIELD1_VALUE = fake.hostname()
FIELD2_KEY = 'network'
FIELD2_VALUE = fake.word()

# Prompt the user for the number of minutes between each event submission
interval_minutes = int(input("Enter the number of minutes between each event submission: "))

# Connect to the Splunk service using the parameters set above
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

# Get the index object for the specified index name
index = service.indexes[INDEX_NAME]

while True:
    # Define the event payload with a timestamp
    event_payload = {
        'index': INDEX_NAME, 
        'sourcetype': SOURCETYPE, 
        'source': SOURCE, 
        'event': {
            '_time': int(time.time()), # timestamp in epoch time
            FIELD1_KEY: FIELD1_VALUE, 
            FIELD2_KEY: FIELD2_VALUE
            }
        }

    # Convert the event payload to JSON format
    json_payload = json.dumps(event_payload)

    # Submit the event to the Splunk index using the index object
    index.submit(json_payload)

    # Print a countdown timer displaying how much time is left before the next event sends
    print(f"Event submitted to Splunk. Next event in {interval_minutes} minute(s).")
    for i in range(interval_minutes * 60, 0, -1):
        print(f"\rNext event in {i // 60} minute(s) and {i % 60} second(s).", end="")
        time.sleep(1)
    print("\r", end="")

