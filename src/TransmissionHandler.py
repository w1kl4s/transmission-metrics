import requests
import json

class Client():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.session = requests.Session()
        self.session.auth = (self.user, self.password)
        self.set_session()

    def set_session(self):
        try:
            r = self.session.post(self.url)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            return None 

        try:
            self.session.headers['X-Transmission-Session-Id'] = r.headers['X-Transmission-Session-Id']
        except KeyError:
            return None

    def get_session_stats(self):

        data = '{"method": "session-stats"}'
        try: 
            r = self.session.post(self.url, data=data, timeout=20)
            return json.loads(r.text)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            return None
