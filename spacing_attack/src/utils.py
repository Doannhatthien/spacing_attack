import pygame
import json
from io import BytesIO
from pathlib import Path
from .settings import IMAGE_DIR, SOUND_DIR, PROGRESS_FILE
from pathlib import Path
from PIL import Image


def load_image(name, size=None):
    path = IMAGE_DIR / name
    try:
        if path.suffix.lower() == ".png":
            try:
                with Image.open(path) as im:
                    im = im.convert("RGBA")
                    # loại bỏ ICC/exif để hết cảnh báo
                    im.info.pop("icc_profile", None)
                    im.info.pop("exif", None)
                    buf = BytesIO()
                    im.save(buf, format="PNG", optimize=True)
                    buf.seek(0)
                    surf = pygame.image.load(buf, name) 
            except ImportError:
                surf = pygame.image.load(str(path))
        else:
            surf = pygame.image.load(str(path))

        if size:
            surf = pygame.transform.smoothscale(surf, size)
        return surf.convert_alpha()
    except Exception as e:
        print(f"[load_image] load '{name}' failed: {e}")
        raise

def load_sound(name: str) -> pygame.mixer.Sound:
    path = SOUND_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy âm thanh: {path}, cwd={Path.cwd()}")
    if pygame.mixer.get_init() is None:
        pygame.mixer.init()
    return pygame.mixer.Sound(str(path))

def load_font(path_like, size: int):
    import pygame.freetype as ft
    if not ft.get_init():
        ft.init()

    font_path = None
    try:
        if path_like:
            p = Path(path_like)
            if p.is_file() and p.stat().st_size > 0:
                font_path = str(p)
    except Exception as e:
        print(f"[load_font] path check error: {e}")

    try:
        return ft.Font(font_path, size)
    except Exception as e:
        print(f"[load_font] open '{font_path}' failed: {e} -> fallback default")
        return ft.Font(None, size)  


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


def safe_json_load(path: Path, default=None):
    """Safely load JSON from path. Returns default on error or missing file."""
    try:
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"[safe_json_load] error loading {path}: {e}")
    return default


def safe_json_save(path: Path, data) -> bool:
    """Safely save JSON to path. Returns True on success, False on error."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[safe_json_save] error saving {path}: {e}")
        return False

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

def list_background_files() -> list[str]:
    exts = {".jpg", ".jpeg", ".png"}
    bg_dir = IMAGE_DIR / "backgrounds"
    files = []
    try:
        for p in bg_dir.iterdir():
            if p.is_file() and p.suffix.lower() in exts:
                files.append(str(p.relative_to(IMAGE_DIR)).replace("\\", "/"))
    except FileNotFoundError:
        pass
    return sorted(files)
