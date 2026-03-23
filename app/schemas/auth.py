from pydantic import BaseModel


class LoginRequest(BaseModel):
    # Dùng email làm định danh đăng nhập cơ bản.
    email: str
    password: str


class UserPublic(BaseModel):
    # Chỉ trả thông tin an toàn, không trả password.
    id: int
    email: str


class LoginResponse(BaseModel):
    # Token giả lập cho mục tiêu học tập, chưa phải JWT.
    access_token: str
    token_type: str
    user: UserPublic
