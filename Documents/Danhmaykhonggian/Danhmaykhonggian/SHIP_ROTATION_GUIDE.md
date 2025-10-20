# 🎯 HƯỚNG DẪN: XỬ LÝ HƯỚNG DI CHUYỂN PHI THUYỀN THEO ENEMY

## 📍 CÁC DÒNG QUAN TRỌNG

---

## 1️⃣ **FILE: `src/game.py`** - Tính toán góc xoay

### 🔧 Khởi tạo biến angle
**Dòng 154:**
```python
self.angle = 0.0
```
- **Mục đích:** Lưu góc xoay hiện tại của phi thuyền (tính bằng radian)
- **Giá trị mặc định:** `0.0` = hướng thẳng lên
- **Khi nào thay đổi:** Khi lock enemy, angle sẽ được update liên tục

---

### 🎯 Method chính: `_update_ship_aim()`
**Dòng 174-184:**
```python
def _update_ship_aim(self):
    """
    Cập nhật góc xoay của phi thuyền để ngắm về enemy đang lock.
    Nếu không có lock thì angle = 0 (hướng thẳng lên).
    """
    if self.locked and self.locked in self.enemies:
        tx = self._enemy_center_x(self.locked)
        ty = self.locked.y
        self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))
    else:
        self.angle = 0.0
```

#### 📊 Phân tích chi tiết:

**Dòng 179:** Kiểm tra có enemy bị lock không
```python
if self.locked and self.locked in self.enemies:
```
- `self.locked` không phải `None`
- `self.locked` vẫn còn trong danh sách `self.enemies` (chưa bị phá hủy)

**Dòng 180:** Lấy toạ độ X trung tâm của enemy
```python
tx = self._enemy_center_x(self.locked)
```
- Gọi method `_enemy_center_x()` để tính chính xác vị trí giữa của từ enemy

**Dòng 181:** Lấy toạ độ Y của enemy
```python
ty = self.locked.y
```
- Vị trí Y của enemy (chiều dọc màn hình)

**Dòng 182:** 🌟 **CÔNG THỨC QUAN TRỌNG NHẤT**
```python
self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))
```

#### 🔬 Phân tích công thức:

```
┌─────────────────────────────────────────┐
│  angle = atan2(Δy, Δx)                  │
│                                         │
│  Δy = ty - SHIP_Y                       │
│     = enemy.y - phi_thuyền.y            │
│     = Khoảng cách dọc                   │
│                                         │
│  Δx = tx - (WIDTH // 2)                 │
│     = enemy.x - phi_thuyền.x            │
│     = Khoảng cách ngang                 │
└─────────────────────────────────────────┘
```

**Giải thích:**
- `SHIP_Y` = 550 (vị trí Y cố định của phi thuyền - gần đáy màn hình)
- `WIDTH // 2` = 400 (vị trí X cố định của phi thuyền - giữa màn hình)
- `math.atan2(y, x)` = Tính góc từ trục X đến điểm (x, y) theo radian
- Kết quả: Góc từ phi thuyền đến enemy

**Dòng 183-184:** Không có lock → Hướng thẳng lên
```python
else:
    self.angle = 0.0
```

---

### 🔄 Gọi update trong game loop
**Dòng 506-507:**
```python
# Ship aim
self._update_ship_aim()
```
- **Vị trí:** Cuối method `update()`, sau khi update enemies
- **Tần suất:** Mỗi frame (60 lần/giây với FPS=60)
- **Mục đích:** Liên tục cập nhật góc xoay theo vị trí enemy mới

---

### 🖼️ Vẽ phi thuyền đã xoay
**Dòng 580:**
```python
draw_rotated_ship(self.win, self.angle, shake_offset)
```
- **Điều kiện:** Chỉ gọi khi `self.locked` tồn tại
- **Tham số:**
  - `self.win`: Surface để vẽ
  - `self.angle`: Góc xoay (radian) đã tính ở trên
  - `shake_offset`: Offset cho hiệu ứng rung màn hình

---

## 2️⃣ **FILE: `src/ship.py`** - Vẽ phi thuyền xoay

### 🎨 Function: `draw_rotated_ship()`
**Dòng 53-75:**
```python
def draw_rotated_ship(surface: pygame.Surface, angle_rad: float, offset=(0, 0)):
    """
    Vẽ tàu vũ trụ với góc xoay nhất định (angle_rad — tính bằng radian).
    - Dùng trong trường hợp tàu tự động xoay nòng súng hướng về enemy bị lock.
    - offset dùng cho hiệu ứng rung hoặc dịch chuyển nhẹ.
    """

    _init_ship()  # Đảm bảo ảnh tàu đã được tải
    
    # Chuyển góc từ radian sang độ, đồng thời trừ 90 độ để điều chỉnh hướng mũi tàu cho đúng
    deg = -math.degrees(angle_rad) - 90  

    # Xoay ảnh theo góc đã tính
    rotated = pygame.transform.rotate(_ship_img, deg)

    # Lấy vị trí trung tâm mới sau khi xoay
    rect = rotated.get_rect(
        center=(WIDTH // 2 + offset[0], SHIP_Y + offset[1])
    )

    # Vẽ ảnh xoay lên màn hình
    surface.blit(rotated, rect)
```

#### 📊 Phân tích chi tiết:

**Dòng 62:** 🌟 **CÔNG THỨC CHUYỂN ĐỔI GÓC**
```python
deg = -math.degrees(angle_rad) - 90
```

**Giải thích:**
1. `math.degrees(angle_rad)`: Chuyển từ radian sang độ (°)
2. `-`: Đảo ngược chiều (vì pygame xoay ngược chiều kim đồng hồ)
3. `- 90`: Điều chỉnh vì mặc định hình phi thuyền hướng lên (90°)

**Tại sao trừ 90?**
```
Mặc định pygame:
  0° = Hướng phải →
  90° = Hướng lên ↑
  180° = Hướng trái ←
  270° = Hướng xuống ↓

Nhưng phi thuyền vốn đã hướng lên (90°)
→ Cần trừ đi 90° để hiệu chỉnh
```

**Dòng 65:** Xoay ảnh
```python
rotated = pygame.transform.rotate(_ship_img, deg)
```
- Tạo ảnh mới đã xoay theo góc `deg`

**Dòng 68-70:** Căn giữa phi thuyền
```python
rect = rotated.get_rect(
    center=(WIDTH // 2 + offset[0], SHIP_Y + offset[1])
)
```
- Vị trí: Giữa màn hình (400, 550)
- Có thêm offset cho screen shake

**Dòng 73:** Vẽ lên màn hình
```python
surface.blit(rotated, rect)
```

---

## 📐 TOÁN HỌC ĐẰNG SAU

### 🧮 Công thức `atan2()`

```python
angle = math.atan2(Δy, Δx)
```

**Đầu vào:**
- `Δy` = ty - SHIP_Y (khoảng cách dọc)
- `Δx` = tx - (WIDTH // 2) (khoảng cách ngang)

**Đầu ra:**
- Góc từ -π đến +π radian (-180° đến +180°)

**Ví dụ thực tế:**

```
Enemy ở vị trí: (500, 200)
Ship ở vị trí: (400, 550)

Δx = 500 - 400 = 100
Δy = 200 - 550 = -350

angle = atan2(-350, 100) ≈ -1.29 radian ≈ -74°
```

### 📊 Biểu đồ góc xoay

```
         0° (0 rad)
         ↑ Enemy ở trên, giữa
         │
 -90° ←──┼──→ +90°
Enemy    │    Enemy
trái     │    phải
         │
        Ship (400, 550)
```

---

## 🔄 FLOW HOẠT ĐỘNG

### 1. Mỗi frame trong game loop:

```
┌─────────────────────────────────┐
│ 1. Player gõ ký tự đầu          │
│    → Lock enemy                 │
└──────────┬──────────────────────┘
           ↓
┌─────────────────────────────────┐
│ 2. update() được gọi            │
│    → Gọi _update_ship_aim()     │
└──────────┬──────────────────────┘
           ↓
┌─────────────────────────────────┐
│ 3. _update_ship_aim()            │
│    - Lấy vị trí enemy (tx, ty)  │
│    - Tính angle = atan2(Δy, Δx) │
└──────────┬──────────────────────┘
           ↓
┌─────────────────────────────────┐
│ 4. draw() được gọi               │
│    → Gọi draw_rotated_ship()    │
└──────────┬──────────────────────┘
           ↓
┌─────────────────────────────────┐
│ 5. draw_rotated_ship()           │
│    - Chuyển radian → độ         │
│    - Hiệu chỉnh -90°            │
│    - Xoay ảnh                   │
│    - Vẽ lên màn hình            │
└─────────────────────────────────┘
```

---

## 🎮 ĐIỀU CHỈNH HÀNH VI

### 1. Thay đổi tốc độ xoay (smooth rotation)

Hiện tại phi thuyền xoay **tức thì**. Muốn xoay **mượt hơn**:

**Sửa trong `game.py` - Method `_update_ship_aim()` (dòng 174):**
```python
def _update_ship_aim(self):
    if self.locked and self.locked in self.enemies:
        tx = self._enemy_center_x(self.locked)
        ty = self.locked.y
        target_angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))
        
        # Xoay mượt thay vì tức thì
        angle_diff = target_angle - self.angle
        
        # Normalize về khoảng -π đến π
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        
        # Xoay từ từ (0.1 = 10% mỗi frame)
        self.angle += angle_diff * 0.1
    else:
        # Về 0 từ từ
        self.angle *= 0.9
```

---

### 2. Giới hạn góc xoay tối đa

Nếu muốn phi thuyền chỉ xoay trong phạm vi hẹp:

**Thêm sau dòng 182:**
```python
self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))

# Giới hạn góc xoay tối đa ±60°
max_angle = math.radians(60)
self.angle = max(-max_angle, min(max_angle, self.angle))
```

---

### 3. Thay đổi điểm xoay

Hiện tại xoay quanh **trung tâm phi thuyền**. Muốn xoay quanh **mũi phi thuyền**:

**Sửa trong `ship.py` - Dòng 68:**
```python
# CŨ: Xoay quanh trung tâm
rect = rotated.get_rect(
    center=(WIDTH // 2 + offset[0], SHIP_Y + offset[1])
)

# MỚI: Xoay quanh mũi (phía trên)
rect = rotated.get_rect(
    midtop=(WIDTH // 2 + offset[0], SHIP_Y - 40 + offset[1])
)
```

---

### 4. Disable xoay (luôn hướng lên)

Nếu muốn phi thuyền **không xoay**:

**Sửa trong `game.py` - Dòng 580:**
```python
# CŨ:
if self.locked and self.locked in self.enemies:
    draw_rotated_ship(self.win, self.angle, shake_offset)
else:
    draw_ship(self.win, shake_offset)

# MỚI: Luôn vẽ thẳng
draw_ship(self.win, shake_offset)
```

Hoặc đơn giản hơn, **giữ angle = 0** trong `_update_ship_aim()`:
```python
def _update_ship_aim(self):
    self.angle = 0.0  # Luôn hướng lên
```

---

## 📊 BẢNG TÓM TẮT

| Chức năng | File | Dòng | Code |
|-----------|------|------|------|
| **Khởi tạo angle** | `game.py` | 154 | `self.angle = 0.0` |
| **Tính góc xoay** | `game.py` | 182 | `self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))` |
| **Update angle** | `game.py` | 507 | `self._update_ship_aim()` |
| **Vẽ ship xoay** | `game.py` | 580 | `draw_rotated_ship(self.win, self.angle, shake_offset)` |
| **Chuyển radian→độ** | `ship.py` | 62 | `deg = -math.degrees(angle_rad) - 90` |
| **Xoay ảnh** | `ship.py` | 65 | `rotated = pygame.transform.rotate(_ship_img, deg)` |

---

## 🎯 VÍ DỤ THỰC TẾ

### Ví dụ 1: Enemy ở phía trên bên phải
```python
Enemy: (600, 100)
Ship: (400, 550)

Δx = 600 - 400 = 200
Δy = 100 - 550 = -450

angle = atan2(-450, 200) ≈ -1.19 rad ≈ -68°
deg = -(-68) - 90 = 68 - 90 = -22°

→ Ship xoay 22° sang phải ↗
```

### Ví dụ 2: Enemy ở phía trên bên trái
```python
Enemy: (200, 100)
Ship: (400, 550)

Δx = 200 - 400 = -200
Δy = 100 - 550 = -450

angle = atan2(-450, -200) ≈ -1.95 rad ≈ -112°
deg = -(-112) - 90 = 112 - 90 = 22°

→ Ship xoay 22° sang trái ↖
```

### Ví dụ 3: Enemy ở ngay giữa phía trên
```python
Enemy: (400, 100)
Ship: (400, 550)

Δx = 400 - 400 = 0
Δy = 100 - 550 = -450

angle = atan2(-450, 0) ≈ -1.57 rad ≈ -90°
deg = -(-90) - 90 = 90 - 90 = 0°

→ Ship hướng thẳng lên ↑
```

---

## 🔍 DEBUG TIPS

### In ra góc xoay để kiểm tra

Thêm vào `_update_ship_aim()`:
```python
if self.locked and self.locked in self.enemies:
    tx = self._enemy_center_x(self.locked)
    ty = self.locked.y
    self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))
    
    # DEBUG: In ra góc
    deg = math.degrees(self.angle)
    print(f"Ship angle: {self.angle:.2f} rad ({deg:.1f}°)")
```

### Vẽ đường ngắm để debug

Thêm vào method `draw()` sau khi vẽ ship:
```python
# DEBUG: Vẽ line từ ship đến enemy
if self.locked and self.locked in self.enemies:
    ship_x = WIDTH // 2
    ship_y = SHIP_Y
    enemy_x = self._enemy_center_x(self.locked)
    enemy_y = self.locked.y
    
    pygame.draw.line(self.win, (255, 0, 0), 
                    (ship_x, ship_y), 
                    (enemy_x, enemy_y), 2)
```

---

## 📝 TÓM TẮT NHANH

**Muốn thay đổi cách phi thuyền xoay?**

1. **Tốc độ xoay** → Sửa `game.py:182` (thêm interpolation)
2. **Giới hạn góc** → Sửa `game.py:182` (thêm clamp)
3. **Điểm xoay** → Sửa `ship.py:68` (thay center)
4. **Vô hiệu hóa** → Sửa `game.py:507` (giữ angle=0)
5. **Hiệu chỉnh hướng** → Sửa `ship.py:62` (thay -90)

**Công thức quan trọng nhất:**
```python
# game.py:182
self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))

# ship.py:62
deg = -math.degrees(angle_rad) - 90
```

---

*Hướng dẫn được tạo: 2025-01-20*
*Tất cả thông tin về xử lý hướng di chuyển phi thuyền*
