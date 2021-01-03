from memotion.application.domain.model.memo.emotion.emotion import (
    Anger,
    Anticipation,
    Disgust,
    Fear,
    Joy,
    Sadness,
    Surprise,
    Trust,
)
from memotion.application.domain.model.memo.emotion.emotion_category import (
    EmotionCategory,
)
from memotion.application.domain.model.memo.emotion.emotion_name import EmotionName


class Test感情の生成:
    class Testポジティブな感情:
        def test_喜びはポジティブ(self):
            emotion = Joy()

            assert (emotion.name, emotion.category) == (
                EmotionName.JOY,
                EmotionCategory.POSITIVE,
            )

        def test_信頼はポジティブ(self):
            emotion = Trust()

            assert (emotion.name, emotion.category) == (
                EmotionName.TRUST,
                EmotionCategory.POSITIVE,
            )

    class Test中立な感情:
        def test_驚きは中立(self):
            emotion = Surprise()

            assert (emotion.name, emotion.category) == (
                EmotionName.SURPRISE,
                EmotionCategory.NEUTRAL,
            )

        def test_予期は中立(self):
            emotion = Anticipation()

            assert (emotion.name, emotion.category) == (
                EmotionName.ANTICIPATION,
                EmotionCategory.NEUTRAL,
            )

    class Testネガティブな感情:
        def test_恐れはネガティブ(self):
            emotion = Fear()

            assert (emotion.name, emotion.category) == (
                EmotionName.FEAR,
                EmotionCategory.NEGATIVE,
            )

        def test_悲しみはネガティブ(self):
            emotion = Sadness()

            assert (emotion.name, emotion.category) == (
                EmotionName.SADNESS,
                EmotionCategory.NEGATIVE,
            )

        def test_嫌悪はネガティブ(self):
            emotion = Disgust()

            assert (emotion.name, emotion.category) == (
                EmotionName.DISGUST,
                EmotionCategory.NEGATIVE,
            )

        def test_怒りはネガティブ(self):
            emotion = Anger()

            assert (emotion.name, emotion.category) == (
                EmotionName.ANGER,
                EmotionCategory.NEGATIVE,
            )


class Test対立する感情:
    def test_喜びの反対は悲しみ(self):
        assert Joy().opposition == Sadness()

    def test_悲しみの反対は喜び(self):
        assert Sadness().opposition == Joy()

    def test_信頼の反対は嫌悪(self):
        assert Trust().opposition == Disgust()

    def test_嫌悪の反対は信頼(self):
        assert Disgust().opposition == Trust()

    def test_恐れの反対は怒り(self):
        assert Fear().opposition == Anger()

    def test_怒りの反対は恐れ(self):
        assert Anger().opposition == Fear()

    def test_驚きの反対は予期(self):
        assert Surprise().opposition == Anticipation()

    def test_予期の反対は驚き(self):
        assert Anticipation().opposition == Surprise()
