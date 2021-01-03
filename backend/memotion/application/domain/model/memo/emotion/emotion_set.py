from dataclasses import dataclass


from .emotion import Emotion


@dataclass
class EmotionSet:
    emotions: set[Emotion]

    def __len__(self):
        return len(self.emotions)

    def __post_init__(self):
        self.__validate(self.emotions)

    @staticmethod
    def __validate(value: set[Emotion]):
        if len(value) == 0:
            raise ValueError("Emotion is empty.")

        oppositions = [e.opposition for e in value]
        if value.intersection(oppositions) != set():
            raise ValueError("Opposition emotions are existed.")

    @classmethod
    def instance(cls, value: set[Emotion]):
        return cls(value)

    def clone(self):
        return self.instance(set(self.emotions))
