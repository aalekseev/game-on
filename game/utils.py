import glob
import os

import pygame

from .settings import ASSETS_PATH


def load_img(path):
    """Load single image."""
    img_path = os.path.abspath(
        os.path.join(ASSETS_PATH, path))
    img = pygame.image.load(img_path).convert_alpha()
    return img


def load_seq(path, extension='png'):
    """Load all images from folder."""
    images = glob.glob(
        os.path.abspath(path) + '*.' + extension)
    for image_path in images:
        yield load_img(image_path)
