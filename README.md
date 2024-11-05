<h1>Hệ Thống Quản Lý Thanh Toán</h1>

* Yêu Cầu Cần Làm :
  - Quản lý thông tin khách hàng.
  - Tạo và quản lý hóa đơn.
  - Quản lý phương thức thanh toán (ví dụ: tiền mặt, thẻ, chuyển khoản).
  - Theo dõi trạng thái thanh toán (đã thanh toán, chưa thanh toán, quá hạn).
  - Xác định các yêu cầu về bảo mật và quyền truy cập của người dùng.

* Thiết Kế :
  - Khách hàng: ID, tên, địa chỉ, email, số điện thoại, v.v.
  - Hóa đơn: ID, ID khách hàng, ngày tạo, tổng số tiền, trạng thái.
  - Chi tiết hóa đơn: ID hóa đơn, mô tả sản phẩm/dịch vụ, số lượng, đơn giá, v.v.
  - Thanh toán: ID thanh toán, ID hóa đơn, ngày thanh toán, phương thức thanh toán.

* Giao Diện DEMO :
  - Tạo, chỉnh sửa và xóa hóa đơn.
  - Cập nhật trạng thái thanh toán.
  - Xem báo cáo tổng quan doanh thu, số hóa đơn đã thanh toán, số hóa đơn còn nợ.
  - Vẽ biểu đồ doanh thu tháng

* Công cụ :
  - Python, HTML, C++, CSS, Javascrip.

<h1>Sơ Đồ Thuật Toán</h1>
          ┌─────────────────────┐
          │   Khởi Động Ứng Dụng│
          └─────────┬───────────┘
                    │
                    ▼
          ┌─────────────────────┐
          │   Hiển Thị Tùy Chọn │
          │   1. Tạo Hóa Đơn    │
          │   2. Xem Hóa Đơn    │
          │   3. Thanh Toán     │
          └─────────┬───────────┘
                    │
                    ▼
            ┌─────────────────┐
        ┌──▶│ Chọn Tùy Chọn   │
        │   └─────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │Tùy Chọn 1: Tạo Hóa Đơn│
        │ └──────────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │Nhập Tên Khách Hàng   │
        │ │Thêm Sản Phẩm         │
        │ │Lưu Vào CSDL          │
        │ └──────────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │Hiển Thị Tổng Hóa Đơn │
        │ └──────────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │Tùy Chọn 3: Thanh Toán│
        │ └──────────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │Nhập Thông Tin Thanh Toán │
        │ │Cập Nhật CSDL              │
        │ └──────────────────────┘
        │         │
        │         ▼
        │ ┌──────────────────────┐
        │ │ In Hóa Đơn           │
        │ └──────────────────────┘
        │
        └─────────────────────────
