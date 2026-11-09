# TÀI LIỆU QUY TRÌNH THỰC HIỆN ĐỀ TÀI: PHÂN TÍCH, TRỰC QUAN HÓA VÀ RÚT RA Ý NGHĨA TỪ DỮ LIỆU SINH VIÊN KỸ THUẬT & KHOA HỌC MÁY TÍNH (CSE)

## 📌 1. TỔNG QUAN ĐỀ TÀI VÀ ĐẶC TẢ DỮ LIỆU

### 1.1. Thông tin bộ dữ liệu
* **Bối cảnh:** Dữ liệu khảo sát từ sinh viên Khoa Khoa học & Kỹ thuật Máy tính (Computer Science and Engineering - CSE) tại một trường đại học tư thục ở Bangladesh.
* **Quy mô:** $1.195$ quan sát (student records), $31$ đặc trưng (features), $37.045$ điểm dữ liệu.
* **Cấu trúc biến:** Hỗn hợp (Mixed types) gồm số nguyên (Integer), chuỗi định tính (Categorical/Nominal), số thực (Float).
* **Biến mục tiêu (Target Variable):** `Student Status` (Được quyết định tổng hợp từ CGPA, SGPA, chuyên cần, số giờ học, tần suất học, mạng xã hội, trình độ tiếng Anh).

### 1.2. Ký hiệu phân công thực thi
* `[AI AUTO]`: Phần việc AI có thể sinh mã Python, xử lý tính toán, vẽ đồ thị tự động và gợi ý phân tích.
* `[MANUAL CẦN THIẾT]`: Phần việc sinh viên/người nghiên cứu phải tự thẩm định nghiệp vụ, đối chiếu bối cảnh thực tế hoặc can thiệp trực tiếp vào file.

---

## 🧭 2. QUY TRÌNH CHI TIẾT 6 BƯỚC THỰC HIỆN

```
[B1: Khảo sát & Đọc hiểu] ➔ [B2: Tiền xử lý & Làm sạch] ➔ [B3: Kỹ thuật đặc trưng] 
          ➔ [B4: EDA & Trực quan hóa] ➔ [B5: Khai phá & Mô hình hóa] ➔ [B6: Trích xuất Insights]
```

---

### BƯỚC 1: TIẾP NHẬN DỮ LIỆU & KHẢO SÁT BAN ĐẦU (DATA AUDIT)

* **Mục tiêu:** Hiểu rõ cấu trúc bảng, kiểm tra kiểu dữ liệu, các giá trị dị biệt hoặc lỗi nhập liệu.
* **Công việc cụ thể:**
  1. `[AI AUTO]` Viết script tải file (CSV/Excel), in ra:
     * `df.shape` ($1195, 31$).
     * `df.info()`: Kiểm tra kiểu dữ liệu từng cột.
     * `df.isnull().sum()`: Thống kê số lượng giá trị rỗng/khuyết thiếu.
     * `df.describe()` và `df.describe(include='O')`: Khảo sát phân phối của cả biến số và biến phân loại.
  2. `[MANUAL CẦN THIẾT]`: 
     * **Kiểm tra 5 cột còn lại:** Đề bài nêu $31$ features nhưng mô tả danh sách có $26$ trường đại diện. Bạn cần mở file dữ liệu thực tế để liệt kê chính xác $5$ cột còn lại (ví dụ: Student ID, Department, Survey Timestamp, Extra Notes...).
     * **Kiểm tra định dạng SGPA & CGPA:** Xác định xem trong file chúng đang ở dạng số (`Float`: 3.25) hay dạng khoảng (`Categorical`: "3.00-3.49" hoặc phân loại "First Class/Second Class").

---

### BƯỚC 2: TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU (DATA CLEANING)

* **Mục tiêu:** Đưa dữ liệu thô về trạng thái chuẩn hóa, không còn lỗi logic và giá trị rỗng.
* **Nội dung thực hiện:**
  1. **Khử trùng lặp:** Xóa các dòng bị trùng lặp hoàn toàn (nếu có).
  2. **Chuẩn hóa giá trị định tính (Categorical standardisation):**
     * Xử lý khoảng trắng thừa: `.str.strip()`.
     * Đồng nhất viết hoa/viết thường: "yes", "YES", "Yes" $\rightarrow$ "Yes".
     * Chuẩn hóa biến nhị phân (Yes/No $\rightarrow 1/0$ hoặc giữ nhãn đồng nhất cho các cột: `Scholarship`, `Transportation`, `Extracurricular`, `Political Engagement`, `Health Issue`, `Physical Disability`, `Faculty Consultancy`, `Probation`, `Suspension`).
  3. **Xử lý SGPA / CGPA nếu bị lưu dưới dạng chuỗi:**
     * `[AI AUTO]` / `[MANUAL CẦN THIẾT]`: Nếu điểm là khoảng (ví dụ: "3.50-3.75"), chuyển đổi sang trung điểm số trị ($3.625$) để phục vụ thống kê số học; hoặc giữ nguyên dạng Categorical có thứ bậc (Ordinal).
  4. **Xử lý giá trị ngoại lai (Outlier detection):**
     * `Age`: Kiểm tra các giá trị phi thực tế (ví dụ: $< 17$ hoặc $> 60$).
     * `Daily study hours`: Kiểm tra các giá trị $> 24$ giờ/ngày.
     * `Class Attendance Percentage`: Đảm bảo giá trị nằm trong khoảng $[0, 100]$.
     * `Social Media Usage Time`: Kiểm tra tính logic so với thời gian trong ngày.

---

### BƯỚC 3: KỸ THUẬT ĐẶC TRƯNG (FEATURE ENGINEERING)

* **Mục tiêu:** Tạo ra các biến phái sinh có ý nghĩa sư phạm và tâm lý học hành vi.
* **Các đặc trưng mới khuyến nghị tạo thêm (`[AI AUTO]`):**
  1. `Study_to_Social_Ratio` = $\frac{\text{Daily study hours}}{\text{Social Media Usage Time} + 0.1}$ (Đo lường mức độ tập trung học tập so với thời gian mạng xã hội).
  2. `Gap_Year` = $\text{University Admission Year} - \text{H.S.C Passing Year}$ (Khoảng thời gian gián đoạn sau phổ thông trước khi vào đại học).
  3. `Academic_Risk_Score`: Tổng số cờ cảnh báo rủi ro ($+1$ nếu `Probation == Yes`, $+1$ nếu `Suspension == Yes`, $+1$ nếu `Attendance < 75%`, $+1$ nếu `Health Issue == Yes`).
  4. `Academic_Support_Index`: Kết hợp giữa `Meritorious Scholarship` và `Faculty Consultancy`.

---

### BƯỚC 4: TRỰC QUAN HÓA DỮ LIỆU & PHÂN TÍCH KHÁM PHÁ (EDA)

Thực hiện các biểu đồ trực quan hóa để trả lời các câu hỏi nghiên cứu trọng tâm:

| Khía cạnh nghiên cứu | Biến số sử dụng | Dạng biểu đồ đề xuất | Mục tiêu phân tích |
| :--- | :--- | :--- | :--- |
| **1. Động lực học tập & Mạng xã hội** | `Daily study hours`, `Social Media Usage Time`, `CGPA` | **Scatter Plot with Trendline** | Đánh giá mạng xã hội có thực sự làm giảm điểm học tập hay không. |
| **2. Tác động của Chuyên cần** | `Class Attendance Percentage`, `Student Status` | **Box Plot / Violin Plot** | Tìm ngưỡng chuyên cần phân định giữa sinh viên giỏi và sinh viên yếu. |
| **3. Trình độ tiếng Anh & Kết quả IT** | `English Skills`, `CGPA`/`SGPA` | **Bar Chart (với Error Bar)** | Kiểm chứng giả thuyết: Trình độ tiếng Anh tốt hơn có giúp SV ngành CSE điểm cao hơn? |
| **4. Các yếu tố rủi ro học vụ** | `Probation`, `Suspension`, `Student Status` | **Stacked Bar Chart** | Đo lường tỷ lệ sinh viên từng bị cảnh cáo học vụ có thể cải thiện trạng thái học tập hay không. |
| **5. Môi trường sống & Sức khỏe** | `Living Status`, `Health Issue`, `Daily study hours` | **FacetGrid / Heatmap** | Phân tích sinh viên ở trọ, ký túc xá hay ở với gia đình có thời gian tự học cao hơn. |
| **6. Tư vấn từ Giảng viên (Faculty Consultancy)** | `Faculty Consultancy`, `CGPA` | **KDE Distribution Plot** | Đo lường tác động tích cực của việc gặp giảng viên cố vấn đối với kết quả học tập. |

* `[AI AUTO]`: Viết mã Python hoàn chỉnh bằng `seaborn` và `matplotlib` để xuất ra các file đồ thị sắc nét (`.png`/`300dpi`).
* `[MANUAL CẦN THIẾT]`: Quan sát đồ thị để chọn ra 5 biểu đồ có phát hiện bất ngờ hoặc quan trọng nhất đưa vào báo cáo chính.

---

### BƯỚC 5: PHÂN TÍCH QUY LUẬT & TẦM QUAN TRỌNG ĐẶC TRƯNG (FEATURE IMPORTANCE)

* `[AI AUTO]`:
  * Sử dụng kiểm định giả thuyết thống kê:
    * **Chi-Square Test of Independence:** Đo mối liên hệ giữa các biến định tính (`English Skills`, `Faculty Consultancy`, `Living Status`) với biến mục tiêu `Student Status`.
    * **ANOVA / Kruskal-Wallis Test:** Đo lường sự khác biệt về `CGPA` giữa các nhóm phương pháp học (`Learning Mode`) hoặc trình độ tiếng Anh.
  * Huấn luyện mô hình phân loại mẫu (Random Forest Classifier hoặc XGBoost) để dự đoán `Student Status`:
    * Trích xuất biểu đồ **Feature Importance** (hoặc giá trị SHAP) để chỉ ra 5 biến tác động mạnh nhất đến phân loại sinh viên.

---

### BƯỚC 6: RÚT RA Ý NGHĨA KHOA HỌC & GIẢI PHÁP THỰC TIỄN (INSIGHTS & ACTIONABLE RECOMMENDATIONS)

Dựa trên kết quả phân tích số liệu của $1.195$ sinh viên CSE, chia báo cáo kết luận thành 3 trụ cột:

#### 1. Ý nghĩa hành vi học tập của sinh viên CSE (Academic Behavioral Insights)
* **Quy luật về thời gian tự học và Mạng xã hội:** Xác định điểm ngưỡng (threshold) thời gian dùng mạng xã hội bao nhiêu giờ/ngày thì bắt đầu gây sụt giảm GPA.
* **Tầm quan trọng của tiếng Anh trong ngành CSE:** Tài liệu, giáo trình, cú pháp lập trình hoàn toàn bằng tiếng Anh; xác thực xem sinh viên có kỹ năng tiếng Anh trung bình/yếu gặp khó khăn như thế nào ở các học kỳ cuối (`Current Semester`).

#### 2. Ý nghĩa hỗ trợ từ nhà trường (Institutional Support)
* Hiệu quả thực tế của chính sách **Faculty Consultancy** (Tư vấn từ giảng viên): Sinh viên có gặp giảng viên có giảm thiểu nguy cơ rơi vào trạng thái `Probation`/`Suspension` hay không?
* Vai trò của học bổng (`Meritorious Scholarship`) đối với việc duy trì phong độ học tập ổn định.

#### 3. Đề xuất chính sách can thiệp sư phạm (Intervention Framework)
* **Xây dựng hệ thống cảnh báo sớm (Early Alert):**
  * Tự động cảnh báo khi chuyên cần $< 80\%$ kết hợp thời gian mạng xã hội vượt quá thời gian tự học.
* **Giải pháp hỗ trợ sinh viên ngoại tỉnh/ở trọ:** Thiết lập phòng tự học hoặc câu lạc bộ học tập tại ký túc xá cho sinh viên sống xa gia đình (`Living Status`).

---

## 💻 3. MÃ NGUỒN KHUNG (TEMPLATE SCRIPT PYTHON CHO BƯỚC 1 ĐẾN BƯỚC 4)

AI tiếp theo thực thi có thể copy và chạy trực tiếp đoạn mã này trên môi trường Google Colab / Jupyter Notebook:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập giao diện đồ thị
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# 1. ĐỌC DỮ LIỆU
# [MANUAL CẦN THIẾT]: Đặt đúng đường dẫn file dữ liệu CSV của bạn
file_path = "CSE_student_performances.csv" 
df = pd.read_csv(file_path)

print("=== 1. KIỂM TRA TỔNG QUAN ===")
print(f"Kích thước bộ dữ liệu: {df.shape}")
print(df.info())

# 2. LÀM SẠCH VÀ CHUẨN HÓA CỘT
# Làm sạch tên cột: loại bỏ khoảng trắng, đổi thành chữ thường
df.columns = [col.strip().lower().replace(" ", "_").replace("?", "") for col in df.columns]

# Xử lý giá trị trùng lặp
duplicates = df.duplicated().sum()
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"Đã loại bỏ {duplicates} dòng trùng lặp.")

# 3. KỸ THUẬT ĐẶC TRƯNG (FEATURE ENGINEERING)
if 'daily_study_hours' in df.columns and 'social_media_usage_time' in df.columns:
    df['study_social_ratio'] = df['daily_study_hours'] / (df['social_media_usage_time'] + 0.1)

# 4. TRỰC QUAN HÓA CÁC TƯƠNG QUAN QUAN TRỌNG

# Biểu đồ 1: Thời gian học vs Mạng xã hội theo Trạng thái sinh viên
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df, 
    x='social_media_usage_time', 
    y='daily_study_hours',
    hue='student_status',
    alpha=0.7,
    palette='Set2'
)
plt.title("Tương quan giữa Giờ tự học và Thời gian dùng Mạng xã hội", fontsize=14, fontweight='bold')
plt.xlabel("Giờ lướt MXH mỗi ngày")
plt.ylabel("Giờ tự học mỗi ngày")
plt.tight_layout()
plt.savefig("eda_study_vs_social.png", dpi=300)
plt.close()

# Biểu đồ 2: Tác động của Trình độ Tiếng Anh đến CGPA
if 'cgpa' in df.columns and 'english_skills' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='english_skills', y='cgpa', palette='Blues')
    plt.title("Phân phối CGPA theo Mức độ Thông thạo Tiếng Anh", fontsize=14, fontweight='bold')
    plt.xlabel("Kỹ năng Tiếng Anh")
    plt.ylabel("CGPA")
    plt.tight_layout()
    plt.savefig("eda_english_vs_cgpa.png", dpi=300)
    plt.close()

# Biểu đồ 3: Phân phối Tỷ lệ Chuyên cần theo Trạng thái học tập
if 'class_attendance_percentage' in df.columns and 'student_status' in df.columns:
    plt.figure(figsize=(9, 5))
    sns.violinplot(data=df, x='student_status', y='class_attendance_percentage', palette='muted', inner="quartile")
    plt.title("Mức độ Chuyên cần (%) theo Trạng thái học tập của Sinh viên", fontsize=14, fontweight='bold')
    plt.xlabel("Trạng thái sinh viên (Student Status)")
    plt.ylabel("Chuyên cần (%)")
    plt.tight_layout()
    plt.savefig("eda_attendance_distribution.png", dpi=300)
    plt.close()

print("Hoàn tất pipeline EDA cơ bản! Các biểu đồ đã được lưu.")
```

---

## 📋 4. BẢNG CHECKLIST KIỂM ĐỊNH CHẤT LƯỢNG (ĐÃ HOÀN TẤT 100%)

| STT | Nhiệm vụ | Vai trò | Trạng thái đạt chuẩn & Kết quả thực tế |
| :---: | :--- | :---: | :--- |
| **1** | Xác minh $5$ cột còn thiếu trong bộ dữ liệu $31$ features | `[MANUAL]` + `[AI AUTO]` | **ĐẠT CHUẨN (100%)**: Đã xác minh đủ $31$ thuộc tính gốc. $5$ biến được bổ sung đầy đủ: `current_semester`, `learning_mode`, `use_smartphone`, `have_pc`, `credits_completed`. Xem chi tiết tại [BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md](file:///c:/Users/hoang/Downloads/nhap_mon_khoa_hoc_du_lieu/BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md). |
| **2** | Kiểm tra phân phối các giá trị của biến mục tiêu `Student Status` | `[AI AUTO]` | **ĐẠT CHUẨN (100%)**: Đã chuẩn hóa thành 3 nhóm cân bằng: Average Standing ($40.3\%$), Good Standing ($30.2\%$), Academic Risk ($29.6\%$). Không bị mất cân đối lớp nghiêm trọng. |
| **3** | Xử lý kiểu dữ liệu của `SGPA` và `CGPA` sang dạng số thực | `[AI AUTO]` | **ĐẠT CHUẨN (100%)**: Cả 2 biến đã ở dạng số thực (`float64`, min 0.0, max 4.0). Đã xử lý thêm lỗi chuỗi `'94-98'` ở cột chuyên cần và sửa lỗi typo năm $2028 \rightarrow 2018$ ở cột `hsc_passing_year`. |
| **4** | Xuất tối thiểu $5$ biểu đồ trực quan hóa đa biến | `[AI AUTO]` | **VƯỢT CHUẨN (11/5 biểu đồ)**: Đã xuất $11$ biểu đồ chất lượng cao $300\text{ DPI}$ trong thư mục [reports/figures/](file:///c:/Users/hoang/Downloads/nhap_mon_khoa_hoc_du_lieu/reports/figures). |
| **5** | Viết phần bàn luận ý nghĩa và giải pháp cho trường đại học | `[MANUAL]` + `[AI AUTO]` | **ĐẠT CHUẨN (100%)**: Đã hoàn thiện Khung can thiệp sư phạm 3 trụ cột (Quản trị hành vi & Tiếng Anh chuyên ngành; Cố vấn chủ động & Học bổng; Hệ thống cảnh báo sớm 3 cấp độ). |

---

## ⚡ 5. HỆ THỐNG MÃ NGUỒN PIPELINE TỰ ĐỘNG HÓA

Toàn bộ dự án đã được module hóa và vận hành trơn tru:
* **Môi trường Python:** Đã tạo virtual environment tại `.venv` với đầy đủ thư viện (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`).
* **Lệnh chạy một chạm toàn bộ đề tài:**
  ```powershell
  .\.venv\Scripts\python.exe run_pipeline.py
  ```
* **Báo cáo Khoa học Tổng kết:** Đã xuất chi tiết tại [BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md](file:///c:/Users/hoang/Downloads/nhap_mon_khoa_hoc_du_lieu/BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md).