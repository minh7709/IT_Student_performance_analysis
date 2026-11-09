# BÁO CÁO ĐỒ ÁN MÔN NHẬP MÔN KHOA HỌC DỮ LIỆU

## ĐỀ TÀI: XÂY DỰNG BỘ DỮ LIỆU VỀ KẾT QUẢ HỌC TẬP CỦA SINH VIÊN IT, XỬ LÝ VÀ TRỰC QUAN HÓA DỮ LIỆU VÀ RÚT RA CÁC Ý NGHĨA

---

## 📑 MỤC LỤC

1. [Tổng quan Đề tài](#1-tổng-quan-đề-tài)
2. [Nguồn Dữ liệu & Mô tả Bộ dữ liệu](#2-nguồn-dữ-liệu--mô-tả-bộ-dữ-liệu)
3. [Quy trình Thực hiện (Pipeline)](#3-quy-trình-thực-hiện-pipeline)
4. [Bước 1 & 2: Tiền xử lý & Làm sạch Dữ liệu](#4-bước-1--2-tiền-xử-lý--làm-sạch-dữ-liệu)
5. [Bước 3: Kỹ thuật Đặc trưng (Feature Engineering)](#5-bước-3-kỹ-thuật-đặc-trưng-feature-engineering)
6. [Bước 4: Thống kê Mô tả & Trực quan hóa Dữ liệu (EDA)](#6-bước-4-thống-kê-mô-tả--trực-quan-hóa-dữ-liệu-eda)
7. [Bước 5.1: Kiểm định Thống kê Giả thuyết](#7-bước-51-kiểm-định-thống-kê-giả-thuyết)
8. [Bước 5.2: Huấn luyện Mô hình Machine Learning](#8-bước-52-huấn-luyện-mô-hình-machine-learning)
9. [Tổng hợp Ý nghĩa & Kết luận Rút ra từ Dữ liệu](#9-tổng-hợp-ý-nghĩa--kết-luận-rút-ra-từ-dữ-liệu)
10. [Giới hạn của Nghiên cứu](#10-giới-hạn-của-nghiên-cứu)
11. [Hướng dẫn Chạy lại Dự án](#11-hướng-dẫn-chạy-lại-dự-án)
12. [Cấu trúc Thư mục Dự án](#12-cấu-trúc-thư-mục-dự-án)

---

## 1. TỔNG QUAN ĐỀ TÀI

**Đề tài:** Xây dựng bộ dữ liệu về kết quả học tập của sinh viên IT, xử lý và trực quan hóa dữ liệu và rút ra các ý nghĩa.

**Mục tiêu cụ thể:**

1. Thu thập và xây dựng bộ dữ liệu phản ánh toàn diện kết quả học tập, thói quen sinh hoạt và điều kiện cá nhân của sinh viên ngành Công nghệ Thông tin.
2. Tiền xử lý, làm sạch dữ liệu thô: sửa lỗi, chuẩn hóa định dạng, xử lý giá trị thiếu và ngoại lai.
3. Tạo các đặc trưng phái sinh (feature engineering) có ý nghĩa phân tích.
4. Trực quan hóa dữ liệu bằng các biểu đồ đa dạng để khám phá mối quan hệ giữa các yếu tố.
5. Kiểm định thống kê giả thuyết để xác nhận các phát hiện bằng bằng chứng khoa học.
6. Xây dựng mô hình Machine Learning để xác định các yếu tố quan trọng nhất ảnh hưởng đến kết quả học tập.
7. Rút ra các ý nghĩa thực tiễn và đề xuất khuyến nghị.

---

## 2. NGUỒN DỮ LIỆU & MÔ TẢ BỘ DỮ LIỆU

### 2.1 Nguồn gốc

Bộ dữ liệu khảo sát sinh viên ngành Khoa học & Kỹ thuật Máy tính (Computer Science and Engineering — CSE) tại một trường đại học tư thục ở Bangladesh, được công bố trên Mendeley Data (DOI: `10.17632/dc3797vf3t.1`, tác giả: TS. Arifa Tur Rahman và cộng sự, 2024).

> **Lý do chọn dataset này:** Do hạn chế về quyền truy cập dữ liệu sinh viên IT tại Việt Nam (yêu cầu phê duyệt từ Phòng Đào tạo, bảo mật thông tin cá nhân), nhóm sử dụng bộ dữ liệu CSE Bangladesh đã công bố quốc tế làm **dữ liệu thay thế có cấu trúc tương đồng** (proxy dataset). Bộ dữ liệu này phản ánh đầy đủ các khía cạnh cần phân tích: kết quả học tập, thói quen, kỹ năng IT, và điều kiện cá nhân của sinh viên ngành CNTT.

### 2.2 Quy mô & Nội dung

- **Số lượng:** 1.194 sinh viên chính quy
- **Số thuộc tính gốc:** 31 cột khảo sát, bao gồm:
  - **Học vụ:** Điểm CGPA (thang 4.0), SGPA kỳ trước, tỷ lệ chuyên cần, số tín chỉ tích lũy, cảnh cáo/đình chỉ học vụ
  - **Thói quen học tập:** Giờ tự học mỗi ngày, tần suất ngồi học, phương thức học (Online/Offline)
  - **Kỹ năng & Định hướng IT:** Trình độ tiếng Anh, kỹ năng lập trình, lĩnh vực quan tâm (AI, Web Dev, Data Science...)
  - **Điều kiện cá nhân:** Giới tính, tuổi, thu nhập gia đình, nơi ở, sức khỏe, tình trạng quan hệ

### 2.3 Từ điển Dữ liệu (Data Dictionary — 31 thuộc tính)

| # | Tên biến Gốc (Survey Question) | Tên biến Chuẩn hóa | Kiểu | Mô tả |
|:---:|:---|:---|:---:|:---|
| 1 | University Admission year | `admission_year` | Integer | Năm nhập học (2018–2023) |
| 2 | Gender | `gender` | Categorical | Giới tính (Male, Female) |
| 3 | Age | `age` | Integer | Tuổi (18–27) |
| 4 | H.S.C passing year | `hsc_passing_year` | Integer | Năm tốt nghiệp THPT |
| 5 | Program | `program` | Categorical | Chương trình (100% BCSE) |
| 6 | Current Semester | `current_semester` | Integer | Học kỳ hiện tại (1–24) |
| 7 | Do you have meritorious scholarship? | `scholarship` | Binary | Có học bổng khuyến khích (Yes/No) |
| 8 | Do you use University transportation? | `university_transport` | Binary | Dùng xe trường (Yes/No) |
| 9 | How many hour do you study daily? | `daily_study_hours` | Integer | Giờ tự học mỗi ngày (0–13) |
| 10 | How many times do you seat for study in a day? | `study_frequency` | Integer | Số lần ngồi vào bàn học/ngày (1–7) |
| 11 | What is your preferable learning mode? | `learning_mode` | Categorical | Hình thức học (Offline/Online) |
| 12 | Do you use smart phone? | `use_smartphone` | Binary | Sử dụng smartphone (Yes/No) |
| 13 | Do you have personal Computer? | `have_pc` | Binary | Có máy tính cá nhân (Yes/No) |
| 14 | How many hour do you spent daily in social media? | `social_media_hours` | Integer | Giờ lướt MXH mỗi ngày (0–20) |
| 15 | Status of your English language proficiency | `english_proficiency` | Categorical | Trình độ tiếng Anh (Basic/Intermediate/Advance) |
| 16 | Average attendance on class | `attendance_percentage` | Float | Tỷ lệ chuyên cần (0–100%) |
| 17 | Did you ever fall in probation? | `probation` | Binary | Từng bị cảnh cáo học vụ (Yes/No) |
| 18 | Did you ever got suspension? | `suspension` | Binary | Từng bị đình chỉ (Yes/No) |
| 19 | Do you attend in teacher consultancy...? | `faculty_consultancy` | Binary | Có tham vấn giảng viên cố vấn (Yes/No) |
| 20 | What are the skills do you have? | `skills` | Categorical | Kỹ năng IT chính (Programming, Web Dev...) |
| 21 | How many hour do you spent daily on skill...? | `skill_dev_hours` | Integer | Giờ rèn kỹ năng IT mỗi ngày (0–12) |
| 22 | What is you interested area? | `interest_area` | Categorical | Lĩnh vực định hướng (Software, AI, Data Science...) |
| 23 | What is your relationship status? | `relationship_status` | Categorical | Tình trạng quan hệ (Single, Relationship...) |
| 24 | Are you engaged with co-curriculum activities? | `extracurricular` | Binary | Tham gia ngoại khóa (Yes/No) |
| 25 | With whom you are living with? | `living_with` | Categorical | Sống với ai (Family/Bachelor) |
| 26 | Do you have any health issues? | `health_issues` | Binary | Có vấn đề sức khỏe (Yes/No) |
| 27 | What was your previous SGPA? | `previous_sgpa` | Float | Điểm trung bình học kỳ trước (0.00–4.00) |
| 28 | Do you have any physical disabilities? | `physical_disabilities` | Binary | Có khuyết tật thể chất (Yes/No) |
| 29 | What is your current CGPA? | `current_cgpa` | Float | Điểm tích lũy hiện tại (0.00–4.00) |
| 30 | How many Credit did you have completed? | `credits_completed` | Integer | Tổng tín chỉ tích lũy (0–145) |
| 31 | What is your monthly family income? | `monthly_income` | Integer | Thu nhập gia đình hàng tháng (BDT) |

---

## 3. QUY TRÌNH THỰC HIỆN (PIPELINE)

Toàn bộ dự án được đóng gói thành **5 module Python** chạy tuần tự, điều phối bởi 1 script tổng `run_pipeline.py`:

```
┌─────────────────────────────────────────────────────────┐
│              RUN_PIPELINE.PY (Điều phối tổng)           │
└────────────────────────┬────────────────────────────────┘
                         │
    ┌────────────────────┼────────────────────┐
    ▼                    ▼                    ▼
┌─────────┐     ┌──────────────┐     ┌──────────────────┐
│ Bước 1&2│     │   Bước 3     │     │     Bước 4       │
│ Làm sạch│────▶│  Feature     │────▶│ Trực quan hóa    │
│ dữ liệu │     │ Engineering  │     │ EDA (11 biểu đồ) │
└─────────┘     └──────────────┘     └──────────────────┘
                                              │
                    ┌─────────────────────────┼──────────────────┐
                    ▼                                            ▼
           ┌──────────────────┐                       ┌──────────────────┐
           │    Bước 5.1      │                       │    Bước 5.2      │
           │ Kiểm định Thống  │                       │ Machine Learning │
           │ kê (Shapiro,     │                       │ (GBM, RF, LR)    │
           │ Chi², ANOVA,     │                       │ + Feature        │
           │ t-test)          │                       │   Importance     │
           └──────────────────┘                       └──────────────────┘
```

**Thời gian chạy toàn bộ pipeline:** ~36 giây.

---

## 4. BƯỚC 1 & 2: TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU

**File:** `scripts/01_data_cleaning.py`
**Đầu vào:** `archive/Students_Performance_data_set.csv` (1.194 dòng × 31 cột)
**Đầu ra:** `data/cleaned_students_performance.csv` (1.194 dòng × 31 cột)

### Các bước xử lý đã thực hiện:

| # | Vấn đề phát hiện | Cách xử lý | Kết quả |
|:---:|:---|:---|:---|
| 1 | 31 tên cột gốc dài, không nhất quán | Đổi tên toàn bộ sang `snake_case` chuẩn | 31 cột chuẩn hóa |
| 2 | Khoảng trắng thừa trong giá trị chuỗi | `str.strip()` trên tất cả cột object | Loại bỏ whitespace |
| 3 | `hsc_passing_year = 2028` (phi lý, vì `admission_year = 2020`) | Sửa thành `2018` (hợp logic: tốt nghiệp THPT 2 năm trước khi vào ĐH) | 1 dòng được sửa |
| 4 | `attendance_percentage` chứa chuỗi `"94-98"` (dòng 457) | Chuyển thành trung điểm `96.0`, ép kiểu `float64` | Toàn cột là numeric |
| 5 | `health_issues` có nhãn `'no'`, `'N'`, `'No'` không nhất quán | Mapping thống nhất thành `'Yes'` / `'No'` | Nhất quán 100% |
| 6 | `interest_area` có typo `'Data Schince'` | Sửa thành `'Data Science'` | Loại bỏ lỗi chính tả |
| 7 | Kiểm tra dòng trùng lặp | `df.duplicated()` → 0 dòng trùng | Không cần xóa |

---

## 5. BƯỚC 3: KỸ THUẬT ĐẶC TRƯNG (FEATURE ENGINEERING)

**File:** `scripts/02_feature_engineering.py`
**Đầu vào:** `data/cleaned_students_performance.csv` (31 cột)
**Đầu ra:** `data/processed_students_performance.csv` (38 cột = 31 gốc + 7 phái sinh)

### 7 đặc trưng mới được tạo:

| # | Tên biến | Công thức | Ý nghĩa |
|:---:|:---|:---|:---|
| 1 | `study_to_social_ratio` | `daily_study_hours / (social_media_hours + 0.1)` | Mức cân bằng giữa thời gian học và lướt MXH. Tỷ lệ < 1.0 nghĩa là dùng MXH nhiều hơn học |
| 2 | `gap_year` | `max(0, admission_year - hsc_passing_year)` | Khoảng cách gián đoạn sau THPT trước khi vào ĐH |
| 3 | `study_effort_index` | `daily_study_hours × study_frequency` | Cường độ nỗ lực học tập tổng hợp |
| 4 | `academic_support_index` | Tổng (có học bổng + có tham vấn GV) ∈ {0, 1, 2} | Mức độ được hỗ trợ học vụ |
| 5 | `academic_risk_score` | Tổng (probation + suspension + chuyên cần < 80% + sức khỏe yếu) ∈ {0–4} | Điểm cảnh báo nguy cơ học vụ |
| 6 | `gpa_progression` | `current_cgpa - previous_sgpa` | Xu hướng tiến bộ điểm số |
| 7 | **`student_status`** (Biến mục tiêu) | Phân loại dựa trên CGPA + kỷ luật | Trạng thái học tập: 3 lớp |

### Biến mục tiêu `student_status` — quy tắc phân loại:

- **Academic Risk (Nguy cơ):** CGPA < 2.50 HOẶC từng bị cảnh cáo/đình chỉ → **353 SV (29.6%)**
- **Average Standing (Trung bình):** 2.50 ≤ CGPA < 3.50 và không bị kỷ luật → **481 SV (40.3%)**
- **Good Standing (Giỏi):** CGPA ≥ 3.50 và không bị kỷ luật → **360 SV (30.2%)**

Phân phối 3 lớp tương đối cân bằng (~30/40/30), thuận lợi cho việc huấn luyện mô hình ML.

---

## 6. BƯỚC 4: THỐNG KÊ MÔ TẢ & TRỰC QUAN HÓA DỮ LIỆU (EDA)

**File:** `scripts/03_eda_visualizations.py`
**Đầu ra:** 11 biểu đồ 300 DPI trong `reports/figures/` + file `reports/descriptive_statistics.txt`

### 6.1 Thống kê Mô tả (Descriptive Statistics)

Bảng thống kê mô tả 8 biến số lượng cốt lõi (n = 1.194 sinh viên):

| Biến | Trung bình | Độ lệch chuẩn | Trung vị | Min | Max | Độ lệch (Skew) |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **current_cgpa** | 3.17 | 0.75 | 3.21 | 0.0 | 4.0 | −2.50 (lệch trái) |
| **previous_sgpa** | 2.68 | 0.87 | 2.68 | 0.0 | 4.0 | −0.86 (lệch trái) |
| **attendance_percentage** | 88.26 | 15.31 | 93.50 | 0.0 | 100.0 | −2.11 (lệch trái) |
| **daily_study_hours** | 3.13 | 1.65 | 3.00 | 0.0 | 13.0 | +1.01 (lệch phải) |
| **social_media_hours** | 3.29 | 2.29 | 3.00 | 0.0 | 20.0 | +1.99 (lệch phải) |
| **credits_completed** | 71.84 | 48.07 | 78.00 | 0.0 | 145.0 | −0.02 (xấp xỉ chuẩn) |
| **study_to_social_ratio** | 1.34 | 1.48 | 0.97 | 0.0 | 30.0 | +8.71 (lệch phải mạnh) |
| **study_effort_index** | 6.60 | 5.45 | 6.00 | 0.0 | 56.0 | +2.05 (lệch phải) |

**Cách đọc:** Điểm CGPA trung bình là 3.17/4.0, nghĩa là đa số sinh viên CSE đạt mức khá. Tuy nhiên độ lệch chuẩn 0.75 cho thấy sự phân tán lớn — có cả sinh viên 0.0 (chưa có điểm) lẫn 4.0 (xuất sắc). Skewness âm (−2.50) cho thấy phân phối CGPA lệch trái, tức phần đuôi kéo dài về phía điểm thấp.

### 6.2 Bộ 11 Biểu đồ Trực quan hóa

Tất cả biểu đồ xuất ở chuẩn ấn phẩm khoa học 300 DPI, lưu trong `reports/figures/`:

#### Biểu đồ 00: Phân phối CGPA & Giờ Tự học (Histogram + KDE)
**File:** `00_cgpa_studyhours_distribution.png`
- **Mô tả:** Hai histogram cạnh nhau thể hiện phân phối tần suất của CGPA và giờ tự học mỗi ngày, kèm đường ước lượng mật độ kernel (KDE) và các đường trung bình/trung vị.
- **Phát hiện:** CGPA tập trung chủ yếu ở dải 3.0–3.8. Giờ tự học phổ biến nhất là 2–4 giờ/ngày. Có một nhóm nhỏ sinh viên tự học 0 giờ/ngày — đây là nhóm đáng báo động.

#### Biểu đồ 01: Giờ Tự học vs Thời gian Mạng xã hội (Scatter Plot)
**File:** `01_study_vs_social_media.png`
- **Mô tả:** Scatter plot với trục X là giờ dùng MXH, trục Y là giờ tự học, tô màu theo `student_status`, kèm đường hồi quy xu hướng chung.
- **Phát hiện:** Sinh viên Academic Risk tập trung dày đặc ở vùng MXH 4–8 giờ/ngày. Khi MXH > 3.5 giờ/ngày, xác suất duy trì Good Standing giảm rõ rệt.

#### Biểu đồ 02: Chuyên cần theo Trạng thái Sinh viên (Violin Plot)
**File:** `02_attendance_distribution.png`
- **Mô tả:** Violin plot thể hiện phân phối tỷ lệ chuyên cần cho mỗi nhóm trạng thái, với đường ngưỡng 80%.
- **Phát hiện:** Good Standing có chuyên cần tập trung 95–100%. Academic Risk trải rộng và nhiều ca dưới 80%. Ngưỡng 80% chuyên cần hoạt động như "hàng rào an toàn".

#### Biểu đồ 03: Trình độ Tiếng Anh vs CGPA (Box Plot)
**File:** `03_english_vs_cgpa.png`
- **Mô tả:** Box plot so sánh phân phối CGPA giữa 3 mức tiếng Anh (Basic, Intermediate, Advance).
- **Phát hiện:** CGPA tăng dần rõ rệt: Basic (TB 3.08) → Intermediate (3.16) → Advance (3.32). Rào cản ngoại ngữ ảnh hưởng trực tiếp đến năng lực đọc hiểu tài liệu kỹ thuật.

#### Biểu đồ 04: Cảnh cáo Học vụ vs Trạng thái (Stacked Bar Chart)
**File:** `04_probation_vs_status.png`
- **Mô tả:** Biểu đồ thanh xếp chồng cho thấy tỷ lệ phân bổ trạng thái SV theo tiền sử Probation.
- **Phát hiện:** 100% sinh viên từng bị Probation nằm trong nhóm theo dõi rủi ro. Probation là yếu tố phân loại mạnh nhất.

#### Biểu đồ 05: Môi trường Sống & Sức khỏe vs Giờ Tự học (Grouped Bar)
**File:** `05_living_health_study.png`
- **Mô tả:** So sánh giờ tự học trung bình giữa sinh viên sống cùng gia đình vs ở trọ, phân nhóm theo vấn đề sức khỏe, kèm khoảng tin cậy 95%.
- **Phát hiện:** SV sống cùng gia đình tự học ổn định hơn (3.25 giờ/ngày vs 3.05 giờ). SV ở trọ + có vấn đề sức khỏe bị sụt giảm nghiêm trọng nhất (< 2.7 giờ/ngày).

#### Biểu đồ 06: Tham vấn Giảng viên & CGPA (KDE Plot)
**File:** `06_faculty_consultancy_impact.png`
- **Mô tả:** So sánh phân phối mật độ CGPA giữa nhóm có và không tham vấn giảng viên.
- **Phát hiện nghịch lý:** Nhóm có tham vấn GV lại có CGPA TB thấp hơn (3.12 vs 3.22). Giải thích: sinh viên đến phòng cố vấn thường là những bạn đang gặp khó khăn, nợ môn, bị cảnh cáo — đây là hiện tượng "Help-seeking bias" phổ biến trong giáo dục.

#### Biểu đồ 07: Phân bố Biến Mục tiêu (Bar Chart)
**File:** `07_target_status_distribution.png`
- **Phát hiện:** 3 lớp phân bổ tương đối cân bằng: Good Standing 360 (30.2%), Average 481 (40.3%), Academic Risk 353 (29.6%).

#### Biểu đồ 08: Ma trận Tương quan Pearson (Heatmap)
**File:** `08_correlation_matrix.png`
- **Mô tả:** Heatmap ma trận tương quan 11 biến số lượng.
- **Phát hiện:** CGPA tương quan mạnh nhất với SGPA kỳ trước (r = 0.58), chuyên cần (r = 0.22). Tương quan âm với điểm rủi ro (r = −0.47). Giờ dùng MXH tương quan âm yếu với CGPA.

#### Biểu đồ 09: Kỹ năng IT của Sinh viên (Horizontal Bar)
**File:** `09_top_cse_skills.png`
- **Phát hiện:** Top 3 kỹ năng: Programming 534 SV (44.7%), Web Development 251 SV (21.0%), Networking 153 SV (12.8%).

#### Biểu đồ 10: Ma trận Nhầm lẫn — Confusion Matrix (Heatmap)
**File:** `10_confusion_matrix.png`
- Xem chi tiết tại [Phần 8: Machine Learning](#8-bước-52-huấn-luyện-mô-hình-machine-learning).

#### Biểu đồ 11: Tầm quan trọng Đặc trưng — Feature Importance (Bar)
**File:** `11_feature_importance.png`
- Xem chi tiết tại [Phần 8: Machine Learning](#8-bước-52-huấn-luyện-mô-hình-machine-learning).

---

## 7. BƯỚC 5.1: KIỂM ĐỊNH THỐNG KÊ GIẢ THUYẾT

**File:** `scripts/04_statistical_tests.py`
**Đầu ra:** `reports/statistical_test_results.json`

Tất cả kiểm định thực hiện ở mức ý nghĩa α = 0.05 (độ tin cậy 95%).

### 7.1 Kiểm định Phân phối Chuẩn (Shapiro-Wilk)

**Mục đích:** Xác định xem các biến số có tuân theo phân phối chuẩn hay không, để quyết định dùng kiểm định tham số (ANOVA, t-test) hay phi tham số (Kruskal-Wallis, Mann-Whitney).

| Biến | W-stat | p-value | Kết luận |
|:---|:---:|:---:|:---|
| CGPA | 0.7497 | 4.24 × 10⁻³⁹ | **KHÔNG chuẩn** → dùng non-parametric |
| SGPA kỳ trước | 0.9350 | 2.14 × 10⁻²² | **KHÔNG chuẩn** → dùng non-parametric |
| Chuyên cần (%) | 0.7551 | 8.64 × 10⁻³⁹ | **KHÔNG chuẩn** → dùng non-parametric |
| Giờ tự học | 0.9140 | 1.84 × 10⁻²⁵ | **KHÔNG chuẩn** → dùng non-parametric |
| Giờ dùng MXH | 0.8056 | 1.34 × 10⁻³⁵ | **KHÔNG chuẩn** → dùng non-parametric |

**Kết luận:** Toàn bộ 5 biến đều KHÔNG có phân phối chuẩn (p << 0.05). Do đó, các kiểm định phi tham số (Kruskal-Wallis, Mann-Whitney) được sử dụng song song với ANOVA/t-test để đảm bảo kết quả đáng tin cậy.

### 7.2 Kiểm định Chi-Square (Tính Độc lập giữa 2 biến phân loại)

| Biến khảo sát vs `student_status` | χ² | df | p-value | Cramer's V | Kết luận |
|:---|:---:|:---:|:---:|:---:|:---|
| **Học bổng Khuyến khích** | **49.97** | 2 | **1.41 × 10⁻¹¹** | **0.205** | ✅ Cực kỳ có ý nghĩa. Học bổng liên kết mạnh với trạng thái tốt |
| **Trình độ Tiếng Anh** | **18.29** | 4 | **1.08 × 10⁻³** | **0.088** | ✅ Có ý nghĩa. Tiếng Anh tốt hơn → khả năng Good Standing cao hơn |
| **Hoạt động Ngoại khóa** | **10.83** | 2 | **4.46 × 10⁻³** | **0.095** | ✅ Có ý nghĩa. SV hoạt động ngoại khóa có xu hướng học tốt hơn |
| Tham vấn Giảng viên | 1.62 | 2 | 0.445 | 0.037 | ❌ Không có ý nghĩa (do help-seeking bias) |
| Nơi ở (Gia đình/Trọ) | 3.05 | 2 | 0.218 | 0.051 | ❌ Không đủ bằng chứng |
| Phương thức Học (Online/Offline) | 2.04 | 2 | 0.361 | 0.041 | ❌ Không có sự khác biệt |
| Vấn đề Sức khỏe | 0.20 | 2 | 0.906 | 0.013 | ❌ Không có ý nghĩa |

**Cách đọc kết quả:** p-value < 0.05 nghĩa là mối quan hệ giữa 2 biến KHÔNG phải do ngẫu nhiên (có ý nghĩa thống kê). Cramer's V đo mức độ liên kết: 0.1–0.3 = yếu đến trung bình, > 0.3 = mạnh.

### 7.3 Kiểm định ANOVA & Kruskal-Wallis (So sánh trung bình giữa nhiều nhóm)

| So sánh | F-stat | ANOVA p | KW-stat | KW p | Ý nghĩa |
|:---|:---:|:---:|:---:|:---:|:---|
| **Chuyên cần theo 3 nhóm Status** | **28.42** | **8.77 × 10⁻¹³** | **42.73** | **5.27 × 10⁻¹⁰** | ✅ Chuyên cần tạo phân hóa điểm số sâu sắc nhất |
| **CGPA theo Trình độ Tiếng Anh** | **7.03** | **9.25 × 10⁻⁴** | **12.90** | **1.58 × 10⁻³** | ✅ SV trình độ Advance có CGPA cao hơn rõ rệt |
| **Giờ MXH theo 3 nhóm Status** | **4.63** | **9.96 × 10⁻³** | **7.46** | **2.39 × 10⁻²** | ✅ Nhóm Good Standing dùng MXH ít hơn đáng kể |
| CGPA giữa Online vs Offline | 0.43 | 0.512 | 5.79 | 0.016 | ❌ Không khác biệt đáng kể (ANOVA) |

**Cách đọc:** ANOVA kiểm tra xem trung bình của ≥ 3 nhóm có khác nhau không. Do dữ liệu KHÔNG chuẩn (Shapiro-Wilk), kết quả Kruskal-Wallis (phi tham số) đáng tin cậy hơn. Cả hai cùng cho p < 0.05 → kết luận vững chắc.

### 7.4 Kiểm định T-test & Mann-Whitney U (So sánh 2 nhóm)

| So sánh | TB Nhóm Có | TB Nhóm Không | t-stat | p-value | Ý nghĩa |
|:---|:---:|:---:|:---:|:---:|:---|
| CGPA: Có tham vấn GV vs Không | 3.12 | 3.22 | −2.25 | 0.025 | Nghịch lý: Nhóm gặp GV điểm thấp hơn (do help-seeking bias) |
| CGPA: Có học bổng vs Không | 3.21 | 3.13 | 1.54 | 0.123 | Không đạt ý nghĩa thống kê (p > 0.05) tuy trend tích cực |

---

## 8. BƯỚC 5.2: HUẤN LUYỆN MÔ HÌNH MACHINE LEARNING

**File:** `scripts/05_machine_learning.py`
**Đầu ra:** `reports/model_evaluation_results.json` + 2 biểu đồ (Confusion Matrix + Feature Importance)

### 8.1 Thiết kế Thí nghiệm

- **Bài toán:** Phân loại đa lớp (3 lớp: Good Standing / Average / Academic Risk)
- **Biến đầu vào (X):** 24 đặc trưng (13 số + 11 phân loại). **KHÔNG** sử dụng `current_cgpa`, `probation`, `suspension` trong X để tránh rò rỉ dữ liệu (data leakage), vì chúng trực tiếp tham gia vào công thức tạo biến mục tiêu.
- **Biến đầu ra (y):** `student_status`
- **Phương pháp đánh giá:** 5-Fold Stratified Cross-Validation
- **3 thuật toán thử nghiệm:** Logistic Regression, Random Forest, Gradient Boosting

### 8.2 Kết quả So sánh Mô hình (5-Fold Stratified CV)

| Thuật toán | Accuracy (TB ± Std) | F1-Macro | F1-Weighted |
|:---|:---:|:---:|:---:|
| Logistic Regression | 62.9% ± 1.7% | 0.6247 | 0.6248 |
| Random Forest | 66.9% ± 3.7% | 0.6579 | 0.6640 |
| **Gradient Boosting** ◄ BEST | **68.1% ± 3.4%** | **0.6686** | **0.6751** |

**Mô hình tốt nhất được hệ thống tự động chọn:** **Gradient Boosting** (theo F1-Weighted cao nhất).

### 8.3 Đánh giá Trên Tập Kiểm thử (Test Set — 239 mẫu)

| Lớp dự đoán | Precision | Recall | F1-Score | Số mẫu |
|:---|:---:|:---:|:---:|:---:|
| **Good Standing** | **77.3%** | **80.6%** | **0.789** | 72 |
| Average Standing | 66.7% | 72.9% | 0.697 | 96 |
| Academic Risk | 61.0% | 50.7% | 0.554 | 71 |
| **Tổng (Weighted Avg)** | **68.2%** | **68.6%** | **0.682** | **239** |

**Cách đọc:**
- **Precision 77.3% (Good Standing):** Khi mô hình dự đoán 1 SV là "Good Standing", có 77.3% khả năng đúng.
- **Recall 80.6%:** Mô hình tìm ra được 80.6% trong tổng số SV thực sự "Good Standing".
- **Accuracy 68.6%:** Tổng thể mô hình đúng 68.6% trường hợp, vượt xa mức đoán ngẫu nhiên (33.3%) và đoán lớp đa số (40.3%).

### 8.4 Top 12 Đặc trưng Quan trọng Nhất (Feature Importance — Gradient Boosting)

| Hạng | Đặc trưng | Importance | Ý nghĩa thực tiễn |
|:---:|:---|:---:|:---|
| 1 | **Điểm Học kỳ trước (SGPA)** | **47.2%** | Yếu tố dự báo mạnh nhất. SV kỳ trước sa sút rất dễ trượt tiếp |
| 2 | Thu nhập Gia đình | 8.4% | Điều kiện kinh tế ảnh hưởng đến cơ hội học tập |
| 3 | Số Tín chỉ đã hoàn thành | 7.7% | Giai đoạn chuyên ngành (40–80 TC) là thời điểm rủi ro cao |
| 4 | Học kỳ Hiện tại | 6.6% | SV các kỳ giữa gặp khó khăn với môn nặng thuật toán |
| 5 | **Tỷ lệ Chuyên cần** | **5.6%** | Biến hành vi duy nhất nhà trường có thể can thiệp trực tiếp |
| 6 | Tỷ lệ Học / Dùng MXH | 3.2% | Cân bằng thời gian là kỹ năng cần thiết |
| 7 | Tuổi Sinh viên | 3.2% | SV lớn tuổi hơn có thể có gap year ảnh hưởng |
| 8 | Giờ dùng MXH mỗi ngày | 3.1% | MXH > 3.5 giờ/ngày tăng rủi ro học vụ |
| 9 | Chỉ số Nỗ lực Học tập | 2.5% | Cả giờ học và tần suất đều quan trọng |
| 10 | Số năm gián đoạn (Gap year) | 1.3% | Ngắt quãng dài ảnh hưởng nhịp độ học |
| 11 | Số lần ngồi vào bàn học | 1.2% | Thói quen đều đặn có tác dụng |
| 12 | Giờ tự học mỗi ngày | 1.0% | Chất lượng quan trọng hơn số lượng |

---

## 9. TỔNG HỢP Ý NGHĨA & KẾT LUẬN RÚT RA TỪ DỮ LIỆU

### 9.1 Năm phát hiện chính từ phân tích 1.194 sinh viên IT

**Phát hiện 1 — Quán tính Học tập:** Điểm SGPA kỳ trước chiếm tới 47.2% trọng số dự báo. Một khi SV bắt đầu tụt điểm, nếu không được can thiệp ngay, xu hướng tụt sẽ tiếp diễn ở các kỳ sau. Đây là bằng chứng thực nghiệm cho hiệu ứng "snowball" trong kết quả học tập.

**Phát hiện 2 — Ngưỡng an toàn Chuyên cần:** Kiểm định ANOVA/KW cho thấy chuyên cần tạo phân hóa điểm số mạnh nhất (F = 28.42, p = 8.77 × 10⁻¹³). Ngưỡng 80% chuyên cần hoạt động như "hàng rào an toàn" — hầu hết SV rơi vào rủi ro học vụ đều có chuyên cần dưới 80%.

**Phát hiện 3 — Bẫy Mạng xã hội:** Khi thời gian dùng MXH vượt 3.5 giờ/ngày, xác suất duy trì Good Standing giảm đáng kể. Kiểm định ANOVA xác nhận sự khác biệt có ý nghĩa thống kê (F = 4.63, p = 0.01).

**Phát hiện 4 — Rào cản Ngoại ngữ:** Trình độ tiếng Anh liên kết có ý nghĩa thống kê với trạng thái học tập (χ² = 18.29, p = 0.001; ANOVA F = 7.03, p < 0.001). Sinh viên Basic có CGPA TB 3.08 vs Advance 3.32. Trong ngành IT, tiếng Anh là ngôn ngữ của tài liệu kỹ thuật, documentation API, và nghiên cứu.

**Phát hiện 5 — Nghịch lý Tư vấn (Help-seeking bias):** Sinh viên tham vấn giảng viên có CGPA TB thấp hơn (3.12 vs 3.22, p = 0.025). Đây KHÔNG có nghĩa tư vấn gây hại, mà vì những SV chủ động tìm tư vấn thường là những bạn đang gặp khó khăn. Phát hiện này gợi ý nhà trường cần chuyển từ cơ chế "cố vấn bị động" sang "cố vấn chủ động".

### 9.2 Khung Khuyến nghị Can thiệp

```
                  ┌─────────────────────────────────────────┐
                  │    KHUNG CAN THIỆP SƯ PHẠM CHO CSE      │
                  └────────────────────┬────────────────────┘
          ┌────────────────────────────┼───────────────────────────┐
          ▼                            ▼                           ▼
┌──────────────────┐         ┌──────────────────┐        ┌──────────────────┐
│  1. QUẢN TRỊ     │         │  2. CỐ VẤN CHỦ   │        │  3. HỆ THỐNG     │
│  HÀNH VI & NGOẠI │         │  ĐỘNG & HỌC BỔNG │        │  CẢNH BÁO SỚM    │
│  NGỮ CHUYÊN NGÀNH│         │  ĐỘNG LỰC        │        │  (EARLY-ALERT)   │
└──────────────────┘         └──────────────────┘        └──────────────────┘
```

**Trụ cột 1 — Quản trị Hành vi:**
- Khuyến nghị ngưỡng dùng MXH giải trí ≤ 2.5 giờ/ngày
- Bổ sung khóa "English for Tech" để xóa rào cản ngoại ngữ chuyên ngành

**Trụ cột 2 — Cố vấn Chủ động:**
- Tự động gán cố vấn gặp gỡ định kỳ cho SV có chuyên cần < 80% hoặc SGPA kỳ trước < 2.75 (thay vì chờ SV tự đến)
- Thiết kế "Học bổng Nỗ lực Vượt bậc" cho SV cải thiện CGPA ≥ 0.4 điểm

**Trụ cột 3 — Hệ thống Cảnh báo Sớm:**

| Cấp độ | Điều kiện Kích hoạt | Hành động |
|:---:|:---|:---|
| 🟢 Mức 1 (An toàn) | Chuyên cần ≥ 90%, Tỷ lệ Học/MXH ≥ 1.0, SGPA ≥ 3.20 | Gửi thông báo khen ngợi, gợi ý tham gia Lab nghiên cứu |
| 🟡 Mức 2 (Lưu tâm) | Chuyên cần 80–89%, HOẶC MXH > 4 giờ/ngày | Email nhắc nhở tự động, trợ giảng hỗ trợ bài tập |
| 🔴 Mức 3 (Khẩn cấp) | Chuyên cần < 80%, HOẶC SGPA < 2.50, HOẶC từng Probation | Lịch hẹn bắt buộc với cố vấn, liên lạc phụ huynh |

---

## 10. GIỚI HẠN CỦA NGHIÊN CỨU

1. **Dữ liệu thay thế (Proxy):** Bộ dữ liệu CSE Bangladesh không phải sinh viên IT Việt Nam. Mặc dù cấu trúc chương trình đào tạo tương đồng (CGPA thang 4.0, các môn CS/CE cốt lõi), nhưng bối cảnh văn hóa, kinh tế xã hội và hệ thống giáo dục có sự khác biệt. Kết quả nên được diễn giải như xu hướng tham khảo, không áp dụng trực tiếp.

2. **Dữ liệu tự khai (Self-reported):** Giờ tự học, giờ dùng MXH, tình trạng sức khỏe... đều do sinh viên tự khai báo qua khảo sát, có thể bị thiên lệch (response bias).

3. **Dữ liệu cắt ngang (Cross-sectional):** Chỉ thu thập tại 1 thời điểm, không theo dõi theo thời gian (longitudinal). Do đó chỉ xác định được **mối tương quan (correlation)**, KHÔNG khẳng định được **quan hệ nhân quả (causation)**.

4. **Accuracy mô hình ML 68.6%:** Mức độ chính xác hợp lý cho bài toán 3 lớp dùng thông tin hành vi/cá nhân (không có CGPA trực tiếp), nhưng chưa đủ cao để triển khai hệ thống cảnh báo tự động trong thực tế mà không cần xác nhận thêm.

---

## 11. HƯỚNG DẪN CHẠY LẠI DỰ ÁN

### 11.1 Yêu cầu Hệ thống

- Python ≥ 3.10 (khuyến nghị Python 3.12)
- Windows / macOS / Linux

### 11.2 Cài đặt & Chạy

```bash
# 1. Tạo môi trường ảo Python
python -m venv .venv

# 2. Kích hoạt môi trường ảo
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Cài đặt thư viện
pip install -r requirements.txt

# 4. Chạy toàn bộ pipeline (1 lệnh duy nhất)
python run_pipeline.py
```

### 11.3 Đọc Kết quả Sau khi Chạy

Pipeline chạy xong sẽ tạo ra các sản phẩm sau:

| Sản phẩm | Đường dẫn | Mô tả |
|:---|:---|:---|
| Dữ liệu sạch | `data/cleaned_students_performance.csv` | 1.194 dòng × 31 cột đã làm sạch |
| Dữ liệu đã xử lý | `data/processed_students_performance.csv` | 1.194 dòng × 38 cột (thêm 7 đặc trưng phái sinh) |
| 11 biểu đồ | `reports/figures/` | File PNG 300 DPI, đánh số từ 00 đến 11 |
| Thống kê mô tả | `reports/descriptive_statistics.txt` | Bảng describe + skewness |
| Báo cáo Thống kê | `reports/statistical_test_results.json` | Shapiro-Wilk, Chi-Square, ANOVA, t-test |
| Báo cáo ML | `reports/model_evaluation_results.json` | CV results, confusion matrix, feature importance |

### 11.4 Cách Đọc File JSON Kết quả

Mở file `reports/model_evaluation_results.json`:
- `"best_model_selected"`: Tên mô hình tốt nhất (tự động chọn)
- `"cross_validation_results"`: Bảng so sánh 3 mô hình (accuracy, F1)
- `"test_set_evaluation"` → `"classification_report"`: Precision, Recall, F1 cho từng lớp
- `"top_features"`: Danh sách 12 đặc trưng quan trọng nhất (Feature, Importance)

Mở file `reports/statistical_test_results.json`:
- `"normality_tests"`: Kết quả Shapiro-Wilk cho 5 biến
- `"chi_square_tests"`: Kết quả Chi-Square cho 7 cặp biến
- `"anova_kruskal_tests"`: Kết quả ANOVA + Kruskal-Wallis cho 4 so sánh
- `"t_tests"`: Kết quả t-test cho 2 so sánh

---

## 12. CẤU TRÚC THƯ MỤC DỰ ÁN

```
nhap_mon_khoa_hoc_du_lieu/
│
├── archive/
│   └── Students_Performance_data_set.csv    # Dữ liệu thô gốc (1.194 SV × 31 cột)
│
├── data/
│   ├── cleaned_students_performance.csv     # Dữ liệu đã làm sạch (31 cột)
│   └── processed_students_performance.csv   # Dữ liệu đã xử lý (38 cột)
│
├── scripts/
│   ├── 01_data_cleaning.py                  # Bước 1&2: Tiền xử lý & Làm sạch
│   ├── 02_feature_engineering.py            # Bước 3: Tạo đặc trưng phái sinh
│   ├── 03_eda_visualizations.py             # Bước 4: EDA & Trực quan hóa (11 biểu đồ)
│   ├── 04_statistical_tests.py              # Bước 5.1: Kiểm định thống kê
│   ├── 05_machine_learning.py               # Bước 5.2: Huấn luyện ML
│   ├── data_audit.py                        # Script kiểm toán dữ liệu (phụ trợ)
│   ├── check_anomalies.py                   # Script phát hiện bất thường (phụ trợ)
│   └── test_feature_eng.py                  # Script test feature engineering (phụ trợ)
│
├── reports/
│   ├── figures/                             # 11 biểu đồ PNG 300 DPI
│   │   ├── 00_cgpa_studyhours_distribution.png
│   │   ├── 01_study_vs_social_media.png
│   │   ├── 02_attendance_distribution.png
│   │   ├── ...
│   │   ├── 10_confusion_matrix.png
│   │   └── 11_feature_importance.png
│   ├── descriptive_statistics.txt           # Thống kê mô tả + skewness
│   ├── statistical_test_results.json        # Kết quả kiểm định thống kê
│   └── model_evaluation_results.json        # Kết quả ML + feature importance
│
├── run_pipeline.py                          # Script điều phối chạy toàn bộ pipeline
├── requirements.txt                         # Danh sách thư viện Python
├── README.md                                # Hướng dẫn tổng quan nhanh
└── BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md # Báo cáo đầy đủ chi tiết (file này)
```

---

*Báo cáo hoàn thành cho môn Nhập môn Khoa học Dữ liệu.*
