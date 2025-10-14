import pygame
from pathlib import Path
from .settings import WIDTH, HEIGHT
from .utils import load_font, load_image
from .settings import IMAGE_DIR

THUMB_W, THUMB_H = 200, 120
GAP = 20
ROWS, COLS = 2, 3

class BackgroundSelect:
    def __init__(self, filenames: list[str], title="Choose Background"):
        self.title = title
        self.items = filenames
        self.title_font = load_font(None, 48)
        self.info_font = load_font(None, 20)
        self.page = 0
        self.per_page = ROWS * COLS
        self._layout()
        self.hover_index = None

    def _layout(self):
        total_w = COLS * THUMB_W + (COLS - 1) * GAP
        total_h = ROWS * THUMB_H + (ROWS - 1) * GAP
        self.start_x = (WIDTH - total_w) // 2
        self.start_y = (HEIGHT - total_h) // 2

    def _page_items(self):
        a = self.page * self.per_page
        b = a + self.per_page
        return self.items[a:b]

    def _draw_background(self, surf):
        top_color = (10, 10, 25)
        bottom_color = (35, 35, 65)
        gradient = pygame.Surface((1, HEIGHT))
        for y in range(HEIGHT):
            ratio = y / HEIGHT
            c = [
                int(top_color[i] + (bottom_color[i] - top_color[i]) * ratio)
                for i in range(3)
            ]
            gradient.set_at((0, y), c)
        gradient = pygame.transform.scale(gradient, (WIDTH, HEIGHT))
        surf.blit(gradient, (0, 0))

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover_index = None
            mx, my = event.pos
            idx = 0
            for r in range(ROWS):
                for c in range(COLS):
                    x = self.start_x + c * (THUMB_W + GAP)
                    y = self.start_y + r * (THUMB_H + GAP)
                    rect = pygame.Rect(x, y, THUMB_W, THUMB_H)
                    if rect.collidepoint(mx, my) and idx < len(self._page_items()):
                        self.hover_index = idx
                    idx += 1

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                return "__CANCEL__"
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                if (self.page + 1) * self.per_page < len(self.items):
                    self.page += 1
            if event.key in (pygame.K_LEFT, pygame.K_a):
                if self.page > 0:
                    self.page -= 1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            idx = 0
            for r in range(ROWS):
                for c in range(COLS):
                    x = self.start_x + c * (THUMB_W + GAP)
                    y = self.start_y + r * (THUMB_H + GAP)
                    rect = pygame.Rect(x, y, THUMB_W, THUMB_H)
                    subs = self._page_items()
                    if idx < len(subs) and rect.collidepoint(mx, my):
                        return subs[idx]
                    idx += 1
        return None

    def draw(self, surf):
        self._draw_background(surf)
        title_surf, _ = self.title_font.render(self.title, (255, 255, 255))
        surf.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, 100)))

        subs = self._page_items()
        idx = 0
        for r in range(ROWS):
            for c in range(COLS):
                x = self.start_x + c * (THUMB_W + GAP)
                y = self.start_y + r * (THUMB_H + GAP)
                rect = pygame.Rect(x, y, THUMB_W, THUMB_H)

                # Hover scale effect
                draw_rect = rect.copy()
                if idx == self.hover_index:
                    draw_rect.inflate_ip(10, 10)

                # Shadow
                shadow_rect = draw_rect.move(4, 4)
                pygame.draw.rect(surf, (10, 10, 20), shadow_rect, border_radius=10)

                # Border
                border_color = (100, 140, 220) if idx == self.hover_index else (50, 60, 80)
                pygame.draw.rect(surf, border_color, draw_rect, border_radius=10)

                # Image / label
                if idx < len(subs):
                    name = subs[idx]
                    try:
                        img = load_image(name, (draw_rect.width, draw_rect.height))
                        surf.blit(img, draw_rect.topleft)
                    except Exception:
                        label, _ = self.info_font.render(Path(name).name, (255, 255, 255))
                        surf.blit(label, label.get_rect(center=draw_rect.center))
                idx += 1

        # Hint
        hint = f"Page {self.page+1}/{max(1,(len(self.items)+self.per_page-1)//self.per_page)}  (A/D để chuyển trang, Esc để hủy)"
        hint_surf, _ = self.info_font.render(hint, (200, 200, 200))
        surf.blit(hint_surf, hint_surf.get_rect(center=(WIDTH // 2, HEIGHT - 40)))