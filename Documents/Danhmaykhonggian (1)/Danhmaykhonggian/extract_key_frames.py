"""
Extract key frames từ video để phân tích enemy movement và explosion
"""
import cv2
import numpy as np
from pathlib import Path

def extract_key_frames(video_path, num_frames=20):
    """Extract các frame quan trọng từ video"""
    print(f"🎬 Đang extract frames từ: {video_path}")
    
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        print("❌ Không thể mở video!")
        return
    
    # Thông tin video
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Tạo thư mục output
    output_dir = Path("gameplay_analysis")
    output_dir.mkdir(exist_ok=True)
    
    # Extract frames đều nhau
    frame_interval = frame_count // num_frames
    
    print(f"📊 Sẽ extract {num_frames} frames (mỗi {frame_interval} frames)")
    
    saved_frames = []
    
    for i in range(num_frames):
        frame_num = i * frame_interval
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        
        if ret:
            # Lưu frame
            save_path = output_dir / f"frame_{i+1:02d}_at_{frame_num}.jpg"
            cv2.imwrite(str(save_path), frame)
            saved_frames.append(save_path)
            
            time_sec = frame_num / fps
            print(f"   ✓ Frame {i+1}/{num_frames} - Time: {time_sec:.1f}s - {save_path.name}")
    
    cap.release()
    
    print(f"\n✅ Đã extract {len(saved_frames)} frames vào {output_dir}")
    print(f"\n🔍 Phân tích gameplay:")
    print(f"   Hãy mở thư mục '{output_dir}' để xem các frames")
    print(f"   Chú ý:")
    print(f"   - Enemy di chuyển như thế nào? (thẳng/lượn/zigzag)")
    print(f"   - Tốc độ rơi nhanh hay chậm?")
    print(f"   - Explosion có hiệu ứng gì? (phóng to/particle/flash)")
    print(f"   - Có screen shake không?")
    
    return saved_frames

def detect_motion_patterns(video_path):
    """Phát hiện patterns chuyển động trong video"""
    print(f"\n🎯 Đang phân tích patterns chuyển động...")
    
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        return
    
    # Đọc vài frames để phân tích
    ret, prev_frame = cap.read()
    if not ret:
        return
    
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    motion_vectors = []
    frame_count = 0
    max_analyze_frames = 100  # Chỉ phân tích 100 frames đầu
    
    while frame_count < max_analyze_frames:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Tính optical flow để detect chuyển động
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 
                                            0.5, 3, 15, 3, 5, 1.2, 0)
        
        # Lấy magnitude của flow
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        avg_motion = np.mean(mag)
        motion_vectors.append(avg_motion)
        
        prev_gray = gray
    
    cap.release()
    
    # Phân tích motion patterns
    if motion_vectors:
        avg_motion = np.mean(motion_vectors)
        max_motion = np.max(motion_vectors)
        motion_variance = np.var(motion_vectors)
        
        print(f"\n📊 Kết quả phân tích chuyển động:")
        print(f"   - Chuyển động trung bình: {avg_motion:.2f}")
        print(f"   - Chuyển động tối đa: {max_motion:.2f}")
        print(f"   - Độ biến thiên: {motion_variance:.2f}")
        
        if avg_motion < 2.0:
            print(f"   → Enemy di chuyển CHẬM và ĐỀU")
        elif avg_motion < 5.0:
            print(f"   → Enemy di chuyển TỐC ĐỘ VỪA")
        else:
            print(f"   → Enemy di chuyển NHANH")
        
        if motion_variance > 10:
            print(f"   → Có nhiều THAY ĐỔI TỐC ĐỘ (gia tốc/pattern phức tạp)")
        else:
            print(f"   → Chuyển động MƯỢT và ĐỀU")

if __name__ == "__main__":
    video_path = Path(r"assets/images/backgrounds/danhmay.mp4")
    
    if not video_path.exists():
        print(f"❌ Không tìm thấy video: {video_path}")
    else:
        # Extract frames
        extract_key_frames(video_path, num_frames=15)
        
        # Phân tích patterns
        detect_motion_patterns(video_path)
        
        print(f"\n💡 Tiếp theo:")
        print(f"   1. Mở thư mục 'gameplay_analysis' để xem frames")
        print(f"   2. Mô tả cho tôi những gì bạn thấy")
        print(f"   3. Tôi sẽ implement chính xác chuyển động và effects!")
