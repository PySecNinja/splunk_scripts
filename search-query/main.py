'''
USAGE - This Python script connects to a Splunk instance using the Splunk 
        SDK for Python and runs a search query to retrieve log data. The search 
        query is defined by the search_query variable. The script then retrieves 
        the results of the search and prints them to the console.

        To connect to the Splunk instance, the script uses the client.connect() 
        method, passing in the hostname, port, username, and password of the 
        Splunk instance.

        The script then creates a search job using the service.jobs.create() 
        method and passes in the search query. The while loop checks the 
        status of the search job until it's completed. The status of the 
        search job is printed to the console while it's running.

        Finally, the script retrieves the search results using the 
        results.JSONResultsReader() method and iterates over each result, 
        printing it to the console.

        This script is just an example and should be tailored to meet specific 
        requirements, such as modifying the search query, processing the 
        search results in a specific way, or sending the results to another 
        system for further processing.

AUTHOR - AUTHOR - https://github.com/Ahendrix9624
'''

import splunklib.client as client
import splunklib.results as results
import os
import time

# Define the search criteria
search_query = "search index=main | stats count by source"

# Set connection parameters using environmental variables
HOST = "localhost"
PORT = "8089"
USERNAME = os.environ.get('SPLUNK_USERNAME')
PASSWORD = os.environ.get('SPLUNK_PASSWORD')

# Connect to Splunk instance
service = client.connect(
    host = HOST,
    port = PORT,
    username = USERNAME,
    password = PASSWORD)

# Run the search and retrieve the results
job = service.jobs.create(search_query)
while True:
    while not job.is_ready():
        pass
    stats = {"isDone": job["isDone"],
            "doneProgress": float(job["doneProgress"]) * 100,
            "scanCount": int(job["scanCount"]),
            "eventCount": int(job["eventCount"]),
            "resultCount": int(job["resultCount"])}
    status = ("\r%(doneProgress)03.1f%%   %(scanCount)d scanned   "
            "%(eventCount)d matched   %(resultCount)d results") % stats
    print(status)
    if stats["isDone"] == "1":
        print("\nDone!")
        break
    time.sleep(2)

# Parse the results
reader = results.JSONResultsReader(job.results(output_mode="json"))
for result in reader:
    print(result)
