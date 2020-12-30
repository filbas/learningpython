



import sys
import os
import pygame
from pygame.locals import *

# Define the colours
WHITE = (255, 255, 255)
PURPLE = (96, 85, 154)
LIGHT_BLUE = (157, 220, 241)
DARK_BLUE = (63, 111, 182)
GREEN = (57, 180,22)

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCOREBOARD_MARGIN = 4
LINE_HEIGHT = 18
BOX_WIDTH = 300
BOX_HEIGHT = 150

TOTAL_LEVELS = 4
MAX_TREES = 12
TREE_SPACING = 40
FIRST_TREE = 140
GROUND_HEIGHT = 8
TREE_OFF_GROUND = 4

PLANE_START_X = 0
PLANE_START_Y = 54

# Setup
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Forest Bomber')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Helvetica', 16)

# Load images
background_image = pygame.image.load('background.png').convert()
tree_image = pygame.image.load('tree.png').convert_alpha()
burn_tree_image = pygame.image.load('burning_tree.png').convert_alpha()
plane_image = pygame.image.load('plane.png').convert_alpha()
burn_plane_image = pygame.image.load('burning_plane.png').convert_alpha()
bomb_image = pygame.image.load('bomb.png').convert_alpha()

# Load sounds
explosion_sound = pygame.mixer.Sound('explosion.ogg')
tree_sound = pygame.mixer.Sound('tree_explosion.ogg')

# Initialise variables
level = 1
score = 0
hi_score = 0
speed_boost = 0

plane_exploded = False
level_cleared = False
plane_front = 0
plane_explode_sound_played = False


bomb_dropped = False
bomb = bomb_image.get_rect()

plane = plane_image.get_rect()
plane.x = PLANE_START_X
plane.y = PLANE_START_Y

tree = tree_image.get_rect()
tree.y = SCREEN_HEIGHT - tree.height - TREE_OFF_GROUND

burning_tree = 0
tree_timer = 0

burning_trees = []

# Set up different forests for each level
forest_1 = ['T', '-', 'T', '-', '-', '-', 'T', '-', '-', '-', '-', 'T']
forest_2 = ['-', 'T', '-', '-', 'T', '-', 'T', '-', 'T', 'T', '-', 'T']
forest_3 = ['T', 'T', '-', '-', 'T', '-', 'T', 'T', 'T', 'T', '-', '-']
forest_4 = ['T', 'T', '-', '-', 'T', 'T', 'T', '-', 'T', 'T', 'T', '-']
forest = list(forest_1)
