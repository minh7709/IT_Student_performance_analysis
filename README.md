# 📊 Phân tích Kết quả Học tập Sinh viên IT (CSE)

> **Đề tài môn Nhập môn Khoa học Dữ liệu:** Xây dựng bộ dữ liệu về kết quả học tập của sinh viên IT, xử lý và trực quan hóa dữ liệu và rút ra các ý nghĩa.

---

## 🚀 Chạy nhanh (1 lệnh duy nhất)

```bash
# Kích hoạt môi trường ảo (đã có sẵn)
.\.venv\Scripts\activate          # Windows
# source .venv/bin/activate       # macOS/Linux

# Chạy toàn bộ pipeline từ đầu đến cuối
python run_pipeline.py
```

Hoặc cài mới từ đầu:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python run_pipeline.py
```

Pipeline chạy **~36 giây**, tự động thực hiện 5 bước và in tóm tắt kết quả cuối cùng.

---

## 📁 Cấu trúc Dự án

```
nhap_mon_khoa_hoc_du_lieu/
├── archive/
│   └── Students_Performance_data_set.csv    # Dữ liệu thô (1.194 SV × 31 cột)
├── data/
│   ├── cleaned_students_performance.csv     # Dữ liệu đã làm sạch (31 cột)
│   └── processed_students_performance.csv   # Dữ liệu đã xử lý (38 cột)
├── scripts/
│   ├── 01_data_cleaning.py        # Tiền xử lý & Làm sạch
│   ├── 02_feature_engineering.py  # Tạo 7 đặc trưng phái sinh
│   ├── 03_eda_visualizations.py   # EDA & 11 biểu đồ 300 DPI
│   ├── 04_statistical_tests.py    # Shapiro-Wilk, Chi², ANOVA, t-test
│   └── 05_machine_learning.py     # ML: GBM, RF, LR + Feature Importance
├── reports/
│   ├── figures/                   # 11 biểu đồ PNG (300 DPI)
│   ├── descriptive_statistics.txt
│   ├── statistical_test_results.json
│   └── model_evaluation_results.json
├── run_pipeline.py                # Điều phối tổng (chạy file này)
├── requirements.txt               # Thư viện Python
├── README.md                      # File này
└── BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md  # Báo cáo đầy đủ
```

---

## 📋 Tổng quan Pipeline (5 bước)

| Bước | Script | Mô tả | Đầu ra |
|:---:|:---|:---|:---|
| 1 & 2 | `01_data_cleaning.py` | Sửa lỗi typo, chuẩn hóa 31 cột snake_case, xử lý giá trị bất thường | `data/cleaned_students_performance.csv` |
| 3 | `02_feature_engineering.py` | Tạo 7 biến phái sinh + biến mục tiêu `student_status` (3 lớp) | `data/processed_students_performance.csv` |
| 4 | `03_eda_visualizations.py` | Thống kê mô tả + 11 biểu đồ (histogram, scatter, violin, box, heatmap...) | `reports/figures/` + `descriptive_statistics.txt` |
| 5.1 | `04_statistical_tests.py` | Shapiro-Wilk, Chi-Square, ANOVA, Kruskal-Wallis, t-test, Mann-Whitney | `reports/statistical_test_results.json` |
| 5.2 | `05_machine_learning.py` | 3 mô hình ML (5-Fold CV), auto-select best, confusion matrix, feature importance | `reports/model_evaluation_results.json` |

---

## 📊 Kết quả Chính

### Dữ liệu
- **1.194 sinh viên** ngành CSE, **38 thuộc tính** (31 gốc + 7 phái sinh)
- Phân loại 3 nhóm: Good Standing (30.2%), Average (40.3%), Academic Risk (29.6%)

### Machine Learning (Best Model: Gradient Boosting)

| Metric | Giá trị |
|:---|:---:|
| Accuracy (5-Fold CV) | **68.1% ± 3.4%** |
| Test Accuracy | **68.6%** |
| F1-Macro | **0.680** |

### Top 5 Yếu tố Quan trọng Nhất

| # | Yếu tố | Importance |
|:---:|:---|:---:|
| 1 | Điểm SGPA kỳ trước | 47.2% |
| 2 | Thu nhập gia đình | 8.4% |
| 3 | Số tín chỉ tích lũy | 7.7% |
| 4 | Học kỳ hiện tại | 6.6% |
| 5 | Tỷ lệ chuyên cần | 5.6% |

### Kiểm định Thống kê (α = 0.05)

- ✅ **Học bổng ↔ Trạng thái SV:** χ² = 49.97, p = 1.41 × 10⁻¹¹ (Cramer's V = 0.205)
- ✅ **Chuyên cần giữa 3 nhóm:** ANOVA F = 28.42, p = 8.77 × 10⁻¹³
- ✅ **Tiếng Anh ↔ CGPA:** ANOVA F = 7.03, p < 0.001
- ✅ **MXH giữa 3 nhóm:** ANOVA F = 4.63, p = 0.01

---

## 💡 5 Phát hiện Chính

1. **Quán tính Học tập:** SGPA kỳ trước chiếm 47.2% khả năng dự báo — SV tụt điểm sẽ tiếp tục tụt nếu không can thiệp
2. **Ngưỡng Chuyên cần 80%:** Hầu hết SV rủi ro đều có chuyên cần dưới 80%
3. **Bẫy MXH:** Dùng MXH > 3.5 giờ/ngày → giảm rõ rệt khả năng duy trì Good Standing
4. **Rào cản Tiếng Anh:** SV Basic (CGPA 3.08) vs Advance (3.32) — tiếng Anh ảnh hưởng trực tiếp đến kết quả học ngành IT
5. **Nghịch lý Tư vấn:** SV gặp cố vấn có CGPA thấp hơn — do chỉ SV đang gặp khó mới chủ động tìm tư vấn

---

## 🛠️ Công nghệ Sử dụng

- **Python 3.12** với pandas, numpy, matplotlib, seaborn, scipy, scikit-learn
- Pipeline tự động hóa 100% qua `run_pipeline.py`
- Best model tự động chọn theo F1-Weighted (Cross-Validation)
- Kiểm định normality (Shapiro-Wilk) để lý giải việc dùng kiểm định phi tham số

---

## 📖 Báo cáo Chi tiết

Xem file [`BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md`](BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md) để đọc:
- Từ điển dữ liệu đầy đủ 31 thuộc tính
- Mô tả chi tiết từng bước xử lý
- Giải thích cách đọc từng biểu đồ và từng kết quả thống kê
- Ý nghĩa thực tiễn và khung khuyến nghị can thiệp
- Giới hạn của nghiên cứu
