from game.animation import Animation


class TestAnimation:
    def test_creating_tests(self, spritesheet):
        anim = Animation(spritesheet, 3)
        assert len(anim.frames) == 3
