from influxdb_client import InfluxDBClient
import os

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
