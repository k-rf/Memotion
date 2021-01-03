from memotion.application.domain.model.memo.emotion.emotion import (
    Anger,
    Joy,
    Sadness,
    Trust,
)
from memotion.application.domain.model.memo.emotion.emotion_set import EmotionSet
import pytest


class TestEmotionSet:
    class Testクローン関数:
        def test_クローンしたもののIDは異なる(self):
            emotions = EmotionSet.instance({Joy()})
            actual = emotions.clone()

            assert id(actual) != id(emotions)
            assert id(actual.emotions) != id(emotions.emotions)

        def test_クローンしたものは中身が共有されない(self):
            emotions = EmotionSet.instance({Joy()})
            clone = emotions.clone()

            clone.emotions.add(Anger())
            emotions.emotions.add(Trust())

            assert clone != emotions

    class Test感情が0個はダメ:
        def test_Emotionが0個のときインスタンス化するとエラーになる(self):
            with pytest.raises(ValueError):
                EmotionSet(set())

        def test_Emotionが0個のときinstanceメソッドを呼び出すとエラーになる(self):
            with pytest.raises(ValueError):
                EmotionSet.instance(set())

    class Test同じ感情は追加できない:
        def test_同じ感情を追加しても状態は変わらない(self):
            emotions = EmotionSet.instance({Joy(), Joy()})
            expected = EmotionSet.instance({Joy()})

            assert emotions == expected
            assert len(emotions) == len(expected)

    class Test対立する感情は追加できない:
        class Test対立する感情が存在するとエラーになる:
            def test_喜びと悲しみのときエラーになる(self):
                with pytest.raises(ValueError):
                    EmotionSet({Joy(), Joy().opposition})

            def test_喜びと悲しみと怒りのときエラーになる(self):
                with pytest.raises(ValueError):
                    EmotionSet({Joy(), Sadness(), Anger()})

            def test_喜びと怒りのときエラーにならない(self):
                EmotionSet({Joy(), Anger()})
