# 🖼️ HƯỚNG DẪN LOAD HÌNH ẢNH TRONG GAME

## 📍 Tất cả vị trí load hình ảnh

---

## 1️⃣ **FILE: `src/game.py`** - Game chính

### 🌌 Background (Hình nền)
**Dòng 94:**
```python
self.background = load_image("backgrounds/background3.jpg", (WIDTH, HEIGHT))
```
- **Đường dẫn:** `assets/images/backgrounds/background3.jpg`
- **Kích thước:** 800x600 (WIDTH x HEIGHT)
- **Mục đích:** Hình nền game chính
- **Thay đổi:** Đổi `"backgrounds/background3.jpg"` thành tên file khác trong thư mục `backgrounds/`

---

### 💥 Explosion (Vụ nổ)
**Dòng 103:**
```python
self.explosion_img = load_image("explosion.png", (40, 40))
```
- **Đường dẫn:** `assets/images/explosion.png`
- **Kích thước:** 40x40 pixel
- **Mục đích:** Hình ảnh vụ nổ khi phá hủy enemy
- **Thay đổi:** 
  - Đổi tên file: `"my_explosion.png"`
  - Đổi kích thước: `(60, 60)` để to hơn

---

## 2️⃣ **FILE: `src/ship.py`** - Phi thuyền

### 🚀 Spaceship (Phi thuyền)
**Dòng 27:**
```python
img = load_image("spaceship.png", (80, 80))
```
- **Đường dẫn:** `assets/images/spaceship.png`
- **Kích thước:** 80x80 pixel
- **Mục đích:** Hình phi thuyền của người chơi
- **Vị trí:** Ở cuối màn hình (giữa, dưới cùng)
- **Thay đổi:**
  - Đổi hình: `"my_ship.png"`
  - To hơn: `(100, 100)`
  - Nhỏ hơn: `(60, 60)`

---

## 3️⃣ **FILE: `src/challenge.py`** - Challenge Mode

### ⭐ Star (Ngôi sao đánh giá)
**Dòng 23:**
```python
self.star_img = load_image(STAR_IMAGE_NAME, (36, 36))
```
- **Đường dẫn:** `assets/images/star.png` (từ `settings.py`)
- **Kích thước:** 36x36 pixel
- **Mục đích:** Hiển thị số sao khi hoàn thành level
- **Thay đổi:** Sửa trong `settings.py` → `STAR_IMAGE_NAME = "your_star.png"`

---

## 4️⃣ **FILE: `src/level_select.py`** - Màn chọn level

### ⭐ Star (Ngôi sao trong level select)
**Dòng 29:**
```python
self.star_img = load_image("star.png", (22, 22))
```
- **Đường dẫn:** `assets/images/star.png`
- **Kích thước:** 22x22 pixel
- **Mục đích:** Hiển thị số sao đã đạt được mỗi level
- **Thay đổi:** Nhỏ hơn challenge mode (22 vs 36)

---

### 🔒 Lock (Khóa level)
**Dòng 34:**
```python
self.lock_img = load_image("lock.png", (26, 26))
```
- **Đường dẫn:** `assets/images/lock.png`
- **Kích thước:** 26x26 pixel
- **Mục đích:** Hiển thị level chưa mở khóa
- **Thay đổi:** Đổi icon khóa bằng hình khác

---

## 5️⃣ **FILE: `src/main.py`** - Main menu

### 🖼️ Menu Background
**Dòng 30:**
```python
background = load_image("background.jpg", (WIDTH, HEIGHT))
```
- **Đường dẫn:** `assets/images/background.jpg`
- **Kích thước:** 800x600 pixel
- **Mục đích:** Background của menu chính
- **Thay đổi:** Đổi background menu khác với game

---

### 🎨 Dynamic Background (khi chọn từ menu)
**Dòng 128:**
```python
game.background = load_image(chosen_bg, (WIDTH, HEIGHT))
```
- **Đường dẫn:** Tùy người chơi chọn trong menu
- **Kích thước:** 800x600 pixel
- **Mục đích:** Load background được chọn vào game
- **Tự động:** Load từ background selector

---

## 6️⃣ **FILE: `src/background_select.py`** - Background selector

### 🎞️ Preview Thumbnails (Ảnh xem trước)
**Dòng 181:**
```python
img = load_image(name, (draw_rect.width, draw_rect.height))
```
- **Đường dẫn:** `assets/images/backgrounds/*.jpg`
- **Kích thước:** Tự động resize theo ô preview
- **Mục đích:** Hiển thị thumbnail các background có sẵn
- **Dynamic:** Quét tất cả file trong thư mục backgrounds/

---

## 📂 CẤU TRÚC THƯ MỤC HÌNH ẢNH

```
assets/
├── images/
│   ├── background.jpg              ← Menu background (main.py:30)
│   ├── explosion.png               ← Vụ nổ (game.py:103)
│   ├── spaceship.png               ← Phi thuyền (ship.py:27)
│   ├── star.png                    ← Ngôi sao (challenge.py:23, level_select.py:29)
│   ├── lock.png                    ← Khóa level (level_select.py:34)
│   │
│   ├── backgrounds/                ← Thư mục backgrounds
│   │   ├── background3.jpg         ← Game background (game.py:94)
│   │   ├── background1.jpg         ← Tuỳ chọn khác
│   │   ├── background2.jpg
│   │   └── ...
│   │
│   └── ships/                      ← (Nếu có nhiều mẫu ship)
│       └── ...
```

---

## 🎨 BẢNG TỔNG HỢP TẤT CẢ HÌNH ẢNH

| Hình ảnh | File | Dòng | Đường dẫn | Kích thước | Mục đích |
|----------|------|------|-----------|------------|----------|
| 🌌 Game Background | `game.py` | 94 | `backgrounds/background3.jpg` | 800x600 | Nền game chính |
| 💥 Explosion | `game.py` | 103 | `explosion.png` | 40x40 | Vụ nổ |
| 🚀 Spaceship | `ship.py` | 27 | `spaceship.png` | 80x80 | Phi thuyền |
| ⭐ Star (Challenge) | `challenge.py` | 23 | `star.png` | 36x36 | Sao đánh giá |
| ⭐ Star (Level Select) | `level_select.py` | 29 | `star.png` | 22x22 | Sao level |
| 🔒 Lock | `level_select.py` | 34 | `lock.png` | 26x26 | Khóa level |
| 🖼️ Menu Background | `main.py` | 30 | `background.jpg` | 800x600 | Nền menu |
| 🎨 Dynamic BG | `main.py` | 128 | `chosen_bg` | 800x600 | BG được chọn |
| 🎞️ BG Thumbnails | `background_select.py` | 181 | `backgrounds/*` | Auto | Preview |

---

## 🛠️ CÁCH THAY ĐỔI HÌNH ẢNH

### 1. Thay đổi hình có sẵn
```python
# VÍ DỤ: Thay explosion.png
# TỪ:
self.explosion_img = load_image("explosion.png", (40, 40))

# THÀNH:
self.explosion_img = load_image("my_explosion.png", (60, 60))
```

**Bước làm:**
1. Đặt file `my_explosion.png` vào `assets/images/`
2. Sửa code như trên
3. Save và chạy lại game

---

### 2. Thay đổi kích thước
```python
# Explosion to hơn
self.explosion_img = load_image("explosion.png", (80, 80))  # Tăng từ 40→80

# Ship nhỏ hơn
img = load_image("spaceship.png", (50, 50))  # Giảm từ 80→50
```

---

### 3. Thêm hình mới
```python
# Thêm hình shield (khiên)
self.shield_img = load_image("shield.png", (100, 100))
```

**Bước làm:**
1. Tạo/đặt file `shield.png` vào `assets/images/`
2. Thêm dòng load vào `__init__()` của game.py
3. Dùng `self.shield_img` để vẽ trong `draw()`

---

### 4. Sử dụng nhiều hình cho 1 object
```python
# Nhiều mẫu explosion
self.explosion_imgs = [
    load_image("explosion1.png", (40, 40)),
    load_image("explosion2.png", (40, 40)),
    load_image("explosion3.png", (40, 40)),
]

# Chọn ngẫu nhiên
import random
chosen_explosion = random.choice(self.explosion_imgs)
```

---

## 🎯 VỊ TRÍ ĐỂ THÊM HÌNH ẢNH MỚI

### Thêm trong `game.py` (sau dòng 103)
```python
# ============================================================
# ASSETS - IMAGES
# ============================================================
try:
    self.explosion_img = load_image("explosion.png", (40, 40))
except:
    self.explosion_img = None

# 👇 THÊM HÌNH MỚI Ở ĐÂY
try:
    self.shield_img = load_image("shield.png", (60, 60))
except:
    self.shield_img = None

try:
    self.powerup_img = load_image("powerup.png", (30, 30))
except:
    self.powerup_img = None
```

---

## 📏 KÍCH THƯỚC ĐỀ XUẤT

### Theo loại hình
| Loại | Kích thước đề xuất | Lý do |
|------|-------------------|-------|
| 🌌 Background | 800x600 (hoặc 1280x720) | Full màn hình |
| 🚀 Ship | 60x60 đến 100x100 | Vừa nhìn rõ |
| 💥 Explosion | 40x40 đến 80x80 | Đủ lớn nhưng không che |
| ⭐ Star | 20x20 đến 40x40 | Icon nhỏ |
| 👾 Enemy (nếu có) | 40x40 đến 60x60 | Nhỏ hơn ship |
| 🎁 Powerup (nếu có) | 30x30 đến 50x50 | Dễ nhận |

---

## 🔍 CÁCH TÌM FILE HÌNH ẢNH TRONG CODE

### 1. Dùng Find (Ctrl+F)
```
Tìm: load_image("
→ Sẽ tìm tất cả dòng load hình ảnh
```

### 2. Dùng Regex
```
Tìm: load_image\("([^"]+)"
→ Tìm và highlight tên file
```

### 3. Grep trong workspace
```
Tìm: load_image
Include: src/*.py
→ Tìm trong tất cả file Python
```

---

## ⚠️ LƯU Ý QUAN TRỌNG

### 1. Đường dẫn tương đối
```python
# ✅ ĐÚNG
load_image("explosion.png", ...)          # Tìm trong assets/images/
load_image("backgrounds/bg.jpg", ...)     # Tìm trong assets/images/backgrounds/

# ❌ SAI
load_image("assets/images/explosion.png", ...)  # Thừa assets/images/
load_image("C:/full/path/explosion.png", ...)   # Đường dẫn tuyệt đối
```

### 2. Định dạng file hỗ trợ
```
✅ PNG (.png) - Khuyến khích (hỗ trợ trong suốt)
✅ JPG (.jpg, .jpeg) - Tốt cho background
✅ BMP (.bmp) - Cơ bản
❌ GIF (.gif) - Không hỗ trợ animation
❌ SVG (.svg) - Không hỗ trợ vector
```

### 3. Try-except để tránh crash
```python
# ✅ TỐT - Có xử lý lỗi
try:
    self.explosion_img = load_image("explosion.png", (40, 40))
except:
    self.explosion_img = None

# ❌ KHÔNG NÊN - Crash nếu không tìm thấy file
self.explosion_img = load_image("explosion.png", (40, 40))
```

### 4. Kiểm tra None trước khi dùng
```python
# Khi vẽ
if self.explosion_img:
    surface.blit(self.explosion_img, position)
else:
    # Vẽ fallback (vòng tròn, hình chữ nhật...)
    pygame.draw.circle(surface, (255, 0, 0), position, 20)
```

---

## 🎨 VÍ DỤ THỰC TẾ

### Thay đổi ship thành mẫu khác
```python
# File: src/ship.py - Dòng 27

# CŨ:
img = load_image("spaceship.png", (80, 80))

# MỚI - Ship màu đỏ to hơn:
img = load_image("spaceship_red.png", (100, 100))
```

### Thêm nhiều loại explosion
```python
# File: src/game.py - Sau dòng 103

# Thêm:
try:
    self.explosion_small = load_image("explosion_small.png", (30, 30))
    self.explosion_large = load_image("explosion_large.png", (100, 100))
except:
    self.explosion_small = None
    self.explosion_large = None

# Sử dụng trong code:
if word_length > 10:
    explosion_img = self.explosion_large  # Từ dài nổ to
else:
    explosion_img = self.explosion_small  # Từ ngắn nổ nhỏ
```

---

## 📊 PERFORMANCE TIPS

### 1. Load một lần, dùng nhiều lần
```python
# ✅ TỐT - Load trong __init__
def __init__(self):
    self.explosion_img = load_image("explosion.png", (40, 40))

# ❌ TỆ - Load mỗi lần vẽ
def draw(self):
    img = load_image("explosion.png", (40, 40))  # Chậm!
```

### 2. Resize đúng kích thước cần dùng
```python
# ✅ TỐT - Resize khi load
img = load_image("big_image.png", (40, 40))

# ❌ TỆ - Load to rồi resize nhỏ
img = load_image("big_image.png", (2000, 2000))
img = pygame.transform.scale(img, (40, 40))  # Tốn RAM
```

### 3. Dùng format phù hợp
```
📦 PNG - Hình có transparency (explosion, ship, star)
📦 JPG - Background lớn (nhẹ hơn PNG)
```

---

## 🎓 TÓM TẮT

**📍 Tổng cộng: 9 vị trí load hình ảnh chính**

1. `game.py:94` - Game background
2. `game.py:103` - Explosion
3. `ship.py:27` - Spaceship
4. `challenge.py:23` - Star (challenge)
5. `level_select.py:29` - Star (level)
6. `level_select.py:34` - Lock
7. `main.py:30` - Menu background
8. `main.py:128` - Dynamic background
9. `background_select.py:181` - BG thumbnails

**🎯 Cách sửa nhanh:**
1. Mở file tương ứng
2. Tìm dòng được chỉ ra
3. Đổi tên file hoặc kích thước
4. Save và test

**💡 Nhớ:**
- Đặt file vào `assets/images/`
- Đường dẫn tương đối, không cần `assets/images/`
- Dùng try-except để tránh crash
- Kiểm tra None trước khi vẽ

---

*Hướng dẫn được tạo: 2025-01-20*
*Tất cả vị trí load hình ảnh trong game*
