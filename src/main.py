import socket
from ipaddress import ip_address 

from src import Collector 
from src import PrometheusServer

def start_prom_server(clients, address, port, interval):
    collectors = Collector.start_collectors(clients, interval)
    server = PrometheusServer.Metrics((address, port), collectors)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        for collector in collectors:
            collector.exit.set()
        server.shutdown()

def start_influx_client(mode):
    pass

