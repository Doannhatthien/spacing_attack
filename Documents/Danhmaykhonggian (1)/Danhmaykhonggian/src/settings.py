from pathlib import Path

# Màn hình
WIDTH, HEIGHT = 800, 600
FPS = 120  # Tăng lên 120 FPS cho chuyển động mượt mà hơn
VSYNC = True  # Bật VSync để tránh screen tearing

# Màu
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# Tàu
SHIP_WIDTH  = 60
SHIP_HEIGHT = 40
SHIP_Y = HEIGHT - SHIP_HEIGHT - 10 

# Enemy & spawn
ENEMY_SPEED   = 0.6  # Tốc độ cơ bản cho từ ngắn
SPAWN_DELAYMS = 2500  

# WORDS - Phân theo độ dài từ ngắn đến dài
WORDS = [
    # Từ ngắn (3-4 ký tự) - Rơi nhanh
    "cat", "dog", "car", "sun", "run",
    "book", "moon", "star", "tree", "fish",
    
    # Từ trung bình (5-7 ký tự) - Rơi vừa
    "apple", "water", "phone", "river", "chair",
    "music", "school", "planet", "coffee", "robot",
    "light", "cloud", "train", "game", "bird",
    "ocean", "garden", "forest", "dragon", "castle",
    
    # Từ dài (8-10 ký tự) - Rơi chậm
    "computer", "keyboard", "mountain", "universe", "elephant",
    "butterfly", "adventure", "beautiful", "chocolate", "wonderful",
    "important", "different", "hospital", "scientist", "government",
    
    # Từ rất dài (11-15 ký tự) - Rơi rất chậm
    "programming", "environment", "communication", "understanding", "extraordinary",
    "revolutionary", "entertainment", "international", "championship", "transformation",
    "sophisticated", "congratulations", "determination", "independence", "technological"
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
