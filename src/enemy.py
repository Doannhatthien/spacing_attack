import random
import pygame
import math

class Enemy:
    def __init__(self, word: str, existing_enemies=None, use_challenge_speed=False, challenge_speed=None):
        self.origin_word = word
        self.progress = 0  # Số ký tự đã gõ đúng
        
        # Vị trí xuất phát - TỰ ĐỘNG TRÁNH CÁC ENEMY KHÁC
        self.x, self.y = self._find_spawn_position(existing_enemies)
        
        # Tốc độ phụ thuộc vào độ dài từ
        word_length = len(word)
        
        if use_challenge_speed and challenge_speed is not None:
            # CHALLENGE MODE: Sử dụng tốc độ từ CHALLENGE_LEVELS
            # Điều chỉnh theo độ dài từ (nhân hệ số)
            if word_length <= 4:  # Từ ngắn - Rơi nhanh hơn
                speed_multiplier = 1.2
            elif word_length <= 7:  # Từ trung bình
                speed_multiplier = 1.0
            elif word_length <= 10:  # Từ dài - Rơi chậm hơn
                speed_multiplier = 0.8
            else:  # Từ rất dài - Rơi rất chậm
                speed_multiplier = 0.6
            
            self.base_speed = challenge_speed * speed_multiplier
        else:
            # CLASSIC MODE: Giữ nguyên logic cũ - tốc độ cực chậm
            if word_length <= 4:  # Từ ngắn (3-4 ký tự) - Rơi cực chậm
                self.base_speed = random.uniform(0.2, 0.35)  # Giảm thêm
            elif word_length <= 7:  # Từ trung bình (5-7 ký tự) - Rơi siêu chậm
                self.base_speed = random.uniform(0.15, 0.25)
            elif word_length <= 10:  # Từ dài (8-10 ký tự) - Rơi cực kỳ chậm
                self.base_speed = random.uniform(0.1, 0.2)
            else:  # Từ rất dài (11+ ký tự) - Rơi như rùa bò
                self.base_speed = random.uniform(0.08, 0.15)
        
        self.speed = self.base_speed
        
        # Gia tốc - LOẠI BỎ hoàn toàn để chuyển động mượt hơn
        self.acceleration = 0  # Không có gia tốc, chuyển động đều
        
        # Chuyển động thông minh - HƯỚNG VỀ PHI THUYỀN
        self.movement_type = 'smart'  # Di chuyển thông minh
        self.time = 0  # Bộ đếm thời gian
        
        # Target phi thuyền (luôn luôn hướng về phi thuyền)
        self.target_ship = True
        self.target_x = 400  # Vị trí phi thuyền (giữa màn hình, WIDTH // 2)
        self.target_y = 550  # Vị trí Y của phi thuyền
        
        # Tốc độ di chuyển ngang (hướng về phi thuyền)
        # Chậm hơn tốc độ rơi để tạo đường cong mượt
        self.horizontal_speed = self.base_speed * 0.6  # 60% tốc độ rơi
        
        # Lưu vị trí ban đầu
        self.start_x = self.x
        self.start_y = self.y
        
        # Cache rendering
        self._cached_text = None
        self._cached_progress = -1
        
        # Lưu vị trí X gốc để tính swing
        self.base_x = self.x
        
        # Collision avoidance (tránh chồng lên nhau)
        self.collision_offset_x = 0
        self.collision_offset_y = 0
        
        # HP System - thanh máu
        self.max_hp = len(word)  # Máu = số ký tự trong từ
        self.current_hp = self.max_hp
    
    def _find_spawn_position(self, existing_enemies):
        """Tìm vị trí spawn không chồng lên enemy khác"""
        max_attempts = 20
        min_spawn_distance = 120  # Khoảng cách tối thiểu giữa các enemy khi spawn
        
        for attempt in range(max_attempts):
            x = random.randint(50, 750)
            y = random.randint(-200, -50)  # Tăng vùng spawn lên trên
            
            # Kiểm tra khoảng cách với các enemy hiện có
            if existing_enemies:
                too_close = False
                for other in existing_enemies:
                    dx = x - other.x
                    dy = y - other.y
                    distance = math.sqrt(dx * dx + dy * dy)
                    
                    if distance < min_spawn_distance:
                        too_close = True
                        break
                
                if not too_close:
                    return (x, y)
            else:
                return (x, y)
        
        # Nếu không tìm được vị trí tốt, spawn ở vùng xa
        return (random.randint(100, 700), random.randint(-300, -150))

    def move(self, other_enemies=None):
        """Di chuyển enemy xuống dưới - HƯỚNG VỀ PHI THUYỀN với collision avoidance"""
        self.time += 1
        
        # 1. Di chuyển theo trục Y (rơi xuống)
        self.y += self.speed
        
        # 2. Di chuyển theo trục X (hướng về phi thuyền)
        dx = self.target_x - self.x  # Khoảng cách đến phi thuyền
        
        if abs(dx) > 5:  # Chỉ di chuyển nếu chưa ở giữa
            # Di chuyển từ từ về phía phi thuyền
            if dx > 0:
                self.x += min(self.horizontal_speed, abs(dx))  # Di chuyển phải
            else:
                self.x -= min(self.horizontal_speed, abs(dx))  # Di chuyển trái
        
        # 3. Tạo đường cong mượt mà (optional - tạo hiệu ứng đẹp hơn)
        # Enemy sẽ di chuyển theo đường parabol nhẹ
        progress = self.y / 600  # 600 là chiều cao màn hình
        if progress < 0.3:  # 30% đầu: di chuyển chậm về phía phi thuyền
            self.horizontal_speed = self.base_speed * 0.4
        elif progress < 0.7:  # 30-70%: tăng tốc hướng về phi thuyền
            self.horizontal_speed = self.base_speed * 0.8
        else:  # 70-100%: tăng tốc mạnh để lao vào phi thuyền
            self.horizontal_speed = self.base_speed * 1.2
        
        # 4. Collision avoidance - tránh chồng lên các enemy khác
        if other_enemies:
            self.avoid_collision(other_enemies)
    
    def avoid_collision(self, other_enemies):
        """Tránh va chạm với các enemy khác - TĂNG CƯỜNG"""
        # Reset offset trước khi tính toán
        push_x = 0
        push_y = 0
        collision_count = 0
        
        for other in other_enemies:
            if other is self:
                continue
            
            # Tính khoảng cách đến enemy khác
            dx = self.x - other.x
            dy = self.y - other.y
            distance = math.sqrt(dx * dx + dy * dy)
            
            # Ngưỡng va chạm TĂNG LÊN (dựa trên độ dài từ)
            # Tăng từ 50 lên 80 để tạo khoảng cách lớn hơn
            base_distance = 80
            word_factor = (len(self.origin_word) + len(other.origin_word)) * 5  # Tăng từ 3 lên 5
            min_distance = base_distance + word_factor
            
            if distance < min_distance and distance > 0.1:  # Tránh chia cho 0
                # Tính lực đẩy để tách ra - MẠNH HƠN
                overlap = min_distance - distance
                push_strength = overlap * 0.5  # Tăng từ 0.3 lên 0.5 (mạnh hơn 67%)
                
                # Normalize vector và áp dụng lực đẩy
                push_x += (dx / distance) * push_strength
                push_y += (dy / distance) * push_strength * 0.3  # Giảm Y từ 0.5 xuống 0.3
                
                collision_count += 1
        
        # Áp dụng offset (tăng giới hạn đẩy)
        max_push = 5  # Tăng từ 3 lên 5
        if collision_count > 0:
            # Nếu va chạm nhiều enemy, đẩy mạnh hơn
            max_push = min(8, 5 + collision_count)
        
        self.x += max(-max_push, min(max_push, push_x))
        self.y += max(-max_push, min(max_push, push_y))

    def required_char(self) -> str:
        """Trả về ký tự tiếp theo cần gõ"""
        if self.progress < len(self.origin_word):
            return self.origin_word[self.progress].lower()
        return ""

    def hit_char(self, ch: str) -> bool:
        """
        Xử lý khi gõ đúng ký tự
        Returns True nếu enemy hoàn thành (gõ hết từ)
        """
        if ch.lower() == self.required_char():
            self.progress += 1
            self.current_hp -= 1  # Giảm HP khi bị hit
            return self.is_complete()
        return False

    def is_complete(self) -> bool:
        """
        METHOD QUAN TRỌNG - Kiểm tra enemy đã bị tiêu diệt hết chưa
        """
        return self.progress >= len(self.origin_word)

    def get_color_by_speed(self):
        """Trả về màu dựa trên tốc độ - điều chỉnh cho tốc độ cực chậm"""
        if self.speed > 0.3:
            return (255, 100, 100)  # Đỏ vừa - nhanh (với tốc độ mới)
        elif self.speed > 0.2:
            return (255, 150, 150)  # Đỏ nhạt
        else:
            return (255, 200, 200)  # Hồng nhạt - chậm
    
    def draw_hp_bar(self, surface: pygame.Surface, font: pygame.font.Font):
        """Vẽ thanh HP phía trên enemy"""
        if self.max_hp <= 0:
            return
        
        # Tính chiều dài thanh HP dựa trên text width
        text_width = font.size(self.origin_word)[0]
        bar_width = max(40, text_width)  # Ít nhất 40px
        bar_height = 5
        bar_x = self.x
        bar_y = self.y - 12  # Vẽ phía trên chữ
        
        # Background (màu xám đậm)
        pygame.draw.rect(surface, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
        
        # HP bar (màu xanh lá -> vàng -> đỏ theo HP)
        hp_ratio = self.current_hp / self.max_hp
        filled_width = int(bar_width * hp_ratio)
        
        # Chọn màu theo HP ratio
        if hp_ratio > 0.6:
            hp_color = (50, 255, 50)  # Xanh lá - khỏe
        elif hp_ratio > 0.3:
            hp_color = (255, 255, 50)  # Vàng - trung bình
        else:
            hp_color = (255, 50, 50)  # Đỏ - yếu
        
        if filled_width > 0:
            pygame.draw.rect(surface, hp_color, (bar_x, bar_y, filled_width, bar_height))
        
        # Viền thanh HP
        pygame.draw.rect(surface, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height), 1)
        
        # Hiển thị số HP nếu từ dài (> 5 ký tự)
        if self.max_hp > 5:
            hp_text = font.render(f"{self.current_hp}/{self.max_hp}", True, (255, 255, 255))
            # Scale down font size
            small_font = pygame.font.SysFont("Arial", 16)
            hp_text = small_font.render(f"{self.current_hp}/{self.max_hp}", True, (255, 255, 255))
            text_rect = hp_text.get_rect()
            text_rect.midtop = (bar_x + bar_width // 2, bar_y + bar_height + 2)
            surface.blit(hp_text, text_rect)
    
    def draw(self, surface: pygame.Surface, font: pygame.font.Font, color=(255, 0, 0)):
        """Vẽ enemy lên màn hình với cache và visual effects"""
        shown = "_" * self.progress + self.origin_word[self.progress:]
        
        # Chọn màu động dựa trên tốc độ
        dynamic_color = self.get_color_by_speed()
        
        # Render text với màu động
        current_text = font.render(shown, True, dynamic_color)
        
        # LOẠI BỎ mũi tên - gây rối mắt và không cần thiết
        # Người chơi có thể thấy enemy di chuyển về phía phi thuyền
        # if self.target_ship and abs(self.target_x - self.x) > 5:
        #     ... (removed)
        
        # Vẽ HP bar trước (phía trên)
        self.draw_hp_bar(surface, font)
        
        # Vẽ text chính
        surface.blit(current_text, (self.x, self.y))
        
        # Vẽ speed indicator bar - LOẠI BỎ vì tốc độ đều và chậm
        # if self.speed > 0.6:
