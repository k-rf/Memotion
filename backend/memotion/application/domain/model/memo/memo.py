from dataclasses import dataclass
from pendulum.datetime import DateTime
from memotion.application.domain.model.memo.memo_id import MemoId
from memotion.application.domain.model.memo.emotion.emotion_set import EmotionSet

from .happening_date import HappeningDate
from .memory.memory import Memory
from .writing_date import WritingDate


@dataclass
class Memo:
    __REWRITABLE_LIMIT = 24
    __DELETABLE_LIMIT = 24

    memo_id: MemoId
    memory: Memory
    emotions: EmotionSet
    happening_date: HappeningDate
    writing_date: WritingDate

    def __post_init__(self):
        if self.writing_date.value < self.happening_date.value:
            raise ValueError("Invalid date order.")

    @classmethod
    def create(
        cls,
        memo_id: MemoId,
        memory: Memory,
        emotions: EmotionSet,
        happening_date: HappeningDate,
        writing_data: WritingDate,
    ):
        return cls(
            memo_id,
            memory,
            emotions,
            happening_date,
            writing_data,
        )

    def revise_memory(self, memory: Memory):
        self.memory = memory

    def __is_over_limit(self, target: DateTime, limit: int):
        return target < self.writing_date.add_hours(limit)

    def is_rewritable(self, target: DateTime):
        return self.__is_over_limit(target, self.__REWRITABLE_LIMIT)

    def is_deletable(self, target: DateTime):
        return self.__is_over_limit(target, self.__DELETABLE_LIMIT)
