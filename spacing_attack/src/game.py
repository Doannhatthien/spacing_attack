# ============================================================
# PHẦN 1: IMPORT LIBRARIES & CONSTANTS
# ============================================================
import math                 # Tính toán góc, vector
import random              # Spawn ngẫu nhiên enemy, chọn từ
import pygame              # Framework game chính

# Import cấu hình game
from .settings import (
    WIDTH, HEIGHT,         # Kích thước màn hình (800x600)
    FPS,                   # Frame per second
    WHITE,                 # Màu trắng
    WORDS,                 # Danh sách từ vựng
    SPAWN_DELAYMS,        # Thời gian spawn enemy
    SHIP_Y                # Vị trí Y của tàu
)

# Import các module con
from .utils import load_image, load_sound
from .enemy import Enemy
from .bullet import Bullet
from .explosion import Explosion
from .ship import draw_ship, draw_rotated_ship

# Màu highlight enemy đang bị lock
YELLOW = (255, 255, 0)


# ============================================================
# PHẦN 2: CLASS GAME - KHỞI TẠO
# ============================================================
class Game:
    """
    Class quản lý toàn bộ game:
    - Khởi tạo pygame, màn hình, assets
    - Xử lý input (gõ phím)
    - Cập nhật logic (enemies, bullets, explosions)
    - Vẽ màn hình
    - Vòng lặp game chính
    """
    
    def __init__(self):
        """
        Khởi tạo game - thiết lập tất cả thành phần
        """
        # --------------------------------------------------
        # 2.1. PYGAME INITIALIZATION
        # --------------------------------------------------
        pygame.init()                           # Khởi tạo tất cả module pygame
        pygame.key.set_repeat(1, 1)            # Key repeat: delay=1ms, interval=1ms
        pygame.key.start_text_input()          # Bật text input (hỗ trợ IME)

        # --------------------------------------------------
        # 2.2. WINDOW & DISPLAY
        # --------------------------------------------------
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))  # Tạo cửa sổ game
        pygame.display.set_caption("Space Typing Game")      # Đặt tiêu đề
        self.clock = pygame.time.Clock()                      # Clock để kiểm soát FPS

        # --------------------------------------------------
        # 2.3. FONT & HUD (Head-Up Display)
        # --------------------------------------------------
        self.font = pygame.font.SysFont("Arial", 32)  # Font hiển thị text
        self.score = 0                                 # Điểm số
        self.lives = 3                                 # Số mạng
        self.typed_word = ""                           # Chuỗi ký tự đang gõ

        # --------------------------------------------------
        # 2.4. CHALLENGE MODE SUPPORT
        # --------------------------------------------------
        self.kills = 0                    # Số enemy đã tiêu diệt
        self.target_kills = None          # Mục tiêu kills (None = Classic mode)
        self.completed = False            # Cờ hoàn thành Challenge
        self.request_quit = False         # Cờ người chơi đóng cửa sổ
        self.game_over = False            # Cờ game over

        # --------------------------------------------------
        # 2.5. ASSETS - IMAGES
        # --------------------------------------------------
        try:
            # Load hình nền mặc định
            self.background = load_image("background.jpg", (WIDTH, HEIGHT))
        except Exception:
            # Nếu lỗi, dùng nền đen
            self.background = None
        
        # Load hình hiệu ứng nổ
        self.explosion_img = load_image("explosion.png", (40, 40))

        # --------------------------------------------------
        # 2.6. ASSETS - AUDIO (ĐÃ SỬA - ĐỔI ban.mp3 → ban.wav)
        # --------------------------------------------------
        try:
            # SỬA: Âm thanh bắn đạn - ĐỔI .mp3 → .wav
            self.shoot_sound = load_sound("ban.wav")  # ← ĐÃ SỬA
        except Exception:
            self.shoot_sound = None
        
        try:
            # Âm thanh gõ phím (nếu có file type.wav)
            self.type_sound = load_sound("type.wav")
        except Exception:
            self.type_sound = None
        
        try:
            # Âm thanh nổ
            self.explosion_sound = load_sound("no.mp3")
        except Exception:
            self.explosion_sound = None
        
        try:
            # Nhạc nền (loop vô hạn)
            pygame.mixer.music.load("assets/sounds/nhacnen.wav")
            pygame.mixer.music.set_volume(0.4)  # 40% volume
            pygame.mixer.music.play(-1)         # -1 = loop forever
        except Exception:
            pass  # Không có nhạc nền cũng OK

        # --------------------------------------------------
        # 2.7. GAME ENTITIES (Đối tượng trong game)
        # --------------------------------------------------
        self.enemies: list[Enemy] = []         # Danh sách kẻ địch
        self.bullets: list[Bullet] = []        # Danh sách đạn
        self.explosions: list[Explosion] = []  # Danh sách hiệu ứng nổ

        # --------------------------------------------------
        # 2.8. SPAWN TIMER
        # --------------------------------------------------
        self.last_spawn_ms = pygame.time.get_ticks()  # Thời điểm spawn cuối

        # --------------------------------------------------
        # 2.9. AIMING SYSTEM (Hệ thống nhắm bắn)
        # --------------------------------------------------
        self.locked: Enemy | None = None                  # Enemy đang bị lock
        self.target_pos: tuple[int, int] | None = None   # Tọa độ mục tiêu
        self.angle: float = 0.0                           # Góc xoay tàu (radians)


# ============================================================
# PHẦN 3: UTILITY METHODS (Phương thức tiện ích)
# ============================================================
    
    def _enemy_center_x(self, enemy: Enemy) -> int:
        """
        Tính tọa độ X chính giữa enemy (để tàu nhắm chính xác)
        
        Args:
            enemy: Enemy cần tính tâm
            
        Returns:
            int: Tọa độ X chính giữa (pixels)
        """
        # Tạo chuỗi hiển thị: "_" cho phần đã gõ, giữ nguyên phần chưa gõ
        shown = "_" * enemy.progress + enemy.origin_word[enemy.progress:]
        
        # Tính độ rộng text
        text_width = self.font.size(shown)[0]
        
        # Trả về X chính giữa = vị trí enemy + nửa chiều rộng
        return int(enemy.x + text_width / 2)

    def _update_ship_aim(self):
        """
        Cập nhật góc xoay tàu để nhắm về locked enemy
        Nếu không có locked enemy → tàu thẳng đứng
        """
        # Kiểm tra locked enemy còn tồn tại
        if self.locked in self.enemies:
            # Lấy tọa độ X chính giữa enemy
            tx = self._enemy_center_x(self.locked)
            # Lấy tọa độ Y enemy
            ty = self.locked.y
            # Lưu tọa độ mục tiêu
            self.target_pos = (tx, ty)
            
            # Tính góc từ tàu đến enemy (radians)
            # atan2(dy, dx) = góc từ trục X đến vector (dx, dy)
            self.angle = math.atan2(ty - SHIP_Y, tx - (WIDTH // 2))
        else:
            # Không có mục tiêu → reset
            self.target_pos = None


# ============================================================
# PHẦN 4: SPAWN SYSTEM (Hệ thống sinh enemy)
# ============================================================
    
    def spawn_enemy_if_needed(self):
        """
        Kiểm tra và spawn enemy mới nếu đã qua SPAWN_DELAYMS
        """
        # Lấy thời gian hiện tại (milliseconds)
        now = pygame.time.get_ticks()
        
        # Kiểm tra đã qua khoảng delay chưa (mặc định 2500ms)
        if now - self.last_spawn_ms > SPAWN_DELAYMS:
            # Tạo enemy mới với từ ngẫu nhiên
            new_enemy = Enemy(random.choice(WORDS))
            self.enemies.append(new_enemy)
            
            # Cập nhật thời điểm spawn
            self.last_spawn_ms = now


# ============================================================
# PHẦN 5: INPUT HANDLING (Xử lý đầu vào)
# ============================================================
    
    def handle_typed_char(self, ch: str):
        """
        Xử lý khi người chơi gõ ký tự
        
        Logic:
        1. Nếu chưa lock enemy → tìm enemy có ký tự đầu khớp → lock
        2. Nếu đã lock → kiểm tra ký tự tiếp theo
           - Đúng → bắn, cộng điểm, kiểm tra tiêu diệt
           - Sai → mất lock
        
        Args:
            ch: Ký tự vừa gõ (1 ký tự)
        """
        # --------------------------------------------------
        # 5.1. TRƯỜNG HỢP: CHƯA LOCK ENEMY
        # --------------------------------------------------
        if self.locked is None:
            # Tìm tất cả enemy có ký tự đầu khớp
            candidates = [e for e in self.enemies if e.required_char() == ch]
            
            if candidates:
                # Sắp xếp ưu tiên enemy gần đáy nhất (y lớn nhất)
                candidates.sort(key=lambda e: e.y, reverse=True)
                
                # Lock vào enemy đầu tiên
                self.locked = candidates[0]
                
                # Lưu ký tự đã gõ
                self.typed_word = ch
                
                # Tạo viên đạn bay về ký tự hiện tại (char_index = progress)
                bullet = Bullet(self.locked, ch, self.font, self.locked.progress)
                self.bullets.append(bullet)
                
                # Phát âm thanh bắn (ký tự đầu tiên)
                if self.shoot_sound:
                    self.shoot_sound.play()
                
                # Đánh dấu ký tự đã trúng (tăng progress)
                self.locked.hit_char(ch)
                
                # Kiểm tra enemy đã tiêu diệt chưa
                if self.locked.progress >= len(self.locked.origin_word):
                    # Cộng điểm = độ dài từ × 10
                    self.score += len(self.locked.origin_word) * 10
                    
                    # Tăng số kills
                    self.kills += 1
                    
                    # Tạo hiệu ứng nổ
                    self.explosions.append(Explosion(self.locked.x, self.locked.y))
                    
                    # Phát âm thanh nổ
                    if self.explosion_sound:
                        self.explosion_sound.play()
                    
                    # Xóa enemy
                    if self.locked in self.enemies:
                        self.enemies.remove(self.locked)
                    
                    # Reset lock
                    self.locked = None
                    self.typed_word = ""
                    
                    # Kiểm tra hoàn thành Challenge
                    if self.target_kills is not None and self.kills >= self.target_kills:
                        self.completed = True
        
        # --------------------------------------------------
        # 5.2. TRƯỜNG HỢP: ĐÃ LOCK ENEMY
        # --------------------------------------------------
        else:
            # Kiểm tra ký tự tiếp theo có khớp không
            if self.locked.required_char() == ch:
                # Thêm ký tự vào typed_word
                self.typed_word += ch
                
                # Tạo viên đạn mới
                bullet = Bullet(self.locked, ch, self.font, self.locked.progress)
                self.bullets.append(bullet)
                
                # ✅ SỬA: Phát âm thanh gõ phím (nếu có), không phải shoot_sound
                if self.type_sound:
                    self.type_sound.play()
                # Fallback: nếu không có type_sound, dùng shoot_sound
                elif self.shoot_sound:
                    self.shoot_sound.play()
                
                # Đánh dấu ký tự trúng
                self.locked.hit_char(ch)
                
                # Kiểm tra tiêu diệt
                if self.locked.is_complete():
                    # Cộng điểm
                    self.score += len(self.locked.origin_word) * 10
                    self.kills += 1
                    
                    # Hiệu ứng nổ
                    self.explosions.append(Explosion(self.locked.x, self.locked.y))
                    if self.explosion_sound:
                        self.explosion_sound.play()
                    
                    # Xóa enemy
                    if self.locked in self.enemies:
                        self.enemies.remove(self.locked)
                    
                    # Reset
                    self.locked = None
                    self.typed_word = ""
                    
                    # Kiểm tra Challenge
                    if self.target_kills is not None and self.kills >= self.target_kills:
                        self.completed = True
            else:
                # Gõ sai → mất lock
                self.locked = None
                self.typed_word = ""

    def handle_keydown(self, event):
        """
        Xử lý các phím điều khiển đặc biệt
        
        Args:
            event: Pygame KEYDOWN event
        """
        # ESC: Hủy lock
        if event.key == pygame.K_ESCAPE:
            self.locked = None
            self.typed_word = ""
        
        # Backspace: Xóa ký tự cuối
        elif event.key == pygame.K_BACKSPACE:
            if self.typed_word:
                self.typed_word = self.typed_word[:-1]


# ============================================================
# PHẦN 6: UPDATE METHODS (Cập nhật logic game)
# ============================================================
    
# ... các phần khác giữ nguyên ...

    def update_bullets(self):
        """
        Cập nhật trạng thái tất cả viên đạn:
        - Di chuyển
        - Xóa ngay khi trúng đích (không phụ thuộc enemy còn tồn tại trong danh sách)
        - Xóa nếu ra ngoài màn hình
        """
        for b in self.bullets[:]:
            b.move()

            # Nếu đạn đã chạm mục tiêu snapshot → remove ngay
            if b.is_hit():
                if b in self.bullets:
                    self.bullets.remove(b)
                continue

           # loại bỏ nếu bay ra khỏi màn hình
            if b.is_out_of_bounds():
                if b in self.bullets:
                    self.bullets.remove(b)

    def update_enemies(self):
        """
        Cập nhật tất cả enemy:
        - Di chuyển xuống
        - Kiểm tra chạm đáy (mất mạng)
        - Xóa enemy chạm đáy
        """
        # Duyệt qua copy danh sách
        for enemy in self.enemies[:]:
            # Di chuyển enemy xuống (y += speed)
            enemy.move()
            
            # Kiểm tra chạm đáy (y > 600)
            if enemy.y > 600:
                # Xóa enemy
                if enemy in self.enemies:
                    self.enemies.remove(enemy)
                
                # Trừ 1 mạng
                self.lives -= 1
                
                # Hủy lock nếu enemy này đang bị lock
                if enemy is self.locked:
                    self.locked = None
                    self.typed_word = ""

    def update_explosions(self):
        """
        Cập nhật hiệu ứng nổ:
        - Giảm timer
        - Xóa explosion hết thời gian
        """
        # Duyệt qua copy danh sách
        for explosion in self.explosions[:]:
            # Kiểm tra hết thời gian
            if explosion.timer <= 0:
                self.explosions.remove(explosion)
            else:
                # Giảm timer (countdown)
                explosion.timer -= 1


# ============================================================
# PHẦN 7: RENDER METHOD (Vẽ màn hình)
# ============================================================
    
    def draw(self):
        """
        Vẽ tất cả đối tượng lên màn hình theo thứ tự:
        1. Background
        2. Enemies
        3. Bullets
        4. Explosions
        5. Ship
        6. HUD (Score, Lives, Locked, Typing, Kills)
        """
        # --------------------------------------------------
        # 7.1. VẼ BACKGROUND
        # --------------------------------------------------
        if self.background:
            self.win.blit(self.background, (0, 0))
        else:
            self.win.fill((0, 0, 0))  # Nền đen

        # --------------------------------------------------
        # 7.2. VẼ ENEMIES
        # --------------------------------------------------
        for enemy in self.enemies:
            if enemy is self.locked:
                # Enemy đang lock → màu vàng
                enemy.draw(self.win, self.font, YELLOW)
            else:
                # Enemy bình thường → màu đỏ (default)
                enemy.draw(self.win, self.font)

        # --------------------------------------------------
        # 7.3. VẼ BULLETS
        # --------------------------------------------------
        for bullet in self.bullets:
            bullet.draw(self.win)

        # --------------------------------------------------
        # 7.4. VẼ EXPLOSIONS
        # --------------------------------------------------
        for explosion in self.explosions:
            explosion.draw(self.win, self.explosion_img)

        # --------------------------------------------------
        # 7.5. VẼ SHIP (Tàu vũ trụ)
        # --------------------------------------------------
        if self.target_pos is not None:
            # Tàu xoay theo góc nhắm
            draw_rotated_ship(self.win, self.angle)
        else:
            # Tàu thẳng đứng
            draw_ship(self.win)

        # --------------------------------------------------
        # 7.6. VẼ HUD (Head-Up Display)
        # --------------------------------------------------
        # Render các text
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        typed_text = self.font.render(f"Typing: {self.typed_word}", True, WHITE)
        
        # Tên enemy đang lock (hoặc '-')
        locked_name = self.locked.origin_word if self.locked else '-'
        locked_text = self.font.render(f"Locked: {locked_name}", True, WHITE)

        # Hiển thị Kills nếu là Challenge mode
        if self.target_kills is not None:
            kills_text = self.font.render(
                f"Kills: {self.kills}/{self.target_kills}", 
                True, 
                WHITE
            )
            self.win.blit(kills_text, (10, 130))

        # Vẽ HUD lên màn hình
        self.win.blit(score_text, (10, 10))           # Góc trên trái
        self.win.blit(lives_text, (10, 50))           # Dưới Score
        self.win.blit(locked_text, (10, 90))          # Dưới Lives
        self.win.blit(typed_text, (10, HEIGHT - 50))  # Góc dưới trái

        # --------------------------------------------------
        # 7.7. CẬP NHẬT MÀN HÌNH
        # --------------------------------------------------
        pygame.display.flip()  # Flip buffer → hiển thị


# ============================================================
# PHẦN 8: GAME LOOP (Vòng lặp game chính)
# ============================================================
    
    def run(self):
        """
        Vòng lặp game chính:
        1. Xử lý events (QUIT, KEYDOWN, TEXTINPUT)
        2. Spawn enemies
        3. Cập nhật logic (enemies, bullets, explosions, aim)
        4. Kiểm tra điều kiện kết thúc
        5. Vẽ màn hình
        6. Điều khiển FPS
        
        Kết thúc khi:
        - Người chơi đóng cửa sổ (QUIT)
        - Hết mạng (lives <= 0)
        - Hoàn thành Challenge (kills >= target_kills)
        """
        # Cờ điều khiển vòng lặp
        running = True
        
        # --------------------------------------------------
        # 8.1. VÒNG LẶP CHÍNH
        # --------------------------------------------------
        while running:
            # ==================== EVENT HANDLING ====================
            for event in pygame.event.get():
                # QUIT: Người chơi đóng cửa sổ
                if event.type == pygame.QUIT:
                    self.request_quit = True
                    pygame.key.stop_text_input()
                    return  # Thoát ngay
                
                # KEYDOWN: Phím điều khiển (ESC, Backspace)
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)
                
                # TEXTINPUT: Ký tự từ hệ điều hành (không bỏ sót)
                elif event.type == pygame.TEXTINPUT:
                    self.handle_typed_char(event.text)

            # ==================== SPAWN ====================
            self.spawn_enemy_if_needed()

            # ==================== UPDATE ====================
            self.update_enemies()      # Cập nhật enemies
            self.update_bullets()      # Cập nhật bullets
            self.update_explosions()   # Cập nhật explosions
            self._update_ship_aim()    # Cập nhật góc xoay tàu

            # ==================== CHECK END CONDITIONS ====================
            # Hết mạng
            if self.lives <= 0:
                running = False
            
            # Hoàn thành Challenge
            if self.target_kills is not None and self.completed:
                running = False

            # ==================== RENDER ====================
            self.draw()

            # ==================== FPS CONTROL ====================
            self.clock.tick(120)  # 120 FPS (mượt, responsive)

        # --------------------------------------------------
        # 8.2. SAU KHI THOÁT VÒNG LẶP
        # --------------------------------------------------
        # Tắt text input
        pygame.key.stop_text_input()
        
        # Hiển thị Game Over (chỉ cho Classic mode, không phải QUIT)
        if self.target_kills is None and not self.request_quit:
            # Vẽ background
            if self.background:
                self.win.blit(self.background, (0, 0))
            else:
                self.win.fill((0, 0, 0))
            
            # Render text "Game Over! Score: xxx"
            end_text = self.font.render(
                f"Game Over! Score: {self.score}", 
                True, 
                WHITE
            )
            
            # Vẽ ở giữa màn hình
            self.win.blit(end_text, (WIDTH // 2 - 180, HEIGHT // 2 - 20))
            
            # Cập nhật màn hình
            pygame.display.flip()
            
            # Chờ 1.2 giây
            pygame.time.wait(1200)