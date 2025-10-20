# Test video background
import sys
sys.path.insert(0, r'C:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian')

import pygame
from src.video_background import VideoBackground
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

video_path = Path(r'C:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian\assets\images\backgrounds\backgrounddong.mp4')

print(f"Video exists: {video_path.exists()}")
print(f"Video path: {video_path}")

try:
    video_bg = VideoBackground(str(video_path), (800, 600))
    print("Video loaded successfully!")
    
    running = True
    while running:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        video_bg.update(dt)
        video_bg.draw(screen)
        
        # Debug text
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Video Background Test - Press ESC to quit", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
    
    video_bg.release()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

pygame.quit()
