from memotion.application.domain.model.memo.writing_date import WritingDate

from pendulum.datetime import DateTime


class TestWritingDate:
    def test_時間を足す(self):
        a = WritingDate(DateTime(2021, 1, 2))
        b = DateTime(2021, 1, 3)

        assert a.add_hours(24) == b
