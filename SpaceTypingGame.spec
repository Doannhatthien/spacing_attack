# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Tập hợp tất cả assets (fonts, images, sounds) và save data
# Chỉ thêm thư mục, PyInstaller sẽ tự copy tất cả file bên trong
added_files = [
    ('assets', 'assets'),
    ('save', 'save'),  # Thêm thư mục save để giữ leaderboard và progress
]

# Thư viện ẩn cần thiết cho pygame
hidden_imports = [
    'pygame',
    'pygame.freetype',
    'PIL',
    'PIL.Image',
    'cv2',
    'numpy',
]

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SpaceTypingGame',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Không hiển thị console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/images/icon.ico',  # Icon cho file .exe
)
