import pytest
from memotion.application.domain.model.memo.memory.memory import Memory


class TestMemory:
    class Test正常系:
        def test_1文字の文字列を与える(self):
            assert Memory("a").content == "a"

    class Test異常系:
        def test_空文字のときエラーになる(self):
            with pytest.raises(ValueError):
                Memory("")

        def test_改行文字のみのときエラーになる(self):
            with pytest.raises(ValueError):
                Memory("\n\n")
