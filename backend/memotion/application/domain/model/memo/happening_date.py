from dataclasses import dataclass

from pendulum.datetime import DateTime


@dataclass
class HappeningDate:
    value: DateTime
