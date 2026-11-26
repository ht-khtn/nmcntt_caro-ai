# Caro AI

Dự án xây dựng trò chơi Caro giữa người chơi và máy tính bằng Python.

## 1. Thông tin dự án

- **Ngôn ngữ:** Python
- **Giao diện:** Pygame
- **Số thành viên:** 4
- **Luật chơi:** >=5 quân liên tiếp để chiến thắng.
- **Đối thủ:** AI sử dụng thuật toán tìm kiếm và đánh giá thế cờ.

## 2. Cấu trúc thư mục

```text
caro-ai/
│
├── main.py
├── requirements.txt
├── README.md
│
├── game/                  # Logic trò chơi
│   ├── __init__.py
│   ├── ...
│
├── ai/                    # Thuật toán AI
│   ├── __init__.py
│   ├── ...
│
├── ui/                    # Giao diện
│   ├── __init__.py
│   ├── app.py
│   ├── ...
│
├── controller/            # Điều khiển và tích hợp
│   ├── __init__.py
│   └── game_controller.py
│
│── tests/                 # Kiểm thử
│   └── ...
```

## 3. Phân công công việc

| Thành viên   | Phụ trách            | Thư mục                  |
| ------------ | -------------------- | ------------------------ |
| Thành viên 1 | Bàn cờ, luật chơi    | `game/`                  |
| Khánh Duy    | Thuật toán AI        | `ai/`                    |
| Thành viên 3 | Giao diện            | `ui/`                    |
| Minh Luân    | Controller, tích hợp | `controller/`, `main.py` |

## 4. Quy ước chung

### Biểu diễn bàn cờ

Sử dụng ma trận hai chiều:

- `0`: Ô trống.
- `1`: Người chơi.
- `2`: AI.

Quy ước tọa độ: `(row, col)`.

### Giao tiếp giữa các module

- AI nhận bàn cờ và trả về tọa độ nước đi `(row, col)`.
- AI không trực tiếp cập nhật bàn cờ.
- Game Logic chịu trách nhiệm thực hiện và kiểm tra nước đi.
- UI chỉ xử lý hiển thị và thao tác người dùng.
- Controller chịu trách nhiệm điều phối các module.

Các hàm giao tiếp cụ thể sẽ được thống nhất trước khi triển khai.

## 5. Cài đặt và chạy chương trình

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

Chạy chương trình:

```bash
python main.py
```

## 6. Quy tắc với Git

### 6.1. Quy tắc commit

- Mỗi thành viên phát triển phần việc trên branch riêng.
- 2 branch chính: `main` và `dev`.
- Đặt tên branch theo dạng `feature/tên-thành-viên/tên-module`. VD: `feature/duy/ai`, `feature/hiep/ui`, `feature/quang/game`, `feature/luan/controller`.
- Không tự ý thay đổi cấu trúc dữ liệu hoặc giao diện hàm đã thống nhất.
- Kiểm tra code trước khi tạo Pull Request.
- Chỉ người phụ trách **Controller** mới được merge code vào `dev` và `main`.

### 6.2. Hướng dẫn sử dụng Git

1. **Sau khi clone repo, tạo branch mới từ `dev`:**

```bash
git clone https://github.com/ht-khtn/nmcntt_caro-ai.git

cd nmcntt_caro-ai

# Lấy thông tin branch mới nhất
git fetch origin

# Tạo local branch dev theo origin/dev
git switch --track -c dev origin/dev

# Tạo branch cá nhân từ dev
git switch -c feature/tên-thành-viên/tên-module
```

2. **Lần đầu commit:**

Dùng `git status` để kiểm tra branch hiện tại và file thay đổi:

```bash
git status # CỰC QUAN TRỌNG, kiểm tra branch hiện tại và file thay đổi
```

Nếu sai branch:

```bash
git switch feature/tên-thành-viên/tên-module
```

Sau đó mới chạy:

```bash
git add .
git commit -m "(tên-module): initial commit"
git push -u origin feature/tên-thành-viên/tên-module

```

3. **Những lần commit tiép theo:**

Dùng `git status` để kiểm tra branch hiện tại và file thay đổi:

```bash
git status # CỰC QUAN TRỌNG, kiểm tra branch hiện tại và file thay đổi
```

Nếu sai branch:

```bash
git switch feature/tên-thành-viên/tên-module
```

Sau đó mới chạy:

```bash
git add .
git commit -m "message" # Xem phần 6.3 để biết cách đặt message
git push
```

4. **Lấy code mới từ dev**

Dùng `git status` để kiểm tra branch hiện tại và file thay đổi:

```bash
git status # CỰC QUAN TRỌNG, kiểm tra branch hiện tại và file thay đổi
```

Nếu sai branch:

```bash
git switch feature/tên-thành-viên/tên-module
```

Lấy những thay đổi mới nhất từ `dev` về branch cá nhân:

```bash
git fetch origin
git merge origin/dev
git push
```

Lưu ý:

- Phải đang ở branch cá nhân khi thực hiện merge.
- Đảm bảo đã commit và push các thay đổi đang làm.
- Nếu xảy ra conflict, phải giải quyết hoàn toàn trước khi tiếp tục.

5. **Tạo Pull Request (Lấy thay đổi của mình đem lên dev)**

**Bước 1**: Commit và push lên branch cá nhân (mục 3)
**Bước 2**: Vào GitHub, chọn tab Pull Request -> New Pull Request.
**Bước 3**: Chọn base là `dev`, compare là branch cá nhân, nhấn Create Pull Request.

### 6.3. Quy tắc đặt tên commit

**Đối với commit trên các branch, cần tuân theo cấu trúc sau:**

Cấu trúc: `(tên-thành-viên/tên-module): nội-dung. File đã sửa: danh-sách-file-đã-sửa`.
VD:

- `(duy/ai): Thực hiện thuật toán minimax. File đã sửa: ai/minimax.py`,
- `(hiep/ui): Thêm giao diện bàn cờ. File đã sửa: ui/app.py`,
- `(quang/game): Cập nhật quy tắc cho điều kiện thắng. File đã sửa: game/rules.py`.

**Đối với commit đối với README.md, requirements.txt, cần tuân theo cấu trúc sau:**

Thay đổi README: `(tên thành viên/docs): nội-dung. File đã sửa: danh-sách-file-đã-sửa`.
Thay đổi requirements: `(tên thành viên/config): nội-dung. File đã sửa: danh-sách-file-đã-sửa`.
VD:

- `(duy/docs): Cập nhật README. File đã sửa: README.md`,
- `(hiep/config): Cập nhật requirements. File đã sửa: requirements.txt`

## 7. Công nghệ và thuật toán dự kiến

- Python: Ngôn ngữ lập trình.
- Pygame: Xây dựng giao diện.
- Minimax: Thuật toán tìm kiếm nước đi.
- Alpha-Beta Pruning: Tối ưu quá trình tìm kiếm.
- Heuristic Evaluation: Đánh giá trạng thái bàn cờ.

Các công nghệ và thuật toán có thể được điều chỉnh trong quá trình phát triển.

## 8. Đặc tả chi tiết

**DƯỚI ĐÂY CHỈ LÀ MINH HOẠ, SỬA LẠI THEO CẤU TRÚC**

### 8.1. Game Logic

#### 8.1.1. Sơ đồ module

**file1.py**:

```python
class A:
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

**file2.py**:

```python
class B:
    __init__()
    fun1(a, b)
    fun2()
```

#### 8.1.2. Đặc tả function

**file1.py/A**:

- Tham số:
  - `arg1`: Kiểu int
  - `arg2`: Kiểu int

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

**file1.py/A/fun1(a,b)**:

- Tham số:
  - `a`: Kiểu int
  - `b`: Kiểu int

- Trả về: Kiểu int

- Chức năng:
  - Thực hiện một số thao tác với `a` và `b`, trả về kết quả.

**file1.py/B**:

- Tham số: Không có

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

### 8.2. AI

#### 8.2.1. Sơ đồ module

**file1.py**:

```python
class A:
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

**file2.py**:

```python
class B:
    __init__()
    fun1(a, b)
    fun2()
```

#### 8.2.2. Đặc tả function

**file1.py/A**:

- Tham số:
  - `arg1`: Kiểu int
  - `arg2`: Kiểu int

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

**file1.py/A/fun1(a,b)**:

- Tham số:
  - `a`: Kiểu int
  - `b`: Kiểu int

- Trả về: Kiểu int

- Chức năng:
  - Thực hiện một số thao tác với `a` và `b`, trả về kết quả.

**file1.py/B**:

- Tham số: Không có

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

### 8.3. UI

#### 8.3.1. Sơ đồ module

**file1.py**:

```python
class A:
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

**file2.py**:

```python
class B:
    __init__()
    fun1(a, b)
    fun2()
```

#### 8.2.2. Đặc tả function

**file1.py/A**:

- Tham số:
  - `arg1`: Kiểu int
  - `arg2`: Kiểu int

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

**file1.py/A/fun1(a,b)**:

- Tham số:
  - `a`: Kiểu int
  - `b`: Kiểu int

- Trả về: Kiểu int

- Chức năng:
  - Thực hiện một số thao tác với `a` và `b`, trả về kết quả.

**file1.py/B**:

- Tham số: Không có

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

**file2.py/B/fun2()**:

- Tham số: Không có
- Trả về: Không có
- Chức năng:
  - Thực hiện một số thao tác.

### 8.4. Controller

#### 8.4.1. Sơ đồ module

**file1.py**:

```python
class A:
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

**file2.py**:

```python
class B:
    __init__()
    fun1(a, b)
    fun2()
```

#### 8.4.2. Đặc tả function

**file1.py/A**:

- Tham số:
  - `arg1`: Kiểu int
  - `arg2`: Kiểu int

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.

**file1.py/A/fun1(a,b)**:

- Tham số:
  - `a`: Kiểu int
  - `b`: Kiểu int

- Trả về: Kiểu int

- Chức năng:
  - Thực hiện một số thao tác với `a` và `b`, trả về kết quả.

**file1.py/B**:

- Tham số: Không có

- Chức năng:
  - Module gồm các hàm giao diện, xử lý sự kiện và hiển thị.
