'''
USAGE - This script sends an event payload to a Splunk index using the 
        Splunk SDK for Python. It uses environmental variables to set 
        the connection parameters for the Splunk service, including 
        the host, port, username, and password. The script defines 
        constants for the index, sourcetype, and source, as well as 
        for key-value pairs to include in the event payload. The 
        payload includes a timestamp, and the script converts the 
        payload to JSON format before submitting it to the Splunk 
        index. Finally, the script prints a message indicating that 
        the event has been submitted to Splunk.

AUTHOR - https://github.com/Ahendrix9624
'''
# Import required libraries
import os
import splunklib.client as client
import splunklib.results as results
import time
import json

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
FIELD1_VALUE = 'dell-cm-250'
FIELD2_KEY = 'network'
FIELD2_VALUE = 'sales'

# Connect to the Splunk service using the parameters set above
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

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

# Get the index object for the specified index name
index = service.indexes[INDEX_NAME]

# Convert the event payload to JSON format
json_payload = json.dumps(event_payload)

# Submit the event to the Splunk index using the index object
index.submit(json_payload)

print("Event submitted to Splunk.")
