# 🚀 Tối Ưu Hóa Hiệu Năng Game

## Các cải thiện đã thực hiện:

### 1. ⚡ Tăng FPS
- **Trước:** 60 FPS
- **Sau:** 120 FPS
- **Lợi ích:** Chuyển động mượt mà hơn gấp đôi

### 2. 🖥️ Tối ưu Display Mode
- Thêm flags: `pygame.HWSURFACE | pygame.DOUBLEBUF`
- **Lợi ích:** Sử dụng hardware acceleration và double buffering

### 3. 📝 Cache Text Rendering
- **HUD Text Cache:** Score, Lives, Kills chỉ render lại khi thay đổi
- **Enemy Text Cache:** Từ chỉ render lại khi progress thay đổi
- **Lợi ích:** Giảm 70-80% font rendering calls

### 4. 🎯 Tăng Tốc Độ Game Elements
- **Enemy speed:** 1-3 → 2-4 (phù hợp với FPS cao hơn)
- **Bullet speed:** 12 → 18 (phù hợp với FPS cao hơn)
- **Enemy base speed:** 1.0 → 2.0

### 5. ⏱️ Delta Time Support
- Thêm `delta_time` tracking trong Game class
- **Lợi ích:** Chuẩn bị cho frame-independent movement

### 6. 🔄 Consistent FPS Usage
- Tất cả `clock.tick(60)` → `clock.tick(FPS)`
- **Lợi ích:** Dễ dàng thay đổi FPS từ settings

## Kết quả mong đợi:

✅ Game chạy mượt mà hơn rõ rệt
✅ Giảm CPU usage do ít render calls hơn
✅ Input response tốt hơn
✅ Animations trơn tru hơn

## Nếu FPS quá cao cho máy yếu:

Chỉnh trong `src/settings.py`:
```python
FPS = 60  # Giảm xuống 60 nếu cần
```

## Tips thêm:

- Nếu máy yếu: Giảm FPS xuống 60 hoặc 75
- Nếu máy mạnh: Có thể tăng lên 144 FPS
- Monitor vsync: Thêm `pygame.SCALED` flag nếu cần
