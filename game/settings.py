import os

from configparser import ConfigParser

project_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))

default_section = 'main'

debug_option = 'debug'
fps_option = 'fps'
weight_option = 'screen_weight'
height_option = 'screen_height'

parser = ConfigParser()
parser.read_dict({
    default_section: {
        debug_option: 'on',
        fps_option: '30',
        weight_option: '480',
        height_option: '640',
    }
})
parser.read(os.path.join(project_dir, 'settings.ini'))

DEBUG = parser.getboolean(default_section, debug_option)
FPS = parser.getint(default_section, fps_option)

SCREEN_HEIGHT = parser.getint(default_section, height_option)
SCREEN_WEIGHT = parser.getint(default_section, weight_option)
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WEIGHT)

ASSETS_PATH = os.path.abspath(os.path.join(project_dir, 'assets'))
