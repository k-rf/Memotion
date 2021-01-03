from dataclasses import dataclass, field
from typing import NoReturn, SupportsAbs

from .emotion_category import EmotionCategory
from .emotion_name import EmotionName


@dataclass(frozen=True)
class Emotion:
    name: EmotionName = field(init=False)
    category: EmotionCategory = field(init=False)

    @property
    def opposition(self):
        mapper = {
            EmotionName.JOY: Sadness(),
            EmotionName.SADNESS: Joy(),
            EmotionName.TRUST: Disgust(),
            EmotionName.DISGUST: Trust(),
            EmotionName.FEAR: Anger(),
            EmotionName.ANGER: Fear(),
            EmotionName.SURPRISE: Anticipation(),
            EmotionName.ANTICIPATION: Surprise(),
        }

        return mapper[self.name]


@dataclass(frozen=True)
class Joy(Emotion):
    name = EmotionName.JOY
    category = EmotionCategory.POSITIVE


@dataclass(frozen=True)
class Trust(Emotion):
    name = EmotionName.TRUST
    category = EmotionCategory.POSITIVE


@dataclass(frozen=True)
class Surprise(Emotion):
    name = EmotionName.SURPRISE
    category = EmotionCategory.NEUTRAL


@dataclass(frozen=True)
class Anticipation(Emotion):
    name = EmotionName.ANTICIPATION
    category = EmotionCategory.NEUTRAL


@dataclass(frozen=True)
class Fear(Emotion):
    name = EmotionName.FEAR
    category = EmotionCategory.NEGATIVE


@dataclass(frozen=True)
class Sadness(Emotion):
    name = EmotionName.SADNESS
    category = EmotionCategory.NEGATIVE


@dataclass(frozen=True)
class Disgust(Emotion):
    name = EmotionName.DISGUST
    category = EmotionCategory.NEGATIVE


@dataclass(frozen=True)
class Anger(Emotion):
    name = EmotionName.ANGER
    category = EmotionCategory.NEGATIVE
