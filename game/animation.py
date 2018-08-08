import pygame


class Animation:
    timer = 0
    current_frame = 0

    def __init__(self, image, frames=1):
        self.image = image
        self.rect = image.get_rect()
        self.frames = self._get_frames(frames)
        self.end_frame = len(self.frames) - 1

    def _get_frames(self, count):
        start = 0
        sprite_width = self.rect.width / count
        frames = []
        for frame in range(count):
            rect = pygame.Rect(
                start, 0, sprite_width, self.rect.height)
            frames.append(self.image.subsurface(rect))
            start += sprite_width
        return frames

    def update(self, speed=1):
        """
        Update animation current frame counter.

        :param speed: change frame every n cycles
        """
        self.timer += 1
        if self.timer == speed:
            self.current_frame = (
                0 if self.end_frame == self.current_frame
                else self.current_frame + 1)
            self.timer = 0
