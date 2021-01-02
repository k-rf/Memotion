from dataclasses import dataclass


@dataclass
class Memory:
    content: str

    def __post_init__(self):
        if self.content is None:
            raise ValueError

        if len(self.content.strip()) == 0:
            raise ValueError
