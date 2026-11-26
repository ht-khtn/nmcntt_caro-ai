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

- Mỗi thành viên phát triển phần việc trên branch riêng.
- 2 branch chính: `main` và `dev`.
- Đặt tên branch theo dạng `dev/feature/tên-module`. VD: `dev/feature/ai`, `dev/feature/ui`.
- Không tự ý thay đổi cấu trúc dữ liệu hoặc giao diện hàm đã thống nhất.
- Kiểm tra code trước khi tạo Pull Request.
- Chỉ người phụ trách **Controller** mới được merge code vào `dev` và `main`.

## 7. Công nghệ và thuật toán dự kiến

- Python: Ngôn ngữ lập trình.
- Pygame: Xây dựng giao diện.
- Minimax: Thuật toán tìm kiếm nước đi.
- Alpha-Beta Pruning: Tối ưu quá trình tìm kiếm.
- Heuristic Evaluation: Đánh giá trạng thái bàn cờ.

Các công nghệ và thuật toán có thể được điều chỉnh trong quá trình phát triển.

## 8. Đặc tả chi tiết

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
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

#### 8.1.2. Đặc tả function

**file1.py/fun1(a,b)**:

Hàm nhận 2 tham số `a` và `b`, thực hiện một số thao tác và trả về kết quả.

**file2.py/fun2()**:

Hàm không nhận tham số, thực hiện một số thao tác và trả về kết quả.

### 8.2. AI

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
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

#### 8.1.2. Đặc tả function

**file1.py/fun1(a,b)**:

Hàm nhận 2 tham số `a` và `b`, thực hiện một số thao tác và trả về kết quả.

**file2.py/fun2()**:

Hàm không nhận tham số, thực hiện một số thao tác và trả về kết quả.

### 8.3. UI

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
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

#### 8.1.2. Đặc tả function

**file1.py/fun1(a,b)**:

Hàm nhận 2 tham số `a` và `b`, thực hiện một số thao tác và trả về kết quả.

**file2.py/fun2()**:

Hàm không nhận tham số, thực hiện một số thao tác và trả về kết quả.

### 8.4. Controller

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
    __init__(arg1,arg2)
    fun1(a, b)
    fun2()
```

#### 8.1.2. Đặc tả function

**file1.py/fun1(a,b)**:

Hàm nhận 2 tham số `a` và `b`, thực hiện một số thao tác và trả về kết quả.

**file2.py/fun2()**:

Hàm không nhận tham số, thực hiện một số thao tác và trả về kết quả.
