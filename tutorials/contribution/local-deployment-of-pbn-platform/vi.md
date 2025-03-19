---
name: Hướng dẫn chạy nền tảng Plan ₿ Network cục bộ
description: Làm thế nào bạn có thể chạy Plan ₿ Network trong môi trường cục bộ để kiểm tra nội dung đóng góp của tôi hoặc hiệu đính/xem xét nội dung giáo dục trên Plan ₿ Network?
---
![github](assets/cover.webp)

## Tóm tắt

Hướng dẫn này cung cấp hướng dẫn từng bước để thiết lập Hệ thống quản lý học tập Bitcoin từ Plan ₿ Network trên máy cục bộ của bạn bằng Docker, khóa giả và cấu hình kho lưu trữ tùy chỉnh.

Nếu bạn không hiểu phần trên, đừng lo lắng - hướng dẫn này là dành cho bạn!

---
## **Cách chạy Hệ thống quản lý học tập Bitcoin cục bộ**

Hướng dẫn này cung cấp các bước chi tiết để thiết lập nền tảng, xử lý khóa giả và tùy chỉnh kho lưu trữ. Thực hiện theo các bước dưới đây để tránh các sự cố thường gặp và cấu hình đúng môi trường cục bộ của bạn.

**1. Điều kiện tiên quyết**


- Máy Linux có cài đặt Docker và Docker Compose (cũng có báo cáo là hoạt động được trên Windows).
- phiên bản `nodejs` đủ (đã thử nghiệm: 22.12.0)
- `pnpm` đã được cài đặt trên hệ thống của bạn.
- Git được cấu hình để sao chép kho lưu trữ.

**2. Sao chép kho lưu trữ**

Sao chép kho lưu trữ vào máy cục bộ của bạn:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Hệ thống quản lý học tập Bitcoin

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Thiết lập biến môi trường**

1\. Sao chép tệp `.env.example`:

```bash
cp .env.example .env
```

1. Chỉnh sửa tệp `.env`, xóa phần .example của tên, bây giờ bạn phải bao gồm các khóa giả cho các biến bắt buộc. Ví dụ:

⚠️ Đây là bước bắt buộc, nếu bỏ qua sẽ dẫn đến lỗi như từ chối kết nối giữa một số container.

Đừng quên thêm Github PAT chuyên dụng của bạn vào tệp

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Cài đặt các phụ thuộc**

`Hãy chắc chắn` đã cài đặt phiên bản nodejs phù hợp. Tính đến ngày 2024-12, v22.12.0 (LTS) đã được chứng minh là hoạt động.

⚠️ Phiên bản nodejs của kho lưu trữ Ubuntu 22.04 là 12.22.9: quá cũ để cho phép bạn cài đặt pnpm

Để cài đặt nodejs, hãy tìm hướng dẫn [tại đây](https://nodejs.org/en/download/package-manager); ví dụ bạn có thể chọn sử dụng phương pháp cài đặt `nvm`.

---
Trước khi bắt đầu giai đoạn cài đặt pnpm các gói cần thiết, hãy đảm bảo rằng bạn đã cài đặt tất cả các gói phụ thuộc, bạn có thể thực hiện việc này bằng cách chạy lệnh sau:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Trong thư mục `../Bitcoin-learning-management-system/` của bạn, hãy chạy lệnh sau để cài đặt `pnpm`

```bash
pnpm install
```

> [!MẸO]
> Hãy nhớ cập nhật theo thời gian cả các phụ thuộc và pnpm
**5. Chạy các Container**

Trong thư mục `../Bitcoin-learning-management-system/` của bạn, hãy khởi động môi trường phát triển với Docker:

```bash
docker compose up --build -V
```

Bạn cũng chạy lệnh tiếp theo theo cách này, bạn sẽ không thấy nhật ký trong thiết bị đầu cuối của mình.

```bash
docker compose up -d --build -V
```

Thao tác này sẽ xây dựng và khởi động tất cả các container cần thiết từ docker.

**6. Truy cập ứng dụng**

Sau khi các container đang chạy, hãy truy cập vào giao diện tại:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Lưu ý: ứng dụng sẽ tự động tải lại nếu bạn thay đổi bất kỳ tệp nguồn nào.

**7.** Thiết lập cơ sở dữ liệu Schema của bạn

Trong lần chạy đầu tiên, bạn sẽ cần chạy di chuyển DB.

Để thực hiện, hãy chạy tập lệnh di chuyển: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Nhập dữ liệu từ kho lưu trữ**

Để nhập dữ liệu vào cơ sở dữ liệu, hãy gửi yêu cầu tới API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Sửa lỗi truy cập Sync Volume**

Nếu bạn gặp sự cố truy cập với ổ đĩa `cdn` và `sync`, hãy chạy:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

rồi lại nữa:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Tùy chỉnh Kho lưu trữ (Tùy chọn)**

Nếu bạn cần sử dụng Fork hoặc một nhánh cụ thể:

1. Chỉnh sửa tệp `.env` để cập nhật các biến sau:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Khởi động lại Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Đồng bộ lại dữ liệu kho lưu trữ:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Hướng dẫn này đảm bảo nền tảng được thiết lập đúng với các khóa giả, các phụ thuộc được cài đặt và kho lưu trữ được tùy chỉnh khi cần. 🎉 Chúc bạn may mắn với thiết lập của mình!

**Lệnh để được trợ giúp thêm**

dừng tất cả các container

```
docker compose down
```

cắt tỉa tất cả các thùng chứa và khối lượng hiện có

```
docker container prune -f
docker volume prune --all
```

tạo lại các thùng chứa bằng cùng lệnh được sử dụng trong hướng dẫn chính thức và tập lệnh đồng bộ hóa bữa trưa:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```