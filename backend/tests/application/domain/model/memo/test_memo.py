import pendulum
import pytest
from memotion.application.domain.model.memo.emotion.emotion import Joy
from memotion.application.domain.model.memo.emotion.emotion_set import EmotionSet
from memotion.application.domain.model.memo.happening_date import HappeningDate
from memotion.application.domain.model.memo.memo import Memo
from memotion.application.domain.model.memo.memo_id import MemoId
from memotion.application.domain.model.memo.memory.memory import Memory
from memotion.application.domain.model.memo.writing_date import WritingDate

default_memo_id = MemoId(100)
default_memory = Memory("Hello World")
default_emotions = EmotionSet({Joy()})
default_happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
default_writing_date = WritingDate(pendulum.datetime(2021, 1, 2))


class Testメモを作成する:
    def test_イベント日が書いた日より前のとき正しく生成される(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 3))

        Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

    def test_イベント日が書いた日と同じとき正しく生成される(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 1))

        Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

    def test_イベント日が書いた日より後のときエラーになる(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 3))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 1))

        with pytest.raises(ValueError):
            Memo.create(
                default_memo_id,
                default_memory,
                default_emotions,
                happening_date,
                writing_date,
            )


class Test記憶を修正する:
    def test_記憶を修正する(self):
        memo = Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            default_happening_date,
            default_writing_date,
        )

        revised_memory = Memory("Good Night World")
        memo.revise_memory(revised_memory)

        assert memo.memory == revised_memory


class Testメモを編集できるか:
    def test_書いてから24時間未満なら編集できる(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 2, 12, 0, 0))

        memo = Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

        rewrite_date = pendulum.datetime(2021, 1, 3, 11, 59, 59)

        assert memo.is_rewritable(rewrite_date) == True

    def test_書いてから24時間以上なら編集できない(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 2, 12, 0, 0))

        memo = Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

        rewrite_date = pendulum.datetime(2021, 1, 3, 12, 0, 0)

        assert memo.is_rewritable(rewrite_date) == False


class Testメモを削除できるか:
    def test_書いてから24時間未満なら削除できる(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 2, 12, 0, 0))

        memo = Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

        delete_date = pendulum.datetime(2021, 1, 3, 11, 59, 59)

        assert memo.is_deletable(delete_date) == True

    def test_書いてから24時間以上なら削除できない(self):
        happening_date = HappeningDate(pendulum.datetime(2021, 1, 1))
        writing_date = WritingDate(pendulum.datetime(2021, 1, 2, 12, 0, 0))

        memo = Memo.create(
            default_memo_id,
            default_memory,
            default_emotions,
            happening_date,
            writing_date,
        )

        delete_date = pendulum.datetime(2021, 1, 3, 12, 0, 0)

        assert memo.is_deletable(delete_date) == False
