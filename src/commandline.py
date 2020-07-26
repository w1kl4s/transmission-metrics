import json
import argparse

from src import main 

def start():
    parser = argparse.ArgumentParser(description="Run transmission metrics daemon/exporter")
    parser.add_argument("-c", "--config", metavar='CONFIG', required=True, help='Config file location')
    parser.add_argument("-m", "--mode", metavar="MODE", action='store', default='pull', help='Runtime mode')
    parser.add_argument("-p", "--port", metavar="port", action='store', type=int, default=8888, help='Port for Prom server to listen on')
    parser.add_argument("-a", "--address", metavar="address", action='store', default='0.0.0.0', help='Address for Prom server to listen on')
    parser.add_argument("-i", "--interval", metavar="interval", action='store', type=int, default=30, help='Interval between Transmission RPC scrapes')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        clients = json.load(f)
    
    if args.mode == "pull":
        main.start_prom_server(clients, args.address, args.port, args.interval)
