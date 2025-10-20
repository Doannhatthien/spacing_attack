# Quick test - run game with video background
import sys
sys.path.insert(0, r'C:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian')

import pygame
from src.game import Game
from src.video_background import VideoBackground
from pathlib import Path

pygame.init()

# Load video
video_path = Path(r'C:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian\assets\images\backgrounds\backgrounddong.mp4')
print(f"Loading video: {video_path}")

try:
    video_bg = VideoBackground(str(video_path), (800, 600))
    print("✅ Video loaded!")
    
    # Create game with video
    game = Game(video_background=video_bg)
    print(f"✅ Game created with video: {game.video_background is not None}")
    
    # Run game
    print("Starting game...")
    game.run()
    
    # Cleanup
    video_bg.release()
    print("Done!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

pygame.quit()
