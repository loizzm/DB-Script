#!/usr/bin/python3
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "ireliontt@gmail.com"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="<BUCKET>"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(26,31):
  point = (
    Point("Medições")
    .tag("sensor", "tagvalue1")
    .field("Temperatura", value)
  )
  write_api.write(bucket=bucket, org="ireliontt@gmail.com", record=point)
  time.sleep(1) # separate points by 1 second