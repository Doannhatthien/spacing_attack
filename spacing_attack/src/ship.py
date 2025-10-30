# ============================================================
# ship.py — Xử lý hiển thị tàu vũ trụ (Spaceship)
# ============================================================

import pygame, math
from .utils import load_image      # Hàm tiện ích để tải hình ảnh
from .settings import WIDTH, SHIP_Y  # Lấy kích thước màn hình & vị trí Y của tàu


# Biến toàn cục lưu ảnh tàu — Cache cho nhiều skin
_ship_images = {}  # Dictionary lưu các skin đã load
_current_skin = None  # Skin hiện tại đang sử dụng


# ------------------------------------------------------------
# Hàm khởi tạo ảnh tàu (_init_ship) - 
# ------------------------------------------------------------
def _init_ship(ship_skin="spaceship.png"):
    """
    Hàm này dùng để tải hình ảnh tàu vũ trụ theo skin.
    - ship_skin: Tên file ảnh (ví dụ: "spaceship.png", "ship2.png", "ship3.png")
    - Cache các skin đã load để tránh load lại nhiều lần
    - Kích thước mặc định: (60, 60)
    """
    global _ship_images, _current_skin
    
    # Nếu skin này chưa được load
    if ship_skin not in _ship_images:
        # Thay đổi kích thước cho phi thuyền
        img = load_image(ship_skin, (60, 60))  # Tải ảnh và resize
        if img.get_alpha() is None:            # Nếu ảnh không có kênh alpha
            bg_color = img.get_at((0, 0))[:3]  # Lấy màu nền
            img.set_colorkey(bg_color)         # Đặt màu nền trong suốt
        _ship_images[ship_skin] = img          # Lưu vào cache
        print(f"[SHIP] ✅ Loaded skin: {ship_skin}")
    
    _current_skin = ship_skin  # Lưu skin hiện tại
# ------------------------------------------------------------
# Hàm vẽ tàu bình thường (không xoay) - HỖ TRỢ SKIN
# ------------------------------------------------------------
def draw_ship(surface: pygame.Surface, offset=(0, 0), center_x=None, ship_skin="spaceship.png"):
    """
    Vẽ tàu vũ trụ ở vị trí mặc định.
    - surface: đối tượng pygame.Surface (màn hình đích để vẽ lên)
    - offset: cho phép dịch chuyển tàu (dùng trong hiệu ứng rung màn hình)
    - center_x: vị trí X của tàu (None = giữa màn hình)
    - ship_skin: tên file ảnh skin (mặc định "spaceship.png")
    """
    _init_ship(ship_skin)  # Đảm bảo skin đã được tải
    
    # Lấy ảnh từ cache
    ship_img = _ship_images.get(ship_skin)
    if ship_img is None:
        return  # Không vẽ nếu không load được
    
    # Xác định vị trí X
    if center_x is None:
        center_x = WIDTH // 2

    rect = ship_img.get_rect(
        center=(center_x + offset[0], SHIP_Y + offset[1])
    )
    surface.blit(ship_img, rect)  # Vẽ ảnh tàu lên màn hình


# ------------------------------------------------------------
# Hàm vẽ tàu xoay theo góc (dùng khi ngắm kẻ địch) - HỖ TRỢ SKIN
# ------------------------------------------------------------
def draw_rotated_ship(surface: pygame.Surface, angle_rad: float, offset=(0, 0), center_x=None, ship_skin="spaceship.png"):
    """
    Vẽ tàu vũ trụ với góc xoay nhất định (angle_rad — tính bằng radian).
    - Dùng trong trường hợp tàu tự động xoay nòng súng hướng về enemy bị lock.
    - offset: dùng cho hiệu ứng rung hoặc dịch chuyển nhẹ
    - center_x: vị trí X của tàu (None = giữa màn hình)
    - ship_skin: tên file ảnh skin
    """
    _init_ship(ship_skin)  # Đảm bảo skin đã được tải
    
    # Lấy ảnh từ cache
    ship_img = _ship_images.get(ship_skin)
    if ship_img is None:
        return  # Không vẽ nếu không load được
    
    # Chuyển góc từ radian sang độ, đồng thời trừ 90 độ để điều chỉnh hướng mũi tàu cho đúng
    deg = -math.degrees(angle_rad) - 90  

    # Xoay ảnh theo góc đã tính
    rotated = pygame.transform.rotate(ship_img, deg)
    # nếu muốn phi thuyền không xoay dùng hàm này
    #rotated = ship_img

    # Lấy vị trí trung tâm mới sau khi xoay
    if center_x is None:
        center_x = WIDTH // 2

    rect = rotated.get_rect(
        center=(center_x + offset[0], SHIP_Y + offset[1])
    )

    # Vẽ ảnh xoay lên màn hình
    surface.blit(rotated, rect)

