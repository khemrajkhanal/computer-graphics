"""
Configuration file for physics simulation
Contains all the settings, colors and physics constrains
 """

# Screen settings
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
ORANGE = (255,165,0)
# Color for targets
GREY = (125,125,125)
TEAL = (0,128,128)
NAVY = (0,0,128)

# Physics constants
GRAVITY = 0.5
BOUNCE_DAMPING = 0.8

# Ball Settings
BALL_RADIUS = 20
BALL_COLOR = RED

COLOR_LIST = [RED, BLUE, GREEN, YELLOW, CYAN, MAGENTA, ORANGE, WHITE]

# Velocity settings
VELOCITY_SCALE = 0.3

# Force settings
WIND_STRENGTH = 0.3
MOUSE_GRAVITY_STRENGTH = 5.0
MOUSE_REPEL_STRENGTH = 8.0
GRAVITY_CHANGE = 0.1

# Collision Setting
COLLISION_DAMPING = 0.95 # (1.0 = perfectly elastic)

# Game Mode Settings
GAME_MODE = False
GAME_TIME_LIMIT = 60
TARGET_SPAWN_INTERVAL = 2.0
MAX_TARGETS = 5

# Target Settings
TARGET_COLOR = [NAVY, GREY, TEAL]
TARGET_SPEED = 2.0

# Scoring
SCORE_SMALL_TARGET = 100
SCORE_MEDIUM_TARGET = 50
SCORE_LARGE_TARGET = 25
