# 🎯 HỆ THỐNG HƯỚNG VỀ PHI THUYỀN & VA CHẠM

## 🚀 Tổng Quan

Enemy giờ đây di chuyển **THÔNG MINH HƠN** - không chỉ rơi thẳng mà còn **HƯỚNG VỀ PHI THUYỀN** để tấn công! Phi thuyền có **3 MẠNG** và sẽ **PHÁT NỔ** khi hết mạng!

---

## ✨ Tính Năng Mới

### 1. 🎯 **Enemy Targeting System**

#### Chuyển Động Thông Minh
- ✅ Enemy **RƠI TỪ TỪ** (giữ nguyên tốc độ chậm)
- ✅ Đồng thời **DI CHUYỂN NGANG** để hướng về phi thuyền
- ✅ Tạo **ĐƯỜNG CONG MƯỢT** khi tiến đến mục tiêu
- ✅ **TĂNG TỐC** khi gần phi thuyền (3 giai đoạn)

#### 3 Giai Đoạn Tăng Tốc
```
0-30% đường:  Chậm (40% tốc độ base)  🟢
30-70% đường: Vừa (80% tốc độ base)   🟡
70-100% đường: Nhanh (120% tốc độ)    🔴 LAO VÀO!
```

#### Visual Indicator
- 🎯 **Mũi tên màu vàng** hiển thị hướng di chuyển
  - ➡️ Mũi tên phải: Enemy đang đi sang phải
  - ⬅️ Mũi tên trái: Enemy đang đi sang trái

---

### 2. 💥 **Hệ Thống Va Chạm**

#### Collision Detection
- ✅ Kiểm tra khoảng cách giữa Enemy và Phi thuyền
- ✅ Bán kính va chạm: **40 pixels**
- ✅ Tính toán chính xác với công thức `√(dx² + dy²)`

#### Khi Enemy Chạm Phi Thuyền
1. 💔 **Mất 1 mạng** (Lives giảm 1)
2. 💥 **Explosion lớn** tại vị trí phi thuyền (40 frames)
3. 🔨 **Screen shake mạnh** (intensity 20, duration 20)
4. 🔊 **Sound effect nổ**
5. 🛡️ **Bất tử tạm thời** 1 giây (60 frames)
6. ✨ **Phi thuyền nhấp nháy** trong lúc bất tử
7. ❌ **Enemy bị xóa** khỏi màn hình

---

### 3. ❤️ **Lives System**

#### Hiển Thị
```
3 mạng: ❤❤❤  (Màu trắng)
2 mạng: ❤❤🖤  (Màu vàng - cảnh báo)
1 mạng: ❤🖤🖤  (Màu đỏ - nguy hiểm!)
0 mạng: 💥 GAME OVER
```

#### Bảo Vệ
- 🛡️ **Invulnerability Timer**: 1 giây sau khi bị hit
- ✨ **Flash Effect**: Phi thuyền nhấp nháy khi bất tử
- 🚫 Không nhận damage trong thời gian bất tử

---

### 4. ⚠️ **Warning System**

#### DANGER Alert
- Khi enemy ở trong vùng nguy hiểm (100 pixels trên phi thuyền)
- Text "⚠️ DANGER! ⚠️" xuất hiện giữa màn hình
- Nhấp nháy đỏ/cam để cảnh báo
- Giúp người chơi tập trung vào mối đe dọa

---

## 🎮 Gameplay

### Chiến Thuật Mới

#### 1️⃣ **Ưu Tiên Mục Tiêu**
```
Priority 1: Enemy gần phi thuyền (y > 450) 🔴
Priority 2: Enemy đang di chuyển ngang nhanh 🟡
Priority 3: Enemy từ dài (nhiều HP) 🟢
Priority 4: Enemy từ ngắn 🔵
```

#### 2️⃣ **Quản Lý Lives**
- ❤️❤️❤️ 3 Lives: Chơi bình thường, có thể mạo hiểm
- ❤️❤️🖤 2 Lives: Cẩn trọng hơn, tập trung enemy nguy hiểm
- ❤️🖤🖤 1 Life: CỰC KỲ CẢNH GIÁC! Ưu tiên sống sót

#### 3️⃣ **Sử Dụng Invulnerability**
- Tận dụng 1 giây bất tử sau khi bị hit
- Thời gian này để clear enemy gần phi thuyền
- Đừng lãng phí thời gian!

---

## 📊 Technical Details

### Enemy Movement Algorithm

```python
# Rơi xuống (vertical)
y += speed

# Di chuyển ngang về phía phi thuyền (horizontal)
dx = target_x - current_x
if abs(dx) > 5:
    x += sign(dx) * horizontal_speed

# Tăng tốc theo giai đoạn
progress = y / 600
if progress < 0.3:
    horizontal_speed = base_speed * 0.4
elif progress < 0.7:
    horizontal_speed = base_speed * 0.8
else:
    horizontal_speed = base_speed * 1.2
```

### Collision Detection

```python
# Tính khoảng cách
dx = enemy.x - ship_x
dy = enemy.y - ship_y
distance = √(dx² + dy²)

# Va chạm
collision = distance < ship_radius (40)
```

---

## 🎯 Tips & Tricks

### 🏆 **Survival Tips**

1. **Luôn theo dõi warning**
   - Khi thấy ⚠️ DANGER!, drop everything!
   - Focus vào enemy gần nhất

2. **Gõ nhanh và chính xác**
   - Tốc độ > độ chính xác khi enemy gần
   - Sai 1 chữ = mất lock = mất thời gian quý báu

3. **Quản lý nhiều target**
   - Luôn biết enemy nào gần nhất
   - Lock enemy nguy hiểm trước

4. **Tận dụng screen space**
   - Enemy ở xa phi thuyền = ít nguy hiểm hơn
   - Priority: Bottom > Middle > Top

### 💡 **Advanced Tactics**

- **Combo Lock**: Giữ lock 1 enemy cho đến khi destroy
- **Quick Switch**: Chuyển target nhanh khi cần
- **Defensive Play**: Khi ít mạng, focus survival > score
- **Aggressive Play**: Khi nhiều mạng, maximize score

---

## 📈 Thống Kê

### Độ Khó

| Lives | Difficulty | Strategy |
|-------|-----------|----------|
| 3 ❤❤❤ | Easy | Aggressive |
| 2 ❤❤🖤 | Medium | Balanced |
| 1 ❤🖤🖤 | Hard | Defensive |

### Scoring

| Action | Points |
|--------|--------|
| Destroy enemy | Word length × 10 |
| Survive hit | -0 (but lose life!) |
| Perfect clear | Bonus multiplier |

---

## 🎨 Visual Effects

### Khi Enemy Di Chuyển
- 🎯 Mũi tên màu vàng chỉ hướng
- 🌈 Màu text thay đổi theo tốc độ
- 💚 HP bar trên enemy

### Khi Va Chạm
- 💥 Explosion lớn (40 frames)
- ✨ Particles bay tứ tung
- ⚡ Flash effect sáng
- 🔨 Screen shake mạnh
- ⭐ Phi thuyền nhấp nháy

### HUD Updates
- ❤️ Hearts hiển thị lives
- 🟢 Xanh khi khỏe (3 lives)
- 🟡 Vàng khi cảnh báo (2 lives)
- 🔴 Đỏ khi nguy hiểm (1 life)

---

## 🚀 Next Steps

### Possible Improvements
- [ ] Boss enemies với nhiều mạng hơn
- [ ] Power-ups (shield, slow-motion)
- [ ] Combo system (destroy nhiều enemy liên tiếp)
- [ ] Difficulty scaling (tăng dần theo thời gian)
- [ ] Achievements system
- [ ] Online leaderboard

---

## 🎮 Kết Luận

Hệ thống mới tạo ra gameplay **THÁCH THỨC và HỒNG HỘI HƠN**:

✅ Enemy thông minh hơn (targeting)
✅ Nguy hiểm hơn (collision)
✅ Nhiều tầng lớp hơn (lives, invulnerability)
✅ Visual feedback tốt hơn (warnings, effects)
✅ Cần kỹ năng cao hơn (priority, timing)

**Chúc bạn chinh phục game mới! 🎯🚀**

---

*Phiên bản: 2.0 - Smart Targeting & Collision System*
*Ngày cập nhật: October 2025*
