import random
import pygame

class Enemy:
    def __init__(self, word: str):
        self.origin_word = word
        self.progress = 0  # Số ký tự đã gõ đúng
        self.x = random.randint(50, 750)
        self.y = random.randint(-100, -50)
        self.speed = random.uniform(1, 3)

    def move(self):
        """Di chuyển enemy xuống dưới"""
        self.y += self.speed

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
            return self.is_complete()
        return False

    def is_complete(self) -> bool:
        """
        METHOD QUAN TRỌNG - Kiểm tra enemy đã bị tiêu diệt hết chưa
        """
        return self.progress >= len(self.origin_word)

    def draw(self, surface: pygame.Surface, font: pygame.font.Font, color=(255, 0, 0)):
        """Vẽ enemy lên màn hình"""
        # Hiển thị phần đã gõ bằng dấu gạch dưới
        shown = "_" * self.progress + self.origin_word[self.progress:]
        text = font.render(shown, True, color)
        surface.blit(text, (self.x, self.y))

    def hit_char(self, ch: str) -> bool:
        """
        Nhận 1 ký tự. Tăng progress nếu đúng 'next char'.
        Trả về True nếu đã hoàn tất (enemy bị tiêu diệt).
        """
        if self.required_char() == ch:
            self.progress += 1
        return self.progress >= len(self.origin_word)
    # Trong class Enemy (enemy.py)

def is_complete(self) -> bool:
    """Kiểm tra enemy đã bị tiêu diệt hết chưa (gõ hết từ)"""
    return self.progress >= len(self.origin_word)