from dataclasses import dataclass
from typing import Union

from pendulum.datetime import DateTime


@dataclass
class WritingDate:
    value: DateTime

    def add_hours(self, hours: int):
        return self.value.add(hours=hours)
