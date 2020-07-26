import socket
from ipaddress import ip_address
from http.server import HTTPServer,BaseHTTPRequestHandler

class Metrics(HTTPServer):    
    def __init__(self, address, collectors):
        if ip_address(address[0]).version == 6: 
            self.address_family = socket.AF_INET6
        self.collectors = collectors 
        super().__init__(address, self.RequestHandler)

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/metrics":
                return self.send_error(404)

            metrics = []
            for collector in self.server.collectors:
                for metric in collector.get_metrics():
                    metrics.append(metric.format_prom())

            output = '\n'.join(metrics) + '\n'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(output.encode())
