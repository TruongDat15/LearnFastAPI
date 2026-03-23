# 🚀 FastAPI Learning Project

## 📌 Giới thiệu

Đây là project nhỏ được xây dựng trong quá trình học **FastAPI**, **SQLAlchemy** và **Pydantic**.

Mục tiêu của project:

* Hiểu cách xây dựng RESTful API bằng FastAPI
* Làm việc với database bằng SQLAlchemy
* Sử dụng Pydantic để validate dữ liệu
* Áp dụng mô hình phân tầng (router → service → CRUD)

---

## 🛠️ Công nghệ sử dụng

* FastAPI
* SQLAlchemy
* Pydantic
* MySQL
* Uvicorn
* Docker

---

## 📁 Chức năng chính

### 👤 User

* Đăng nhập cơ bản (email & password)
* Trả về access token giả lập cho mục đích học tập

### 📦 Product

* Thêm sản phẩm
* Lấy danh sách sản phẩm

---

## 📂 Cấu trúc thư mục

```text
app/
│── main.py
│
├── core/                   # cấu hình chung
│   └── config.py
├── db/                     # engine, session, base
│   ├── base.py
│   └── session.py
├── models/                 # ORM models
│   └── user.py
├── schemas/                # Pydantic schemas
│   └── auth.py
├── crud/                   # thao tác DB
│   └── user.py
├── services/               # business logic
│   └── auth_service.py
└── api/
    ├── deps.py
    └── v1/
        ├── api.py
        └── endpoints/
            └── auth.py
```

---

## ▶️ Cách chạy project

### 1. Cài dependencies

```
pip install -r requirements.txt
```

### 2. Chạy server

```
uvicorn app.main:app --reload
```

### 3. Truy cập Swagger

```
http://127.0.0.1:8000/docs
```

### 4. API đăng nhập cơ bản

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "123456"
}
```

---

## ⚠️ Ghi chú

* Project chỉ mang tính chất học tập
* Chưa sử dụng mã hóa mật khẩu (đang so sánh plain text để học)
* Token trả về là token giả lập (chưa phải JWT)

---

## 📌 Định hướng phát triển

* Thêm JWT Authentication
* Hash password
* Phân quyền user
    
    .......

