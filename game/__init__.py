import pygame

from . import settings
from .constants import WHITE
from .player import Player

SCREEN_START = (0, 0)
DEBUG_TEMPLATE = 'FPS: {0:.2f} Playtime: {1:.2f}'


def user_want_to_exit_game(event):
    """User closing application or pressed ESC."""

    quit_event = event.type == pygame.QUIT
    esc_pressed = (
            event.type == pygame.KEYDOWN and
            event.key == pygame.K_ESCAPE)
    return quit_event or esc_pressed


class Game:
    running = True
    playtime = 0.0

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            settings.SCREEN_SIZE)

    def _clear_screen(self, color=WHITE):
        """Clear artifacts from screen with one-color background."""

        background = pygame.Surface(self.screen.get_size())  # type: pygame.SurfaceType
        background.convert(background)
        background.fill(color)
        self.screen.blit(background, SCREEN_START)

    def start(self):
        pygame.init()
        self._clear_screen()

        p1 = Player()
        all_sprites = pygame.sprite.RenderPlain([p1])

        while self.running:
            milliseconds = self.clock.tick(settings.FPS)
            self.playtime += milliseconds / 1000.0

            for event in pygame.event.get():
                if user_want_to_exit_game(event):
                    self.running = False

            if settings.DEBUG:
                debug_msg = DEBUG_TEMPLATE.format(
                    self.clock.get_fps(), self.playtime)
                pygame.display.set_caption(debug_msg)

            all_sprites.update()
            self._clear_screen()
            all_sprites.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
