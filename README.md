# OnTimeDeliveryPredict
Chương trình này được lập trình với mục đích dự đoán xem có giao hàng đúng hạn hay không.
Chương trình gồm các file:
1. X_train.pickle, X_test.pickle, X_val.pickle, y_train.pickle, y_test.pickle, y_val.pickle chứa dữ liệu đã được chia tách và có thể sử dụng để train model luôn
2. modelTraining.ipynb: file tiền xử lý dữ liệu, không cần chạy file này mà sử dụng dữ liệu đã xử lý sẵn ở các file pickle trên cũng đc. Hoặc có thể tải bộ dataset này (https://drive.google.com/drive/folders/1zO5XHkACzih2t_4Jm0uNE6mP_RSeu76H?fbclid=IwAR1Ct1EBZ26kYJDukPesdlBMFO6XqtjvRTkTD06CtSYSTk485rwaIHq-z1w) về, đặt trong folder data và chạy lại file này.
3. main.ipynb: scale dữ liệu và chạy so sánh kết quả 6 giải thuật: AdaBoost, RandomForest, Bagging, Gradient Boost, XGBoost, LightGBM với nhau
4. XGBoost: undersampling, oversampling, tinh chỉnh siêu tham số vs thuật toán XGBoost
5. stacking: thử các trường hợp stacking vs 4 thuật toán Random forest, gradient boost, xgboost, light gradient boost
6. folder flask: Đóng gói API


## Yêu cầu
python >= 3.0
```
!pip install -r requirements.txt (window, ubuntu)
%pip install -r requirements.txt (macos)
```
(macOS)

## Hướng dẫn chạy thử
- Cài đặt theo các lệnh như trên
- Chạy từng ô một hoặc run all trên visual studio code
