import pygame
import json
from io import BytesIO
from pathlib import Path
from .settings import IMAGE_DIR, SOUND_DIR, PROGRESS_FILE
from PIL import Image


def stars_from_lives(lives: int) -> int:
    if lives >= 3:
        return 3
    elif lives == 2:
        return 2
    elif lives == 1:
        return 1
    return 0

def load_progress() -> dict:
    try:
        if PROGRESS_FILE.exists():
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                unlocked = int(data.get("unlocked_level", 1))
                stars = data.get("stars", [0]*10)
                if not isinstance(stars, list) or len(stars) != 10:
                    stars = [0]*10
                stars = [max(0, min(3, int(x))) for x in stars]
                return {"unlocked_level": max(1, min(10, unlocked)), "stars": stars}
    except Exception as e:
        print("[progress] load error:", e)
    return {"unlocked_level": 1, "stars": [0]*10}

def save_progress(unlocked_level: int, stars: list[int]) -> None:
    try:
        PROGRESS_FILE.parent.mkdir(exist_ok=True)
        # normalize
        unlocked_level = max(1, min(10, int(unlocked_level)))
        if not isinstance(stars, list) or len(stars) != 10:
            stars = [0]*10
        stars = [max(0, min(3, int(x))) for x in stars]
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump({"unlocked_level": unlocked_level, "stars": stars}, f)
    except Exception as e:
        print("[progress] save error:", e)

