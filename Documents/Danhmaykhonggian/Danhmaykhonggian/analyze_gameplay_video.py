"""
Script phân tích video gameplay để hiểu chuyển động enemy và explosion effects
"""
import cv2
import numpy as np
from pathlib import Path

def analyze_video(video_path):
    """Phân tích video gameplay"""
    print(f"🎬 Đang phân tích video: {video_path}")
    
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        print("❌ Không thể mở video!")
        return
    
    # Lấy thông tin video
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    
    print(f"\n📊 Thông tin video:")
    print(f"   - Độ phân giải: {width}x{height}")
    print(f"   - FPS: {fps}")
    print(f"   - Tổng số frame: {frame_count}")
    print(f"   - Thời lượng: {duration:.2f}s")
    
    print(f"\n🎮 Đang phân tích gameplay...")
    print(f"   Nhấn SPACE để tạm dừng/tiếp tục")
    print(f"   Nhấn 'q' để thoát")
    print(f"   Nhấn 's' để lưu frame hiện tại")
    
    # Tạo thư mục để lưu frames quan trọng
    output_dir = Path("analysis_frames")
    output_dir.mkdir(exist_ok=True)
    
    frame_num = 0
    paused = False
    saved_count = 0
    
    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_num += 1
            
            # Hiển thị frame number và time
            time_sec = frame_num / fps
            display_frame = frame.copy()
            cv2.putText(display_frame, f"Frame: {frame_num}/{frame_count}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, f"Time: {time_sec:.2f}s", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, f"[SPACE] Pause  [S] Save  [Q] Quit", 
                       (10, height-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Resize để hiển thị tốt hơn
            display_scale = 1.0
            if width > 1200:
                display_scale = 1200 / width
            display_frame = cv2.resize(display_frame, 
                                      (int(width*display_scale), int(height*display_scale)))
            
            cv2.imshow('Gameplay Analysis', display_frame)
        
        # Handle keyboard
        key = cv2.waitKey(1 if not paused else 0) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord(' '):
            paused = not paused
            print(f"   {'⏸️  PAUSED' if paused else '▶️  PLAYING'}")
        elif key == ord('s'):
            # Save frame
            save_path = output_dir / f"frame_{frame_num:04d}.png"
            cv2.imwrite(str(save_path), frame)
            saved_count += 1
            print(f"   💾 Đã lưu frame {frame_num} -> {save_path}")
    
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n✅ Phân tích hoàn tất!")
    print(f"   - Đã xem {frame_num}/{frame_count} frames")
    print(f"   - Đã lưu {saved_count} frames vào {output_dir}")
    
    if saved_count > 0:
        print(f"\n💡 Hãy kiểm tra các frame đã lưu để phân tích:")
        print(f"   - Chuyển động của enemy")
        print(f"   - Hiệu ứng nổ (explosion)")
        print(f"   - Tốc độ và pattern di chuyển")

if __name__ == "__main__":
    video_path = Path(r"assets/images/backgrounds/danhmay.mp4")
    
    if not video_path.exists():
        print(f"❌ Không tìm thấy video: {video_path}")
        print(f"   Hãy đảm bảo file video tồn tại!")
    else:
        analyze_video(video_path)
