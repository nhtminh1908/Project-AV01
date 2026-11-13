# AV01
Phát triển ứng dụng giao tiếp với giao thức truyền thông MQTT
## Mục tiêu dự án
Xây dựng và kiểm chứng mô hình gửi–nhận tin nhắn hai chiều qua MQTT bằng Node-RED. Trọng tâm là Publisher/Subscriber, Broker, topic và luồng xử lý message; không cần cảm biến, cơ sở dữ liệu hay giao diện riêng
### Publish/Subscribe và Broker
Publisher và Subscriber không cần biết địa chỉ hay sự tồn tại của nhau; cả hai làm việc thông qua Broker. Việc gửi/nhận bất đồng bộ giúp tách rời bên gửi và bên nhận. Tin chỉ được định tuyến đến Subscriber đăng ký topic phù hợp.
### Topic và wildcard
Topic là chuỗi phân cấp, thường phân cách bằng `/`, ví dụ `factory/zone1/status`. Wildcard chỉ dùng khi subscribe: `+` khớp một cấp (`demo/+/status`); `#` khớp nhiều cấp và thường đặt ở cuối (`demo/#`). Publisher gửi tới topic cụ thể, không publish bằng wildcard.
### QoS (Quality of Service)
#### QoS == 0 - At most once  -       Gửi mà không chờ xác nhận     - Nhanh, nhẹ; có thể mất tin nhắn.
#### QoS == 1 - At least once -           Có thể gửi lại            - Tin nhắn có thể đến trùng.
#### QoS == 2 - At most once  - PUBLISH → PUBREC → PUBREL → PUBCOMP - Tin cậy nhất nhưng nhiều bước, độ trễ/chi phí cao hơn.
### Retained message
Khi publish với retain=true, Broker lưu tin retained mới nhất của topic và gửi nó cho Subscriber mới đăng ký topic đó. Đây là trạng thái gần nhất, không phải lịch sử tin nhắn. Để minh họa, publish một trạng thái lên topic thử nghiệm khi chưa có Subscriber, sau đó thêm MQTT in subscribe topic ấy và Deploy mà không gửi lại; kiểm tra tin xuất hiện ở Debug. Gửi payload rỗng với retain bật lên đúng topic để xóa retained message sau khi thử.
