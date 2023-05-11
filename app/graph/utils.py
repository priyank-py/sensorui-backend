from influxdb_client import InfluxDBClient
import os
from datetime import datetime
import pytz

def get_client():
    """ Load temp's data

    Parameters:
    -  db object
    """

    token = os.environ.get('INFLUX_TOKEN')
    org = "Priyank"
    url = "http://127.0.0.1:8086"

    client = InfluxDBClient(url=url, token=token, org=org)

    query_api = client.query_api()

    return query_api


def get_datetime(str_date):
    if str_date.isnumeric():
        try:
            return datetime.fromtimestamp(int(str_date) / 1000).astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except: 
            return ""