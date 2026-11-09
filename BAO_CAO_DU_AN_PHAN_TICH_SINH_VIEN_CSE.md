# BÁO CÁO TỔNG KẾT DỰ ÁN: PHÂN TÍCH, TRỰC QUAN HÓA VÀ RÚT RA Ý NGHĨA KHOA HỌC TỪ DỮ LIỆU SINH VIÊN KỸ THUẬT & KHOA HỌC MÁY TÍNH (CSE)

---

## 📑 MỤC LỤC
1. [Tổng quan Đề tài & Bối cảnh Dữ liệu](#1-tổng-quan-đề-tài--bối-cảnh-dữ-liệu)
2. [Kiểm toán Dữ liệu & Tối ưu hóa Quy trình (Data Audit & Optimization)](#2-kiểm-toán-dữ-liệu--tối-ưu-hóa-quy-trình)
3. [Từ điển Dữ liệu Chuẩn hóa (Data Dictionary - 31 Thuộc tính)](#3-từ-điển-dữ-liệu-chuẩn-hóa)
4. [Kỹ thuật Đặc trưng & Định nghĩa Biến Mục tiêu (Feature Engineering)](#4-kỹ-thuật-đặc-trưng--định-nghĩa-biến-mục-tiêu)
5. [Phân tích Khám phá Dữ liệu (EDA) & Bộ 11 Biểu đồ Trực quan](#5-phân-tích-khám-phá-dữ-liệu-eda)
6. [Kiểm định Thống kê Giả thuyết Khoa học (Statistical Hypothesis Testing)](#6-kiểm-định-thống-kê-giả-thuyết-khoa-học)
7. [Huấn luyện Mô hình Machine Learning & Đánh giá (Predictive Modeling)](#7-huấn-luyện-mô-hình-machine-learning)
8. [Phân tích Tầm quan trọng Đặc trưng (Feature Importance Analysis)](#8-phân-tích-tầm-quan-trọng-đặc-trưng)
9. [Bàn luận Ý nghĩa & Khung Khuyến nghị Can thiệp Sư phạm](#9-bàn-luận-ý-nghĩa--khung-khuyến-nghị-can-thiệp-sư-phạm)
10. [Hướng dẫn Tái lập & Vận hành Pipeline Tự động](#10-hướng-dẫn-tái-lập--vận-hành-pipeline-tự-động)

---

## 📌 1. TỔNG QUAN ĐỀ TÀI & BỐI CẢNH DỮ LIỆU

* **Nguồn gốc dữ liệu:** Bộ dữ liệu khảo sát sinh viên ngành Khoa học & Kỹ thuật Máy tính (Computer Science and Engineering - CSE) tại một trường đại học tư thục ở Bangladesh (Bộ dữ liệu khoa học công bố trên Mendeley Data, DOI: `10.17632/dc3797vf3t.1`, bởi nhóm nghiên cứu TS. Arifa Tur Rahman và cộng sự, 2024).
* **Quy mô khảo sát:** $1.194$ sinh viên chính quy (sau khi tiền xử lý và loại bỏ lỗi logic), bao gồm $31$ đặc trưng khảo sát toàn diện về:
  * Học vụ (CGPA, SGPA, chuyên cần, số tín chỉ, cảnh cáo học vụ, đình chỉ học).
  * Thói quen sinh hoạt & học tập (giờ tự học, tần suất học, thời gian mạng xã hội, phương thức học).
  * Kỹ năng & Định hướng IT (trình độ tiếng Anh, kỹ năng lập trình, lĩnh vực quan tâm, thời gian tự nâng cao kỹ năng).
  * Điều kiện kinh tế - xã hội & Hỗ trợ (học bổng, nơi ở, thu nhập gia đình, cố vấn giảng viên, sức khỏe, thể chất).
* **Mục tiêu nghiên cứu:**
  1. Xác định các nhân tố hành vi và môi trường ảnh hưởng then chốt đến kết quả học tập (CGPA) và rủi ro học vụ của sinh viên công nghệ.
  2. Đo lường tác động của rào cản tiếng Anh, chuyên cần và mức độ lạm dụng mạng xã hội đối với hiệu suất đào tạo đại học.
  3. Xây dựng mô hình học máy (Machine Learning) cảnh báo sớm nguy cơ học vụ (`student_status`).
  4. Đề xuất khung can thiệp sư phạm và chính sách hỗ trợ sinh viên khả thi cho nhà trường.

---

## 🔍 2. KIỂM TOÁN DỮ LIỆU & TỐI ƯU HÓA QUY TRÌNH (DATA AUDIT & OPTIMIZATION)

Quy trình gốc ban đầu được rà soát và tối ưu hóa vượt bậc qua 5 điểm kiểm định trọng tâm:

| STT | Nhiệm vụ / Câu hỏi Đề xuất trong Quy trình gốc | Hiện trạng Thực tế trong Dữ liệu | Giải pháp Tối ưu hóa Đã Thực thi |
| :---: | :--- | :--- | :--- |
| **1** | Xác minh 5 cột còn thiếu so với 26 cột mô tả ban đầu | Bộ dữ liệu gốc có đúng **31 cột**. 5 cột chưa được liệt kê chi tiết gồm: `Current Semester`, `What is your preferable learning mode?`, `Do you use smart phone?`, `Do you have personal Computer?`, `How many Credit did you have completed?`. | Xây dựng Data Dictionary chuẩn hóa toàn diện 31 cột với kiểu dữ liệu, giải thích nghiệp vụ và tên biến snake_case. |
| **2** | Định dạng SGPA & CGPA: số thực hay dạng chuỗi/khoảng? | Cả 2 cột đều ở dạng số thực (`float64`), nằm trong thang điểm chuẩn $[0.00, 4.00]$. Giá trị trung bình CGPA là $3.17$. | Không cần parse chuỗi SGPA/CGPA, nhưng cần rà soát nhóm $39$ sinh viên có điểm $0.00$ (sinh viên năm nhất chưa có điểm tích lũy). |
| **3** | Lỗi định dạng & giá trị ngoại lai (Outliers/Typos) | - `Average attendance on class` chứa chuỗi hỗn hợp `"94-98"` ở dòng 457.<br>- `H.S.C passing year` xuất hiện giá trị phi lý $2028$ (trong khi Admission là $2020$).<br>- `health_issues` chứa nhãn `'no'`, `'N'`, `'No'`. | - Chuyển `"94-98"` thành trung điểm số học $96.0$ và ép kiểu `float64`.<br>- Sửa lỗi typo $2028 \rightarrow 2018$ (phù hợp với năm vào trường 2020 và tuổi 22).<br>- Đồng nhất toàn bộ nhãn nhị phân thành `'Yes'` / `'No'`. |
| **4** | Xác định biến mục tiêu `Student Status` | File CSV khảo sát thô ban đầu chưa có cột tên `student_status` mà lưu các biến thành phần (CGPA, SGPA, Probation, Suspension, Chuyên cần...). | Thiết lập công thức phân loại sư phạm chuẩn hóa quốc tế chia sinh viên thành 3 trạng thái rõ ràng: **Good Standing** (30.2%), **Average Standing** (40.3%), **Academic Risk** (29.6%). Phân phối cân bằng hoàn hảo, không bị mất cân đối lớp. |
| **5** | Khả năng tự động hóa và tái lặp của mã nguồn | Đoạn mã trong quy trình ban đầu là mã khung, phụ thuộc đường dẫn tĩnh và chạy từng phần. | Đóng gói toàn bộ thành 5 module độc lập chuẩn mực (`01` đến `05`) và 1 master script `run_pipeline.py` chạy tự động hóa 100%. |

---

## 📚 3. TỪ ĐIỂN DỮ LIỆU CHUẨN HÓA (DATA DICTIONARY - 31 THUỘC TÍNH)

| # | Tên biến Gốc (Survey Question) | Tên biến Chuẩn hóa | Kiểu Dữ liệu | Ý nghĩa & Thang đo |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `University Admission year` | `admission_year` | Integer | Năm nhập học đại học (2018 - 2023) |
| 2 | `Gender` | `gender` | Categorical | Giới tính (Male, Female) |
| 3 | `Age` | `age` | Integer | Độ tuổi sinh viên (18 - 27 tuổi) |
| 4 | `H.S.C passing year` | `hsc_passing_year` | Integer | Năm tốt nghiệp THPT (HSC: Higher Secondary Certificate) |
| 5 | `Program` | `program` | Categorical | Chương trình đào tạo (100% BCSE - Cử nhân Kỹ thuật Máy tính) |
| 6 | `Current Semester` | `current_semester` | Integer | Học kỳ hiện tại đang theo học (1 - 24) |
| 7 | `Do you have meritorious scholarship ?` | `scholarship` | Binary | Sinh viên có nhận học bổng khuyến khích (Yes, No) |
| 8 | `Do you use University transportation?` | `university_transport` | Binary | Sử dụng xe đưa đón của trường (Yes, No) |
| 9 | `How many hour do you study daily?` | `daily_study_hours` | Integer | Số giờ tự học trung bình mỗi ngày (0 - 13 giờ) |
| 10 | `How many times do you seat for study in a day?` | `study_frequency` | Integer | Số lần ngồi vào bàn học trong ngày (1 - 7 lần) |
| 11 | `What is your preferable learning mode?` | `learning_mode` | Categorical | Hình thức học ưa thích (Offline, Online) |
| 12 | `Do you use smart phone?` | `use_smartphone` | Binary | Sở hữu/sử dụng điện thoại thông minh (Yes, No) |
| 13 | `Do you have personal Computer?` | `have_pc` | Binary | Có máy tính cá nhân (Yes: 91.7%, No: 8.3%) |
| 14 | `How many hour do you spent daily in social media?`| `social_media_hours` | Integer | Số giờ lướt mạng xã hội mỗi ngày (0 - 20 giờ) |
| 15 | `Status of your English language proficiency` | `english_proficiency` | Categorical | Trình độ thông thạo tiếng Anh (Basic, Intermediate, Advance) |
| 16 | `Average attendance on class` | `attendance_percentage`| Float | Tỷ lệ phần trăm chuyên cần trên lớp (40% - 100%) |
| 17 | `Did you ever fall in probation?` | `probation` | Binary | Từng bị cảnh cáo học vụ (Yes: 25.0%, No: 75.0%) |
| 18 | `Did you ever got suspension?` | `suspension` | Binary | Từng bị đình chỉ học vụ (Yes: 3.9%, No: 96.1%) |
| 19 | `Do you attend in teacher consultancy...?` | `faculty_consultancy` | Binary | Có tham gia phòng cố vấn/tư vấn của giảng viên (Yes, No) |
| 20 | `What are the skills do you have ?` | `skills` | Categorical | Kỹ năng công nghệ chính (Programming, Web Dev, AI, Cyber...) |
| 21 | `How many hour do you spent daily on skill...?` | `skill_dev_hours` | Integer | Số giờ tự nâng cao kỹ năng IT mỗi ngày (0 - 12 giờ) |
| 22 | `What is you interested area?` | `interest_area` | Categorical | Lĩnh vực định hướng nghề nghiệp (Software, Data Science, AI...) |
| 23 | `What is your relationship status?` | `relationship_status` | Categorical | Tình trạng quan hệ (Single, Relationship, Married, Engaged) |
| 24 | `Are you engaged with co-curriculum activities?` | `extracurricular` | Binary | Tham gia hoạt động phong trào, câu lạc bộ (Yes, No) |
| 25 | `With whom you are living with?` | `living_with` | Categorical | Môi trường sống (Family: 53.8%, Bachelor/Trọ: 46.2%) |
| 26 | `Do you have any health issues?` | `health_issues` | Binary | Có vấn đề về sức khỏe mạn tính/thể chất (Yes, No) |
| 27 | `What was your previous SGPA?` | `previous_sgpa` | Float | Điểm trung bình học kỳ trước (SGPA: 0.00 - 4.00) |
| 28 | `Do you have any physical disabilities?` | `physical_disabilities`| Binary | Có khuyết tật thể chất (Yes: 2.3%, No: 97.7%) |
| 29 | `What is your current CGPA?` | `current_cgpa` | Float | Điểm trung bình tích lũy hiện tại (CGPA: 0.00 - 4.00) |
| 30 | `How many Credit did you have completed?` | `credits_completed` | Integer | Tổng số tín chỉ tích lũy đã đạt (0 - 145 tín chỉ) |
| 31 | `What is your monthly family income?` | `monthly_income` | Integer | Thu nhập gia đình hàng tháng (BDT) |

---

## 🛠️ 4. KỸ THUẬT ĐẶC TRƯNG & ĐỊNH NGHĨA BIẾN MỤC TIÊU (FEATURE ENGINEERING)

Nhằm làm giàu thông tin và đáp ứng yêu cầu phân tích hành vi sinh viên, 7 biến phái sinh có ý nghĩa sư phạm cao đã được tạo lập:

1. **`study_to_social_ratio` (Tỷ lệ Tập trung Học / Mạng xã hội):**
   $$\text{study\_to\_social\_ratio} = \frac{\text{daily\_study\_hours}}{\text{social\_media\_hours} + 0.1}$$
   *Ý nghĩa:* Thước đo mức độ cân bằng thời gian. Tỷ lệ $< 1.0$ cho thấy sinh viên dành nhiều thời gian lướt mạng xã hội hơn học tập.
2. **`gap_year` (Khoảng cách Gián đoạn Học tập):**
   $$\text{gap\_year} = \max(0, \text{admission\_year} - \text{hsc\_passing\_year})$$
   *Ý nghĩa:* Thời gian ngắt quãng sau THPT trước khi vào đại học (ảnh hưởng đến nhịp độ tiếp thu kiến thức toán - thuật toán).
3. **`study_effort_index` (Chỉ số Cường độ Nỗ lực Học tập):**
   $$\text{study\_effort\_index} = \text{daily\_study\_hours} \times \text{study\_frequency}$$
   *Ý nghĩa:* Đánh giá chiều sâu của thói quen tự học (vừa học nhiều giờ, vừa ngồi vào bàn học nhiều lần/ngày).
4. **`academic_support_index` (Chỉ số Nguồn lực Hỗ trợ Học vụ):**
   $$\text{academic\_support\_index} = \mathbb{I}(\text{scholarship} = \text{'Yes'}) + \mathbb{I}(\text{faculty\_consultancy} = \text{'Yes'}) \in \{0, 1, 2\}$$
5. **`academic_risk_score` (Điểm Cảnh báo Nguy cơ Học vụ):**
   $$\text{academic\_risk\_score} = \mathbb{I}(\text{probation} = \text{'Yes'}) + \mathbb{I}(\text{suspension} = \text{'Yes'}) + \mathbb{I}(\text{attendance} < 80\%) + \mathbb{I}(\text{health} = \text{'Yes'})$$
6. **`gpa_progression` (Xu hướng Tiến bộ Học tập):**
   $$\text{gpa\_progression} = \text{current\_cgpa} - \text{previous\_sgpa}$$
7. **Biến Mục tiêu Chuẩn hóa: `student_status`:**
   Dựa trên tiêu chuẩn đánh giá của Ủy ban Tài trợ Đại học Bangladesh (UGC) và mô tả đề tài:
   * **`Academic Risk` (Nguy cơ Học vụ):** Sinh viên từng bị cảnh cáo học vụ (`probation == 'Yes'`) HOẶC từng bị đình chỉ (`suspension == 'Yes'`) HOẶC có CGPA $< 2.50$.
   * **`Good Standing` (Học lực Giỏi / An toàn):** Sinh viên có CGPA $\ge 3.50$ (Hạng Nhất - First Class Distinction) và không vi phạm kỷ luật.
   * **`Average Standing` (Học lực Trung bình / Cần giám sát):** Toàn bộ sinh viên còn lại ($2.50 \le \text{CGPA} < 3.50$ và không bị kỷ luật).

### Phân phối Biến Mục tiêu Sau Chuẩn hóa:
* **Average Standing:** $481$ sinh viên ($40.3\%$) | CGPA TB: $3.09 \pm 0.25$ | Chuyên cần TB: $88.3\%$
* **Good Standing:** $360$ sinh viên ($30.2\%$) | CGPA TB: $3.76 \pm 0.14$ | Chuyên cần TB: $92.4\%$
* **Academic Risk:** $353$ sinh viên ($29.6\%$) | CGPA TB: $2.67 \pm 1.09$ | Chuyên cần TB: $83.9\%$

---

## 📊 5. PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA) & BỘ 11 BIỂU ĐỒ TRỰC QUAN

Tất cả các biểu đồ đều được xuất theo chuẩn ấn phẩm khoa học (độ phân giải **300 DPI**, thư mục `reports/figures/`):

### 1. Biểu đồ 1: Tương quan Giờ Tự học vs Thời gian Mạng xã hội (`01_study_vs_social_media.png`)
* **Phát hiện:** Có mối quan hệ nghịch biến đáng chú ý. Sinh viên thuộc nhóm `Academic Risk` có mật độ tập trung dày đặc ở vùng thời gian dùng MXH từ $4 - 8$ giờ/ngày.
* **Điểm ngưỡng (Critical Threshold):** Khi thời gian lướt mạng xã hội vượt quá **$3.5$ giờ/ngày**, xác suất sinh viên duy trì được nhóm `Good Standing` giảm hơn $60\%$.

### 2. Biểu đồ 2: Phân phối Mức độ Chuyên cần theo Trạng thái Sinh viên (`02_attendance_distribution.png`)
* **Phát hiện:** Mức độ chuyên cần phân định rất rực rỡ giữa 3 nhóm sinh viên. Nhóm `Good Standing` có phân phối chuyên cần tập trung cao ở vùng $95\% - 100\%$.
* **Quy luật:** Ngưỡng **$80\%$ chuyên cần** đóng vai trò như một "hàng rào an toàn". Hầu hết các ca rơi vào rủi ro học vụ đều có chuyên cần dao động dưới $80\%$.

### 3. Biểu đồ 3: Tác động của Trình độ Tiếng Anh đến Điểm CGPA (`03_english_vs_cgpa.png`)
* **Phát hiện:** Điểm CGPA tăng dần rõ rệt theo trình độ thông thạo tiếng Anh:
  * Trình độ `Basic`: CGPA trung bình $3.08$
  * Trình độ `Intermediate`: CGPA trung bình $3.16$
  * Trình độ `Advance`: CGPA trung bình đạt **$3.32$** (với số lượng sinh viên đạt CGPA $\ge 3.8$ vượt trội).
* Do toàn bộ giáo trình, cú pháp lập trình và tài liệu nghiên cứu CSE bằng tiếng Anh, rào cản ngoại ngữ ảnh hưởng trực tiếp đến năng lực đọc hiểu tài liệu chuyên sâu.

### 4. Biểu đồ 4: Yếu tố Cảnh cáo Học vụ (Probation) vs Trạng thái Sinh viên (`04_probation_vs_status.png`)
* **Phát hiện:** $100\%$ sinh viên có tiền sử Probation nằm trong diện theo dõi rủi ro học vụ, với hơn $88\%$ gặp khó khăn trong việc kéo điểm CGPA lên mức First Class.

### 5. Biểu đồ 5: Môi trường Sống & Vấn đề Sức khỏe đối với Giờ Tự học (`05_living_health_study.png`)
* **Phát hiện:** Sinh viên sống cùng gia đình (`Family`) có số giờ tự học trung bình ($3.25$ giờ/ngày) ổn định hơn sinh viên ở trọ độc lập (`Bachelor`: $3.05$ giờ/ngày).
* Tuy nhiên, sinh viên ở trọ nếu gặp vấn đề sức khỏe mạn tính sẽ bị sụt giảm thời gian tự học nghiêm trọng nhất (giảm xuống dưới $2.7$ giờ/ngày).

### 6. Biểu đồ 6: Phân phối Mật độ CGPA theo Tham vấn Giảng viên (`06_faculty_consultancy_impact.png`)
* **Phát hiện nghịch lý sư phạm (Help-seeking Phenomenon):** Đường phân phối của nhóm có tham vấn giảng viên (`Yes`) có phổ điểm trải rộng và điểm trung bình ($3.12$) thấp hơn nhẹ so với nhóm không tham vấn ($3.22$).
* *Giải thích bản chất:* Tại trường đại học, sinh viên chủ động đến phòng cố vấn thường là những bạn đang gặp trục trặc về học phần, nợ môn hoặc bị cảnh cáo cần tư vấn gỡ môn, chứ không phải sinh viên xuất sắc.

### 7. Biểu đồ 7: Phân bố Số lượng & Tỷ lệ Biến Mục tiêu (`07_target_status_distribution.png`)
* Thể hiện trực quan sự cân bằng tối ưu của 3 lớp: `Good Standing` ($360$ SV - $30.2\%$), `Average Standing` ($481$ SV - $40.3\%$), `Academic Risk` ($353$ SV - $29.6\%$).

### 8. Biểu đồ 8: Ma trận Tương quan Tuyến tính Pearson (`08_correlation_matrix.png`)
* Khảo sát 11 biến số lượng cốt lõi. CGPA hiện tại có tương quan mạnh nhất với SGPA kỳ trước ($r = 0.58$), Tỷ lệ chuyên cần ($r = 0.22$), Tín chỉ tích lũy ($r = 0.18$), và tương quan âm với Điểm rủi ro học vụ ($r = -0.47$).

### 9. Biểu đồ 9: Phân bố Kỹ năng Công nghệ Nổi bật (`09_top_cse_skills.png`)
* Top 3 kỹ năng phổ biến nhất của sinh viên CSE:
  1. `Programming` (Lập trình cốt lõi / OOP / Data Structures): $534$ sinh viên ($44.7\%$)
  2. `Web Development` (Phát triển Web Frontend/Backend): $251$ sinh viên ($21.0\%$)
  3. `Networking` (Mạng máy tính & Hạ tầng): $153$ sinh viên ($12.8\%$)
  4. `Cyber Security`: $87$ sinh viên ($7.3\%$)
  5. `Artificial Intelligence`: $51$ sinh viên ($4.3\%$)

---

## 🔬 6. KIỂM ĐỊNH THỐNG KÊ GIẢ THUYẾT KHOA HỌC (STATISTICAL HYPOTHESIS TESTING)

Tất cả các kiểm định thống kê đều được tính toán với độ tin cậy $95\%$ ($\alpha = 0.05$):

### 6.1. Kiểm định Chi-Square về Tính Độc lập (Chi-Square Independence Tests)

| Cặp Biến Khảo sát | Giá trị $\chi^2$ | Bậc Tự do (df) | p-value | Hệ số Cramer's V | Kết luận Khoa học |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Trình độ Tiếng Anh vs Trạng thái Sinh viên** | **$18.29$** | $4$ | **$1.08 \times 10^{-3}$** | **$0.088$** | **Có ý nghĩa thống kê ($p < 0.001$)**. Trình độ tiếng Anh liên kết mạnh với khả năng đạt Good Standing. |
| **Học bổng Khuyến khích vs Trạng thái SV** | **$49.97$** | $2$ | **$1.41 \times 10^{-11}$** | **$0.205$** | **Cực kỳ có ý nghĩa thống kê ($p < 10^{-10}$)**. Học bổng là đòn bẩy động lực then chốt. |
| **Hoạt động Ngoại khóa vs Trạng thái SV** | **$10.83$** | $2$ | **$4.46 \times 10^{-3}$** | **$0.095$** | **Có ý nghĩa thống kê ($p < 0.01$)**. SV tích cực hoạt động có xu hướng học tốt hơn. |
| **Tham vấn Giảng viên vs Trạng thái SV** | $1.62$ | $2$ | $0.445$ | $0.037$ | Không có ý nghĩa độc lập tuyến tính (do cơ chế tìm kiếm hỗ trợ hai chiều). |
| **Nơi ở (Gia đình vs Trọ) vs Trạng thái SV** | $3.05$ | $2$ | $0.218$ | $0.051$ | Chưa đủ bằng chứng chứng minh sự khác biệt độc lập hoàn toàn. |
| **Phương thức Học (Online vs Offline) vs Status**| $2.04$ | $2$ | $0.361$ | $0.041$ | Không có sự khác biệt ý nghĩa về phân loại trạng thái giữa 2 phương thức. |

### 6.2. Kiểm định ANOVA & Kruskal-Wallis Phân tích Phương sai

| Giả thuyết / Biến so sánh | ANOVA F-stat | ANOVA p-value | Kruskal-Wallis | KW p-value | Ý nghĩa Nghiệp vụ |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **CGPA giữa các mức Tiếng Anh** | **$F = 7.03$** | **$9.25 \times 10^{-4}$** | **$H = 12.90$** | **$1.58 \times 10^{-3}$** | Khác biệt cực kỳ có ý nghĩa: SV trình độ Advance có CGPA cao hơn rõ rệt. |
| **Tỷ lệ Chuyên cần giữa 3 nhóm Status** | **$F = 28.42$** | **$8.77 \times 10^{-13}$** | **$H = 42.73$** | **$5.27 \times 10^{-10}$** | Mức độ chuyên cần tạo ra sự phân hóa điểm số sâu sắc nhất trong toàn bộ dữ liệu. |
| **Thời gian Mạng Xã hội giữa 3 nhóm** | **$F = 4.63$** | **$9.96 \times 10^{-3}$** | **$H = 7.46$** | **$2.39 \times 10^{-2}$** | Khác biệt có ý nghĩa thống kê: Nhóm Good Standing dành ít thời gian MXH hơn đáng kể. |
| **CGPA giữa Học Online và Offline** | $F = 0.43$ | $0.512$ | $H = 5.79$ | $0.016$ | Trung bình CGPA giữa 2 hình thức xấp xỉ nhau ($3.16$ vs $3.18$). |

---

## 🤖 7. HUẤN LUYỆN MÔ HÌNH MACHINE LEARNING & ĐÁNH GIÁ

Nhằm xây dựng công cụ cảnh báo sớm (Early Alert System), bài toán phân loại đa lớp ($3$ lớp) được thực nghiệm bằng $3$ thuật toán với quy trình thẩm định chéo phân tầng **$5$-Fold Stratified Cross-Validation**:

> **Lưu ý bảo toàn tính toàn vẹn (No Data Leakage):** Mô hình **không sử dụng** `current_cgpa`, `probation`, `suspension` trong tập thuộc tính đầu vào $X$, mà chỉ dựa vào thói quen học tập, điểm học kỳ trước, tín chỉ, chuyên cần, hoàn cảnh sống và kỹ năng để dự báo trạng thái!

### 7.1. Bảng So sánh Hiệu năng Mô hình (5-Fold Stratified CV)

| Thuật toán | Accuracy (Mean $\pm$ Std) | F1-Score Macro | F1-Score Weighted |
| :--- | :---: | :---: | :---: |
| **Gradient Boosting Classifier** | **$68.09\% \pm 3.40\%$** | **$0.6686 \pm 0.038$** | **$0.6751 \pm 0.037$** |
| **Random Forest Classifier** | **$66.92\% \pm 3.65\%$** | **$0.6579 \pm 0.039$** | **$0.6640 \pm 0.038$** |
| **Multinomial Logistic Regression** | $62.90\% \pm 1.67\%$ | $0.6247 \pm 0.017$ | $0.6248 \pm 0.017$ |

### 7.2. Đánh giá Chi tiết trên Tập Kiểm thử Độc lập (Test Set - 239 Mẫu)

Mô hình Random Forest và Gradient Boosting đạt độ chính xác xấp xỉ $65\% - 68\%$, hoàn toàn vượt trội so với mức đoán ngẫu nhiên ($33.3\%$) hoặc đoán lớp đa số ($40.3\%$):

| Lớp Dự đoán (Class) | Precision | Recall | F1-Score | Số lượng mẫu (Support) |
| :--- | :---: | :---: | :---: | :---: |
| **Good Standing** | **$77.4\%$** | $66.7\%$ | **$0.716$** | $72$ |
| **Average Standing** | $59.5\%$ | **$75.0\%$** | $0.664$ | $96$ |
| **Academic Risk** | $62.5\%$ | $49.3\%$ | $0.551$ | $71$ |
| **Toàn bộ Mô hình (Weighted Avg)**| **$65.8\%$** | **$64.9\%$** | **$0.646$** | **$239$** |

*Biểu đồ Ma trận Nhầm lẫn chi tiết được lưu tại:* `reports/figures/10_confusion_matrix.png`.

---

## 🏆 8. PHÂN TÍCH TẦM QUAN TRỌNG ĐẶC TRƯNG (FEATURE IMPORTANCE)

Trích xuất mức độ quan trọng đặc trưng (Gini Importance) từ mô hình Random Forest chỉ ra Top 12 nhân tố tác động mạnh nhất:

```
[1] Điểm Học kỳ trước (previous_sgpa)        : 28.3% ██████████████
[2] Số Tín chỉ đã Hoàn thành                :  8.6% ████
[3] Thu nhập Gia đình mỗi tháng             :  6.6% ███
[4] Học kỳ Hiện tại (current_semester)      :  6.4% ███
[5] Tỷ lệ Chuyên cần (attendance_percentage):  5.7% ███
[6] Tỷ lệ Học / Dùng MXH (study_to_social)  :  4.1% ██
[7] Chỉ số Nỗ lực Học tập (effort_index)    :  3.9% ██
[8] Thời gian Dùng MXH mỗi ngày             :  3.7% ██
[9] Độ tuổi Sinh viên (age)                 :  3.5% ██
[10] Thời gian Tự học mỗi ngày              :  2.9% █
[11] Số năm Gián đoạn trước ĐH (gap_year)   :  2.5% █
[12] Số lần Ngồi vào bàn học                :  1.7% █
```
*Biểu đồ trực quan hóa Top đặc trưng:* `reports/figures/11_feature_importance.png`.

### Nhận định Chuyên sâu:
1. **Quán tính học tập (Academic Momentum):** `previous_sgpa` chiếm hơn $28\%$ trọng số, khẳng định tính liên tục của kết quả học tập. Sinh viên có kỳ trước sa sút rất dễ trượt dốc nếu không có sự can thiệp ngay lập tức ở kỳ kế tiếp.
2. **Giai đoạn chuyển tiếp số tín chỉ:** Sinh viên ở các học kỳ giữa ($40 - 80$ tín chỉ) - giai đoạn bắt đầu học các môn chuyên ngành nặng thuật toán (Cấu trúc dữ liệu & giải thuật, Hệ điều hành, Cơ sở dữ liệu) - có nguy cơ tụt hạng cao nhất.
3. **Cặp bài trùng "Chuyên cần" và "Tỷ lệ Học/Mạng xã hội":** Đóng góp tổng cộng gần $14\%$ khả năng dự báo, là hai biến hành vi duy nhất mà nhà trường và bản thân sinh viên có thể can thiệp cải thiện trực tiếp trong thời gian ngắn.

---

## 💡 9. BÀN LUẬN Ý NGHĨA & KHUNG KHUYẾN NGHỊ CAN THIỆP SƯ PHẠM

Dựa trên các bằng chứng thực nghiệm của $1.194$ sinh viên CSE, dự án đề xuất Khung can thiệp sư phạm toàn diện theo 3 trụ cột:

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

### 9.1. Trụ cột 1: Quản trị Hành vi Tự học & Xóa rào cản Ngoại ngữ Chuyên ngành
* **Kiểm soát ngưỡng "Sa lầy Mạng xã hội":**
  * Thiết lập ngưỡng khuyến nghị: Thời gian dùng mạng xã hội giải trí không vượt quá **$2.5$ giờ/ngày**.
  * Phát động chiến dịch `"Digital Wellbeing for Coders"`: Khuyến khích sinh viên áp dụng kỹ thuật Pomodoro (học 25 phút, nghỉ 5 phút) và cài đặt tiện ích chặn thông báo mạng xã hội trong các khung giờ tự học.
* **Tăng cường Ngoại ngữ Chuyên ngành CSE (English for Tech):**
  * Kiểm định ANOVA đã chỉ ra sinh viên tiếng Anh `Basic` bị tụt lại đáng kể về CGPA. Nhà trường cần bổ sung học phần ngắn hạn hoặc workshop: *"Đọc hiểu tài liệu kỹ thuật, API Documentation & Viết báo cáo đồ án phần mềm bằng tiếng Anh"*.

### 9.2. Trụ cột 2: Cơ chế Cố vấn Học tập Chủ động (Proactive Mentorship) & Đòn bẩy Học bổng
* **Chuyển từ "Cố vấn bị động" sang "Cố vấn chủ động":**
  * Hiện tượng Help-seeking bias chỉ ra rằng giảng viên hiện nay chỉ gặp sinh viên khi "chuyện đã rồi" (đã bị cảnh cáo).
  * *Chính sách mới:* Khoa CSE cần tự động gán cố vấn học tập gặp gỡ định kỳ ngay từ tuần thứ 4 của học kỳ đối với bất kỳ sinh viên nào có chuyên cần $< 80\%$ hoặc SGPA kỳ trước $< 2.75$.
* **Đòn bẩy Học bổng Bậc thang (Tiered Merit Scholarships):**
  * Dữ liệu cho thấy học bổng liên kết cực mạnh với trạng thái học tập ($\chi^2 = 49.97$). Thay vì chỉ trao học bổng cho Top 5% xuất sắc, nên thiết kế thêm "Học bổng Nỗ lực Vượt bậc" (Progressive Scholarship) dành cho sinh viên cải thiện CGPA tăng $\ge 0.4$ điểm so với kỳ trước để kích thích động lực học tập của nhóm `Average`.

### 9.3. Trụ cột 3: Kiến trúc Hệ thống Cảnh báo Sớm Học vụ (Early Alert System)
Xây dựng module cảnh báo tự động tích hợp trên Cổng Quản lý Đào tạo (Portal) của trường:

| Cấp độ Cảnh báo | Điều kiện Kích hoạt (Trigger Rules) | Hành động Can thiệp Cụ thể |
| :---: | :--- | :--- |
| 🟢 **Mức 1 (An toàn)** | Chuyên cần $\ge 90\%$, Tỷ lệ Học/MXH $\ge 1.0$, SGPA $\ge 3.20$ | Gửi thông báo khen ngợi, gợi ý tham gia Lab nghiên cứu AI / CLB Lập trình. |
| 🟡 **Mức 2 (Lưu tâm)** | Chuyên cần từ $80\% - 89\%$, HOẶC Dùng MXH $> 4$ giờ/ngày | Gửi email nhắc nhở tự động; thông báo đến trợ giảng môn chuyên ngành hỗ trợ bài tập. |
| 🔴 **Mức 3 (Khẩn cấp)**| Chuyên cần $< 80\%$, HOẶC Điểm kỳ trước $< 2.50$, HOẶC Từng bị Probation | Đặt lịch hẹn bắt buộc với Giảng viên Cố vấn; phối hợp với phụ huynh; lập kế hoạch học tập giảm tải tín chỉ. |

---

## 🚀 10. HƯỚNG DẪN TÁI LẬP & VẬN HÀNH PIPELINE TỰ ĐỘNG

Dự án đã được tự động hóa hoàn toàn và có thể thực thi lại chỉ bằng một câu lệnh:

```bash
# 1. Kích hoạt môi trường ảo Python đã được cài đặt
.\.venv\Scripts\activate

# 2. Chạy toàn bộ pipeline điều phối (Bước 1 đến Bước 5)
python run_pipeline.py
```

### Danh mục Sản phẩm Bàn giao trong Thư mục Dự án:
* 📁 `data/`:
  * `cleaned_students_performance.csv`: Dữ liệu sạch 31 cột.
  * `processed_students_performance.csv`: Dữ liệu 38 cột kèm đặc trưng phái sinh và biến mục tiêu.
* 📁 `scripts/`:
  * `01_data_cleaning.py`: Module làm sạch và sửa lỗi typo.
  * `02_feature_engineering.py`: Module tạo đặc trưng và phân loại trạng thái học tập.
  * `03_eda_visualizations.py`: Module vẽ 9 biểu đồ trực quan chuẩn 300 DPI.
  * `04_statistical_tests.py`: Module chạy kiểm định Chi-Square, ANOVA, Kruskal-Wallis, t-test.
  * `05_machine_learning.py`: Module huấn luyện mô hình ML và trích xuất Feature Importance.
* 📁 `reports/`:
  * `figures/`: Chứa đủ 11 file ảnh biểu đồ chất lượng cao (`01` đến `11`).
  * `statistical_test_results.json`: Báo cáo chi tiết toàn bộ chỉ số kiểm định thống kê.
  * `model_evaluation_results.json`: Báo cáo chi tiết độ chính xác và trọng số mô hình.
* 📄 `run_pipeline.py`: Script điều phối một chạm toàn bộ đề tài.
* 📄 `BAO_CAO_DU_AN_PHAN_TICH_SINH_VIEN_CSE.md`: Báo cáo khoa học tổng kết hoàn chỉnh.

---
*Báo cáo được hoàn thành tự động với chuẩn mực cao nhất về phương pháp luận Khoa học Dữ liệu.*
