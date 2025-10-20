# Space Typing Game 🚀

Game bắn máy bay không gian với cơ chế đánh máy để tiêu diệt kẻ địch.

## Yêu cầu hệ thống

- **Python**: 3.11.9 (khuyên dùng) hoặc 3.10.x, 3.11.x
- **Hệ điều hành**: Windows, macOS, Linux

## Cài đặt

### 1. Clone hoặc tải project về máy

```bash
git clone https://github.com/NguyenToanThanh/SpacingType.git
cd SpacingType
```

### 2. Tạo môi trường ảo (Virtual Environment)

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Cài đặt các thư viện cần thiết

```bash
pip install pygame Pillow opencv-python numpy
```

**Danh sách thư viện:**

- `pygame==2.6.1` - Engine game chính
- `Pillow==12.0.0` - Xử lý hình ảnh
- `opencv-python==4.12.0.88` - Xử lý video background
- `numpy==2.2.6` - Hỗ trợ tính toán (dependency của OpenCV)

### 4. Tạo file requirements.txt (tùy chọn)

Bạn có thể tạo file `requirements.txt` với nội dung:

```
pygame==2.6.1
Pillow==12.0.0
opencv-python==4.12.0.88
numpy==2.2.6
```

Sau đó cài đặt bằng lệnh:

```bash
pip install -r requirements.txt
```

## Cách chạy game

### Cách 1: Chạy như Python module (khuyên dùng)

```bash
python -m src.main
```

### Cách 2: Chạy trực tiếp từ thư mục gốc

**Windows:**

```powershell
cd d:\code\test\spacing_attack
.venv\Scripts\python.exe -m src.main
```

**macOS/Linux:**

```bash
cd /path/to/spacing_attack
.venv/bin/python -m src.main
```

## Cấu trúc thư mục

```
spacing_attack/
├── assets/
│   ├── fonts/          # Font chữ
│   ├── images/         # Hình ảnh
│   │   └── backgrounds/  # Background cho game
│   ├── sounds/         # Âm thanh và nhạc nền
│   └── save/          # Dữ liệu lưu game
├── src/
│   ├── __init__.py
│   ├── main.py        # File chính để chạy game
│   ├── game.py        # Logic game chính
│   ├── menu.py        # Menu chính
│   ├── settings.py    # Cấu hình game
│   ├── utils.py       # Các hàm tiện ích
│   ├── ship.py        # Tàu người chơi
│   ├── enemy.py       # Kẻ địch
│   ├── bullet.py      # Đạn
│   ├── explosion.py   # Hiệu ứng nổ
│   ├── challenge.py   # Chế độ thử thách
│   ├── leaderboard.py # Bảng xếp hạng
│   └── ...
├── .venv/             # Môi trường ảo Python
└── README.md          # File này
```

## Chế độ chơi

1. **Classic Mode**: Chế độ chơi tự do không giới hạn
2. **Challenge Mode**: Chơi theo từng level với độ khó tăng dần
3. **Leaderboard**: Xem bảng xếp hạng điểm cao

## Tính năng

- ✨ Giao diện đẹp mắt với hiệu ứng full-screen
- 🎮 Điều khiển bằng cách đánh máy từ tiếng Anh
- 🎵 Nhạc nền và âm thanh sống động
- 🎬 Hỗ trợ video background
- 🏆 Hệ thống bảng xếp hạng
- 💾 Lưu tiến trình tự động

## Xử lý lỗi thường gặp

### Lỗi: `ModuleNotFoundError: No module named 'pygame'`

**Giải pháp:** Cài đặt pygame:

```bash
pip install pygame
```

### Lỗi: `ModuleNotFoundError: No module named 'PIL'`

**Giải pháp:** Cài đặt Pillow:

```bash
pip install Pillow
```

### Lỗi: `ImportError: attempted relative import with no known parent package`

**Giải pháp:** Chạy game bằng lệnh:

```bash
python -m src.main
```

Thay vì:

```bash
python src/main.py  # ❌ Sai
```

### Lỗi: Python 3.13.x không cài được pygame

**Giải pháp:** Sử dụng Python 3.11.9:

1. Cài đặt Python 3.11.9
2. Tạo lại môi trường ảo với Python 3.11.9
3. Cài đặt lại các thư viện

## Phát triển bởi

- **Repository**: [NguyenToanThanh/SpacingType](https://github.com/NguyenToanThanh/SpacingType)
- **Branch**: test4

## Giấy phép

[Thêm thông tin giấy phép ở đây]

---

**Chúc bạn chơi game vui vẻ! 🎮🚀**
