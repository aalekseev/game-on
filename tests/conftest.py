import os

import pygame
import pytest

from game import settings


@pytest.fixture
def spritesheet():
    return pygame.image.load(
        os.path.abspath(os.path.join(settings.ASSETS_PATH, 'sprites/ghost.png')))
