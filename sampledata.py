from datetime import datetime
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# Define InfluxDB settings
influxdb_url = "http://10.14.0.42:8086"
influxdb_token = "<your-influxdb-token>"
influxdb_org = "<your-influxdb-org>"
influxdb_bucket = "<your-influxdb-bucket>"

# Connect to the InfluxDB client and get a write API
client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Define the measurement and tags for the data
measurement = "temperature"
location_tag = "location"
location_value = "room1"

# Generate random temperature data and write it to InfluxDB
while True:
    # Generate a random temperature reading between 20 and 30 degrees Celsius
    temperature_value = random.uniform(20, 30)

    # Get the current time in UTC
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct the data point
    data_point = f"{measurement},{location_tag}={location_value} value={temperature_value} {current_time}"

    # Write the data point to InfluxDB
    write_api.write(influxdb_bucket, record=data_point)

    # Wait for 1 second before generating the next data point
    time.sleep(1)
