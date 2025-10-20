# 🎯 Hệ Thống Chuyển Động Thông Minh Của Enemy

## 🚀 Tính Năng Mới

### 1. 📊 Tốc Độ Đa Dạng
Mỗi enemy có tốc độ khác nhau:
- **Chậm:** 1.5 - 2.5 px/frame (màu hồng nhạt)
- **Trung bình:** 2.5 - 3.5 px/frame (màu đỏ nhạt)
- **Nhanh:** 3.5 - 5.0 px/frame (màu đỏ vừa)
- **Rất nhanh:** > 5.0 px/frame (màu đỏ sáng)

### 2. ⚡ Gia Tốc
- **60%** enemy rơi với tốc độ đều
- **40%** enemy tăng tốc dần khi rơi
- Enemy có gia tốc sẽ có **trail effect** phía sau
- Có **speed bar** màu đỏ khi tốc độ > 4

### 3. 🌊 4 Loại Chuyển Động

#### 🎯 Straight (Thẳng)
- Rơi thẳng xuống
- Đơn giản và dễ đoán
- Chiếm ~25% enemies

#### 🎵 Swing (Lắc lư)
- Lắc lư mượt mà như con lắc
- Di chuyển theo sine wave
- Khó bắn hơn straight
- Chiếm ~25% enemies

#### ⚡ Zigzag (Răng cưa)
- Di chuyển zigzag sắc nét
- Thay đổi hướng đột ngột
- Rất khó dự đoán
- Có **indicator màu tím** 💜
- Chiếm ~25% enemies

#### 🌀 Spiral (Xoắn ốc)
- Biên độ lắc tăng dần
- Tạo quỹ đạo xoắn ốc
- Cực kỳ khó nhắm
- Có **indicator màu xanh** 🔵
- Chiếm ~25% enemies

### 4. 🎯 Hướng Về Phi Thuyền
- **25%** enemies sẽ hướng về phi thuyền
- Di chuyển ngang về phía giữa màn hình
- Có **glow effect màu vàng** nhấp nháy
- NGUY HIỂM HƠN - ưu tiên tiêu diệt!

## 🎨 Visual Indicators

### Màu Sắc Theo Tốc Độ
```
Tốc độ > 5.0:  🔴 Đỏ sáng (255, 50, 50)
Tốc độ > 3.5:  🔴 Đỏ vừa (255, 100, 100)
Tốc độ > 2.5:  🔴 Đỏ nhạt (255, 150, 150)
Tốc độ < 2.5:  💗 Hồng nhạt (255, 200, 200)
```

### Hiệu Ứng Đặc Biệt

#### 🌟 Glow Effect (Hướng về phi thuyền)
- Viền sáng màu vàng cam
- Nhấp nháy nhẹ
- 8 lớp offset tạo hiệu ứng phát sáng

#### 💨 Trail Effect (Có gia tốc)
- Bóng mờ phía sau
- Độ mờ tăng theo gia tốc
- Cho cảm giác tốc độ

#### 📊 Speed Bar (Tốc độ > 4)
- Thanh bar nhỏ phía trên enemy
- Màu từ vàng → cam → đỏ
- Hiển thị tốc độ real-time

#### 🔵 Movement Indicators
- **Spiral:** Vòng tròn nhỏ màu xanh
- **Zigzag:** Đường zigzag màu tím

## 🎮 Chiến Thuật Chơi Game

### Ưu Tiên Tiêu Diệt

1. **🔴⚡ Đỏ + Glow vàng:** Nhanh VÀ hướng về phi thuyền - CỰC NGUY HIỂM!
2. **🔴 Đỏ sáng:** Tốc độ rất cao - nguy hiểm
3. **🌟 Glow vàng:** Đang hướng về phi thuyền
4. **🌀 Spiral/Zigzag:** Khó bắn - xử lý sớm
5. **🎵 Swing:** Vừa phải
6. **🎯 Straight chậm:** Dễ nhất - để sau cũng được

### Tips

- **Quan sát màu sắc:** Màu đỏ càng đậm = càng nguy hiểm
- **Chú ý glow vàng:** Enemy đang tiến gần phi thuyền
- **Ưu tiên speed bar:** Nếu thấy speed bar đỏ = tiêu diệt ngay
- **Zigzag/Spiral:** Bắn khi chúng ở giữa quỹ đạo
- **Swing:** Bắn khi đang chuyển hướng (tốc độ ngang = 0)

## 🔧 Tham Số Điều Chỉnh

Trong `src/enemy.py`:

```python
# Tốc độ
base_speed: 1.5 - 4.5  # Tốc độ ban đầu
acceleration: 0, 0.015, 0.025, 0.035  # Gia tốc

# Swing
swing_amplitude: 20 - 40  # Biên độ lắc
swing_frequency: 0.015 - 0.035  # Tần số

# Zigzag
swing_amplitude: 30 - 50
swing_frequency: 0.05 - 0.08

# Spiral
swing_amplitude: 15 - 35
swing_frequency: 0.03 - 0.05
spiral_growth: 0.3 - 0.6  # Tốc độ tăng biên độ

# Target ship
target_ship: 25% chance
horizontal_speed: 0.3 - 0.8
```

## 📊 Thống Kê Phân Bố

| Loại | Tỷ Lệ | Độ Khó |
|------|-------|--------|
| Straight | 25% | ⭐ |
| Swing | 25% | ⭐⭐ |
| Zigzag | 25% | ⭐⭐⭐ |
| Spiral | 25% | ⭐⭐⭐⭐ |
| + Target Ship | +25% | +⭐⭐ |
| + Acceleration | +40% | +⭐ |

## 🎯 Kết Hợp Nguy Hiểm Nhất

**💀 The Perfect Storm:**
- Spiral movement 🌀
- High acceleration ⚡
- Target ship 🎯
- Speed > 5 🔴

Xác suất: ~2.5% (hiếm nhưng CỰC NGUY HIỂM!)

## 🔮 Tương Lai

Có thể thêm:
- [ ] Pause/slow motion khi enemy gần phi thuyền
- [ ] Combo multiplier khi tiêu diệt nhanh
- [ ] Power-up làm chậm enemies
- [ ] Boss enemies với pattern đặc biệt
- [ ] Weather effects ảnh hưởng chuyển động

---

**Chúc bạn chơi game vui vẻ với hệ thống enemy thông minh mới! 🎮✨**
