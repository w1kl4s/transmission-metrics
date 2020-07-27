import time
import random
import threading
from collections import MutableMapping

from src import Metric 
from src import TransmissionHandler

class CollectorThread(threading.Thread):
    def __init__(self, instance, interval):
        threading.Thread.__init__(self)
        self.exit = threading.Event()

        self.instance = instance
        self.metrics = None
        self.interval = interval 

    def get_metrics(self):
        return self.metrics

    def _flatten(self, d, parent_key='', sep='-'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, MutableMapping):
                items.extend(self._flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def _parse_session_stats(self, session_stats):
        if session_stats['result'] != 'success':
            #TODO: Raise an exception in the future, that shouldn't happen
            return None 

        data = self._flatten(session_stats['arguments'])

        prefix = "transmission_session"
        instance = self.instance['name']
        mapping = {
                'torrentCount': 'total_torrent_count',
                'activeTorrentCount': 'active_torrent_count',
                'cumulative-stats-downloadedBytes': 'downloaded_bytes',
                'cumulative-stats-uploadedBytes': 'uploaded_bytes',
                'cumulative-stats-filesAdded': 'total_files_count',
                'current-stats-secondsActive': 'uptime'
        }
        return [Metric(prefix, y, {'instance': instance}, data[x]) for x, y in mapping.items()]
        
    def run(self):
        client = TransmissionHandler.Client(
                        url = self.instance['url'],
                        user=self.instance['user'],
                        password=self.instance['password']
                    )
        while not self.exit.is_set(): 
            session_stats = client.get_session_stats()
            self.metrics = self._parse_session_stats(session_stats)
            self.exit.wait(self.interval)


def start_collectors(instances, interval):
    collectors = []
    for instance in instances:
        collector = CollectorThread(instance, interval)
        collector.start()
        collectors.append(collector)
    return collectors
