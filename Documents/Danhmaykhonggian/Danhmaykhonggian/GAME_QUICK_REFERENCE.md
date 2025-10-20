# 📝 QUICK REFERENCE - GAME.PY

## 🎯 Tóm tắt nhanh các methods

### 🔧 KHỞI TẠO
```python
__init__(music_file=None, video_background=None)
```
- Khởi tạo pygame, window, assets
- Load images, sounds, music
- Setup biến game (score, lives, enemies, bullets)

---

### 🛠️ PRIVATE UTILITY (dùng nội bộ)

```python
_enemy_center_x(enemy) → int
```
➜ Tính X trung tâm enemy để ngắm bắn

```python
_update_ship_aim()
```
➜ Update góc xoay ship theo locked enemy

```python
_draw_hearts(x, y)
```
➜ Vẽ hearts thể hiện lives (3 mạng)

```python
_draw_heart_shape(surface, x, y, size, color, filled)
```
➜ Vẽ 1 trái tim bằng parametric equations

---

### 🎮 CORE GAME LOGIC

```python
check_ship_collision(enemy) → bool
```
➜ Kiểm tra enemy chạm ship (circle collision, radius=40px)

```python
hit_ship(enemy)
```
➜ Xử lý khi ship bị hit:
  - Lives -1
  - Explosion + screen shake
  - Invulnerable 60 frames
  - Unlock nếu đang lock

```python
spawn_enemy()
```
➜ Spawn enemy mới theo thời gian (SPAWN_DELAYMS)

```python
destroy_enemy(enemy)
```
➜ Phá hủy enemy:
  - Score +10/ký tự
  - Kills +1
  - Explosion + shake
  - Check win (Challenge mode)

---

### ⌨️ INPUT HANDLING

```python
handle_typed_char(ch)
```
➜ Xử lý ký tự gõ:
  - **Chưa lock:** Tìm enemy bắt đầu bằng 'ch', chọn gần nhất
  - **Đã lock:**
    - Đúng → Bắn, tăng progress
    - **Sai → BỎ QUA, GIỮ LOCK** (không auto-switch)

```python
handle_keydown(event)
```
➜ Xử lý phím đặc biệt:
  - **ESC:** Hủy lock
  - **Backspace:** Xóa ký tự, giảm progress, tăng HP

---

### 🔄 UPDATE & RENDER

```python
update()
```
➜ Update mỗi frame:
  1. Video background
  2. Screen shake
  3. Invulnerability timer
  4. Bullets (move + remove)
  5. Enemies (move + collision + remove)
  6. Explosions
  7. Ship aim

```python
draw()
```
➜ Render mỗi frame:
  1. Background + shake
  2. Enemies + shake (vàng nếu lock)
  3. Bullets + shake
  4. Explosions + shake
  5. Ship (flash khi hit, xoay khi lock)
  6. HUD (KHÔNG shake): Score, Hearts, Locked, Typing, Kills, Warning

---

### 🔁 MAIN LOOP

```python
run()
```
➜ Vòng lặp chính:
  1. Delta time (FPS control)
  2. Events (QUIT, KEYDOWN, TEXTINPUT)
  3. Spawn enemies
  4. Update
  5. Check end (lives<=0 hoặc target_kills)
  6. Draw
  7. Repeat

Post-game:
  - Stop music
  - Show Game Over (Classic mode)

---

## 📊 Biến quan trọng

### Game State
```python
score           # Điểm
lives           # Số mạng (0-3)
kills           # Số enemy giết được
target_kills    # Target (Challenge), None = Classic
completed       # Win flag (Challenge)
```

### Input State
```python
typed_word      # Từ đang gõ
locked          # Enemy đang lock (None nếu không)
angle           # Góc xoay ship
```

### Entities
```python
enemies = []    # Danh sách Enemy
bullets = []    # Danh sách Bullet
explosions = [] # Danh sách Explosion
screen_shake    # ScreenShake object
```

---

## 🎯 Flow chính

### Gõ từ (Chưa lock)
```
Gõ 'f' → Tìm enemies bắt đầu 'f' → Chọn gần nhất → Lock
        → Bắn bullet → hit_char → Check complete
```

### Gõ từ (Đã lock - Đúng)
```
Gõ 'o' (đúng) → Bắn bullet → hit_char → Check complete
```

### Gõ từ (Đã lock - Sai) ⭐
```
Gõ 'x' (sai) → Print warning → BỎ QUA, GIỮ LOCK
```

### Va chạm
```
Enemy chạm ship → check_ship_collision → hit_ship
                → Lives -1, Explosion, Shake, Invulnerable 60 frames
```

---

## 🔑 Key Features

### Lock Target System
- Tự động lock enemy khi gõ ký tự đầu
- Ship xoay về phía enemy locked
- Enemy hiển thị màu vàng
- **GỮ LOCK khi gõ sai** (không auto-switch)
- ESC để hủy, Backspace để sửa

### Lives System
- 3 mạng ban đầu
- Giảm khi enemy chạm ship
- Invulnerable 60 frames sau hit
- Flash effect khi bất tử
- Hearts đổi màu theo lives

### Screen Shake
- Apply khi explosion
- Intensity tùy độ dài từ
- Tất cả entities shake TRỪ HUD
- Decay theo thời gian

### HUD Caching
- Chỉ render khi giá trị thay đổi
- Cache: Score, Lives, Kills
- Không cache: Locked, Typing, Warning

---

## 🐛 Lỗi thường gặp

### AttributeError: 'word'
➜ Dùng `origin_word` thay vì `word`

### Hearts không hiển thị
➜ Gọi `_draw_hearts()` trong `draw()`

### Lock auto-switch
➜ Đã fix: Gõ sai → pass (không switch)

---

## 📚 Files liên quan

- `game.py` - File này
- `enemy.py` - Enemy class (movement, collision avoidance)
- `bullet.py` - Bullet class
- `explosion.py` - Explosion + ScreenShake
- `ship.py` - Draw ship functions
- `settings.py` - Constants (WIDTH, HEIGHT, FPS, WORDS)
- `utils.py` - load_image(), load_sound()

---

## 🎓 Đọc code chi tiết

➜ Xem file `GAME_CODE_STRUCTURE.md` để hiểu sâu hơn!

---

*Quick Reference - Cập nhật: 2025-01-20*
