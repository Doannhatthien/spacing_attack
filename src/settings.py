import sys
from pathlib import Path

# Detect if running as .exe (frozen by PyInstaller)
if getattr(sys, 'frozen', False):
    # Running as .exe - assets are in _MEIPASS temporary folder
    BASE_DIR = Path(sys._MEIPASS)
else:
    # Running as script - assets are relative to project root
    BASE_DIR = Path(__file__).parent.parent

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

# Đường dẫn asset - tự động detect khi chạy .exe hoặc script
ASSET_DIR = BASE_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"
SOUND_DIR = ASSET_DIR / "sounds"

# Font
FONT_DIR = ASSET_DIR / "fonts"
FONT_REGULAR = FONT_DIR / "Roboto-Regular.ttf"
FONT_BOLD    = FONT_DIR / "Roboto-Bold.ttf"

# Save directory - luôn ở thư mục user hiện tại (không trong _MEIPASS)
if getattr(sys, 'frozen', False):
    # Khi chạy .exe, lưu save vào thư mục hiện tại
    SAVE_DIR = Path.cwd() / "save"
    SAVE_DIR.mkdir(exist_ok=True, parents=True)
    
    # Copy save data từ _MEIPASS nếu chưa có (lần chạy đầu tiên)
    bundled_save = BASE_DIR / "save"
    if bundled_save.exists():
        import shutil
        # Copy leaderboard.json nếu chưa có
        if (bundled_save / "leaderboard.json").exists() and not (SAVE_DIR / "leaderboard.json").exists():
            try:
                shutil.copy2(bundled_save / "leaderboard.json", SAVE_DIR / "leaderboard.json")
            except Exception as e:
                print(f"Warning: Could not copy leaderboard.json: {e}")
        
        # Copy progress.json nếu chưa có
        if (bundled_save / "progress.json").exists() and not (SAVE_DIR / "progress.json").exists():
            try:
                shutil.copy2(bundled_save / "progress.json", SAVE_DIR / "progress.json")
            except Exception as e:
                print(f"Warning: Could not copy progress.json: {e}")
else:
    # Khi chạy script, lưu vào thư mục project
    SAVE_DIR = BASE_DIR / "save"
    SAVE_DIR.mkdir(exist_ok=True, parents=True)

PROGRESS_FILE = SAVE_DIR / "progress.json"

# Challenge
CHALLENGE_LEVELS = [0.8, 1.2, 1.5, 1.7, 1.9, 2.3, 2.7, 3.0, 3.5, 4.0]  # tốc độ rơi
STAR_IMAGE_NAME = "star.png"

# States
STATE_MENU = "menu"
STATE_CLASSIC = "classic"
STATE_CHALLENGE = "challenge"
STATE_LEADERBOARD = "leaderboard"
STATE_LEVEL_CLEAR = "level_clear"
