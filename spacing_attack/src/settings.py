from pathlib import Path

# Màn hình
WIDTH, HEIGHT = 800, 600
FPS = 60

# Màu
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Tàu
SHIP_WIDTH  = 60
SHIP_HEIGHT = 40
SHIP_Y = HEIGHT - SHIP_HEIGHT - 10 

# Enemy & spawn
ENEMY_SPEED   = 1.0
SPAWN_DELAYMS = 2500  

# WORDS
WORDS = [
    "apple", "banana", "car", "house", "cat",
    "book", "phone", "river", "planet", "chair",
    "music", "school", "light", "game", "bird",
    "train", "coffee", "robot", "cloud", "tree"
]

# Đường dẫn asset tương đối
ASSET_DIR = Path("assets")
IMAGE_DIR = ASSET_DIR / "images"
SOUND_DIR = ASSET_DIR / "sounds"

# Font
FONT_DIR = ASSET_DIR / "fonts"
FONT_REGULAR = FONT_DIR / "Roboto-Regular.ttf"
FONT_BOLD    = FONT_DIR / "Roboto-Bold.ttf"

SAVE_DIR = Path("save")
SAVE_DIR.mkdir(exist_ok=True)
PROGRESS_FILE = SAVE_DIR / "progress.json"

# Challenge
CHALLENGE_LEVELS = [1.2, 1.5, 1.8, 2.2, 2.6, 3.0, 3.5, 4.0, 4.6, 5.2]  # tốc độ rơi
STAR_IMAGE_NAME = "star.png"

# States
STATE_MENU = "menu"
STATE_CLASSIC = "classic"
STATE_CHALLENGE = "challenge"
STATE_LEADERBOARD = "leaderboard"
STATE_LEVEL_CLEAR = "level_clear"
