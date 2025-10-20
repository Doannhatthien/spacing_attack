# 🌿 HƯỚNG DẪN TẠO NHÁNH MỚI VÀ PUSH LÊN GITHUB

## 📋 Mục tiêu
- Tạo nhánh mới tên `khonggian`
- Push toàn bộ dự án lên nhánh đó

---

## 🚀 CÁCH 1: Sử dụng Terminal (PowerShell)

### Bước 1: Mở Terminal
- Nhấn `` Ctrl + ` `` trong VS Code
- Hoặc: Terminal → New Terminal

---

### Bước 2: Kiểm tra Git đã cài chưa
```powershell
git --version
```

**Kết quả mong đợi:**
```
git version 2.x.x
```

**Nếu chưa có:** Tải Git tại https://git-scm.com/download/win

---

### Bước 3: Kiểm tra trạng thái hiện tại
```powershell
cd "c:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian"
git status
```

**Nếu chưa là Git repo:**
```powershell
git init
```

---

### Bước 4: Tạo file .gitignore (nếu chưa có)
```powershell
# Tạo file .gitignore
New-Item -Path ".gitignore" -ItemType File -Force

# Thêm nội dung
@"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
.env

# Virtual Environment
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Game files (tuỳ chọn - xóa nếu muốn commit)
*.pyc
*.pyo

# Logs
*.log
"@ | Out-File -FilePath ".gitignore" -Encoding utf8
```

---

### Bước 5: Commit tất cả files hiện tại
```powershell
# Add tất cả files
git add .

# Commit với message
git commit -m "Initial commit - Space Typing Game"
```

---

### Bước 6: Tạo nhánh mới tên 'khonggian'
```powershell
# Tạo và chuyển sang nhánh khonggian
git checkout -b khonggian
```

**Hoặc tách riêng:**
```powershell
# Tạo nhánh
git branch khonggian

# Chuyển sang nhánh
git checkout khonggian
```

**Kiểm tra nhánh hiện tại:**
```powershell
git branch
```
**Kết quả:** Dấu `*` ở `khonggian`
```
  main
* khonggian
```

---

### Bước 7: Kết nối với GitHub (nếu chưa có repo)

#### A. Tạo repo mới trên GitHub
1. Vào https://github.com
2. Nhấn nút **New** (màu xanh)
3. Đặt tên repo: `space-typing-game` (hoặc tên khác)
4. **KHÔNG** tick "Initialize this repository with a README"
5. Nhấn **Create repository**

#### B. Kết nối local repo với GitHub
```powershell
# Thay YOUR_USERNAME và YOUR_REPO bằng thông tin thực tế
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Ví dụ:
# git remote add origin https://github.com/john/space-typing-game.git
```

**Kiểm tra:**
```powershell
git remote -v
```

---

### Bước 8: Push nhánh 'khonggian' lên GitHub
```powershell
# Push nhánh khonggian lên GitHub
git push -u origin khonggian
```

**Giải thích:**
- `git push`: Đẩy code lên
- `-u`: Set upstream (lần sau chỉ cần `git push`)
- `origin`: Tên remote (GitHub)
- `khonggian`: Tên nhánh

**Nhập username và password (hoặc token) nếu được hỏi**

---

### Bước 9: Xác nhận thành công
1. Vào GitHub repo của bạn
2. Nhấn dropdown "main" → Chọn "khonggian"
3. Kiểm tra files đã được push

---

## 🔄 CÁCH 2: Sử dụng VS Code GUI

### Bước 1: Mở Source Control
- Nhấn `Ctrl + Shift + G`
- Hoặc: Click icon Source Control bên trái (biểu tượng nhánh)

---

### Bước 2: Initialize Repository (nếu chưa có)
- Nhấn "Initialize Repository"
- Chọn thư mục dự án

---

### Bước 3: Stage và Commit files
1. Click "+" ở "Changes" để stage tất cả
2. Nhập commit message: "Initial commit - Space Typing Game"
3. Nhấn `Ctrl + Enter` hoặc click ✓ để commit

---

### Bước 4: Tạo nhánh mới
1. Click vào tên nhánh hiện tại (góc dưới trái, ví dụ "main")
2. Chọn "Create new branch"
3. Nhập tên: `khonggian`
4. Nhấn Enter

---

### Bước 5: Publish Branch
1. Click "Publish Branch" (nút xuất hiện sau khi tạo nhánh)
2. Chọn GitHub
3. Chọn Public hoặc Private
4. Nhập tên repo (hoặc chọn repo có sẵn)

---

## 📝 CÁC LỆNH QUAN TRỌNG

### Kiểm tra trạng thái
```powershell
git status                    # Xem files thay đổi
git branch                    # Xem danh sách nhánh
git log --oneline            # Xem lịch sử commit
```

### Làm việc với nhánh
```powershell
git branch                           # Liệt kê nhánh
git branch khonggian                 # Tạo nhánh mới
git checkout khonggian               # Chuyển sang nhánh
git checkout -b khonggian            # Tạo và chuyển luôn
git branch -d khonggian              # Xóa nhánh (local)
```

### Đồng bộ với GitHub
```powershell
git pull origin khonggian            # Kéo code mới nhất
git push origin khonggian            # Đẩy code lên
git push -u origin khonggian         # Đẩy và set upstream
git push --all                       # Đẩy tất cả nhánh
```

### Quản lý remote
```powershell
git remote -v                        # Xem remote
git remote add origin <URL>          # Thêm remote
git remote remove origin             # Xóa remote
git remote set-url origin <NEW_URL>  # Đổi URL
```

---

## 🔐 XÁC THỰC GITHUB

### Nếu dùng HTTPS (khuyến nghị dùng Token)

1. **Tạo Personal Access Token:**
   - Vào GitHub → Settings → Developer settings
   - Personal access tokens → Tokens (classic)
   - Generate new token
   - Chọn scopes: `repo` (toàn quyền repo)
   - Copy token (CHỈ HIỆN 1 LẦN!)

2. **Khi push, dùng token thay password:**
   ```
   Username: your_github_username
   Password: ghp_xxxxxxxxxxxxx (token vừa tạo)
   ```

3. **Lưu credential (không cần nhập lại):**
   ```powershell
   git config --global credential.helper store
   ```

### Nếu dùng SSH (advanced)
```powershell
# Tạo SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Thêm SSH key vào GitHub
# Copy nội dung file: ~/.ssh/id_ed25519.pub
# Paste vào GitHub → Settings → SSH Keys

# Đổi remote sang SSH
git remote set-url origin git@github.com:USERNAME/REPO.git
```

---

## 📂 CẤU TRÚC SAU KHI PUSH

```
GitHub Repo
├── Branch: main (có thể không có nếu bạn chỉ push khonggian)
└── Branch: khonggian ✅
    ├── assets/
    ├── src/
    ├── .gitignore
    ├── README.md (nếu có)
    └── ... (tất cả files)
```

---

## ❗ XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi 1: "fatal: not a git repository"
```powershell
# Giải pháp: Init Git
git init
```

### Lỗi 2: "failed to push some refs"
```powershell
# Giải pháp: Pull trước khi push
git pull origin khonggian --allow-unrelated-histories
git push origin khonggian
```

### Lỗi 3: "Permission denied (publickey)"
```powershell
# Giải pháp: Dùng HTTPS thay vì SSH
git remote set-url origin https://github.com/USERNAME/REPO.git
```

### Lỗi 4: Quên tên nhánh
```powershell
# Giải pháp: Xem danh sách nhánh
git branch -a
```

### Lỗi 5: Files không được track
```powershell
# Kiểm tra .gitignore
cat .gitignore

# Force add nếu bị ignore nhầm
git add -f <file_name>
```

---

## 🎯 WORKFLOW ĐỀ XUẤT

### Lần đầu setup
```powershell
# 1. Navigate to project
cd "c:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian"

# 2. Init Git (nếu chưa)
git init

# 3. Create .gitignore
# (Xem bước 4 ở trên)

# 4. Add & commit
git add .
git commit -m "Initial commit - Space Typing Game"

# 5. Create branch
git checkout -b khonggian

# 6. Add remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 7. Push
git push -u origin khonggian
```

### Sau khi sửa code
```powershell
# 1. Check changes
git status

# 2. Add files
git add .

# 3. Commit
git commit -m "Update: <mô tả thay đổi>"

# 4. Push
git push
```

---

## 📋 CHECKLIST

- [ ] Git đã cài đặt (`git --version`)
- [ ] Đã init repo (`git init`)
- [ ] Đã tạo .gitignore
- [ ] Đã commit files (`git commit`)
- [ ] Đã tạo nhánh khonggian (`git checkout -b khonggian`)
- [ ] Đã tạo repo trên GitHub
- [ ] Đã add remote (`git remote add origin`)
- [ ] Đã push thành công (`git push -u origin khonggian`)
- [ ] Kiểm tra trên GitHub web

---

## 📖 TÀI LIỆU THAM KHẢO

- Git Docs: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

## 💡 TIPS HỮU ÍCH

### 1. Alias để gõ nhanh hơn
```powershell
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Sau đó dùng:
git co khonggian  # thay vì git checkout khonggian
git st            # thay vì git status
```

### 2. Xem lịch sử đẹp hơn
```powershell
git log --graph --oneline --all --decorate
```

### 3. Undo commit cuối (chưa push)
```powershell
git reset --soft HEAD~1
```

### 4. Xem diff trước khi commit
```powershell
git diff
```

### 5. Commit một phần file
```powershell
git add -p <file>  # Chọn từng phần để commit
```

---

## 🎓 GHI CHÚ QUAN TRỌNG

1. **Luôn pull trước khi push** nếu làm việc nhóm
2. **Viết commit message rõ ràng**
3. **Không push files nhạy cảm** (.env, passwords, tokens)
4. **Sử dụng .gitignore đúng cách**
5. **Branch khonggian là nhánh riêng**, có thể merge vào main sau

---

## 🚀 LỆNH NHANH (COPY & PASTE)

```powershell
# Navigate
cd "c:\Users\pc\Documents\Danhmaykhonggian (1)\Danhmaykhonggian"

# Setup Git (lần đầu)
git init
git add .
git commit -m "Initial commit - Space Typing Game"

# Tạo và push nhánh khonggian
git checkout -b khonggian
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin khonggian
```

**Thay `YOUR_USERNAME` và `YOUR_REPO` bằng thông tin của bạn!**

---

*Hướng dẫn được tạo: 2025-01-20*
*Chúc bạn push thành công! 🎉*
