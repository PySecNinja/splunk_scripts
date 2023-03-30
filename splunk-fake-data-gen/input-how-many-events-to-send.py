'''
USAGE - The script is a Python program that submits fake events to a Splunk 
        instance. It uses the Splunk SDK to connect to a Splunk service, then 
        prompts the user to input the number of events they want to send to 
        Splunk. It then generates fake data using the Faker library, 
        constructs an event payload with a timestamp and the fake data, 
        and submits the event payload to Splunk. The program repeats this 
        process for the specified number of events and prints a message when 
        each event is submitted and when all events have been submitted.

AUTHOR - https://github.com/Ahendrix9624
'''
# Import required libraries
import os
import splunklib.client as client
import splunklib.results as results
import time
import json
from faker import Faker

# Set connection parameters using environmental variables
HOST = "localhost"
PORT = "8089"
USERNAME = os.environ.get('SPLUNK_USERNAME')
PASSWORD = os.environ.get('SPLUNK_PASSWORD')

# Set constants for index, sourcetype, and source
INDEX_NAME = 'main'
SOURCETYPE = 'mysourcetype'
SOURCE = 'mysource'

# Create a Faker object for generating fake data
fake = Faker()

# Set constants for key-value pairs
FIELD1_KEY = 'host'
FIELD1_VALUE = fake.hostname()
FIELD2_KEY = 'network'
FIELD2_VALUE = fake.word()

# Connect to the Splunk service using the parameters set above
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

# Prompt the user to input how many times they want to run the script
num_events = int(input("How many events do you want to send to splunk? "))

# Loop over the number of runs and submit events to Splunk
for event in range(num_events):
    # Define the event payload with a timestamp and fake data
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

    # Get the index object for the specified index name
    index = service.indexes[INDEX_NAME]

    # Convert the event payload to JSON format
    json_payload = json.dumps(event_payload)

    # Submit the event to the Splunk index using the index object
    index.submit(json_payload)

    print(f"Event {event+1} submitted to Splunk.")

print(f"All {num_events} events submitted to Splunk.")
