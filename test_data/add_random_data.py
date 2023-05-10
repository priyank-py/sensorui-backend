
import random
import time
from datetime import datetime, timedelta
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "34S5Pm8iQDQ2PeLmdJefEc0MYhuEtFiNpaq8zvVCohR20P7XCa0qpya2gjFOcJjBNs3yegvz1ZKdUatGdngCPQ=="
org = "Priyank"
url = "http://127.0.0.1:8086"

client = InfluxDBClient(url=url, token=token, org=org)
bucket = "weather"

write_api = client.write_api(write_options=SYNCHRONOUS)

def add_temperature():
    value = round(random.uniform(15.8, 28.9), 2)
    print(value, record_date)
    point = (
        Point("temperature")
        .tag("source", "random")
        .field("value", value)
        # .field("_start", time.mktime(record_date.timetuple()))
        # .field("_end", time.mktime((record_date + timedelta(minutes=30)).timetuple()))
    )
    write_api.write(bucket=bucket, org="Priyank", record=point)

def add_precipitation():
    value = round(random.uniform(11, 15), 2)
    print(value, record_date)
    point = (
        Point("precipitation")
        .tag("source", "random")
        .field("value", value)
        # .field("_start", time.mktime(record_date.timetuple()))
        # .field("_end", time.mktime((record_date + timedelta(minutes=30)).timetuple()))
    )
    write_api.write(bucket=bucket, org="Priyank", record=point)

def add_humidity():
    value = round(random.uniform(23, 60), 2)
    print(value, record_date)
    point = (
        Point("humidity")
        .tag("source", "random")
        .field("value", value)
        # .field("_start", time.mktime(record_date.timetuple()))
        # .field("_end", time.mktime((record_date + timedelta(minutes=30)).timetuple()))
    )
    write_api.write(bucket=bucket, org="Priyank", record=point)

def add_wind_speed():
    value = round(random.uniform(3, 17), 2)
    print(value, record_date)
    point = (
        Point("wind_speed")
        .tag("source", "random")
        .field("value", value)
        # .field("_start", time.mktime(record_date.timetuple()))
        # .field("_end", time.mktime((record_date + timedelta(minutes=30)).timetuple()))
    )
    write_api.write(bucket=bucket, org="Priyank", record=point)

record_date = datetime.now()
td = timedelta(hours=1)
while True:
    
    add_temperature()
    add_precipitation()
    add_humidity()
    add_wind_speed()

    time.sleep(1) # separate points by 1 second