-- Tạo database
CREATE DATABASE IF NOT EXISTS company_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE company_db;

-- Bảng nhân viên
CREATE TABLE IF NOT EXISTS staff (
    id         CHAR(6)                      PRIMARY KEY,   -- mã PIN 6 số, vừa là ID vừa là mật khẩu đăng nhập
    name       VARCHAR(50)                  NOT NULL,
    role       ENUM('cashier', 'manager')   NOT NULL DEFAULT 'cashier',
    is_active  TINYINT(1)                   NOT NULL DEFAULT 1   -- 1 = đang làm, 0 = đã nghỉ/khóa
);

-- Dữ liệu mẫu để test
INSERT INTO staff (id, name, role) VALUES
('123456', 'Nguyễn Văn An',  'cashier'),
('654321', 'Trần Thị Bình',  'cashier'),
('111222', 'Lê Minh Quân',   'manager');