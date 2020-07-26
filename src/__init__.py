# TODO Probably a pretty shitty place for this, should move it somewhere
from dataclasses import dataclass

@dataclass
class Metric:
    prefix: str
    value_name: str
    labels: dict
    value: float
    def format_prom(self) -> str:
        labels = ','.join(x + '=' + '"' + self.labels[x] + '"' for x in self.labels.keys())
        return f"{self.prefix}_{self.value_name}{{{labels}}} {self.value}"
