"""
PIPELINE TỔNG ĐIỀU PHỐI (END-TO-END AUTOMATED PIPELINE)
Đề tài: Phân tích, trực quan hóa và rút ra ý nghĩa từ dữ liệu sinh viên CSE
"""
import sys
import time
import subprocess

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

steps = [
    ("Bước 1 & 2: Tiền xử lý & Làm sạch dữ liệu", "scripts/01_data_cleaning.py"),
    ("Bước 3: Kỹ thuật đặc trưng (Feature Engineering)", "scripts/02_feature_engineering.py"),
    ("Bước 4: EDA & Trực quan hóa dữ liệu (9 Biểu đồ 300DPI)", "scripts/03_eda_visualizations.py"),
    ("Bước 5.1: Kiểm định Thống kê Giả thuyết (Chi-Square, ANOVA, t-test)", "scripts/04_statistical_tests.py"),
    ("Bước 5.2: Huấn luyện Mô hình Machine Learning & Feature Importance", "scripts/05_machine_learning.py")
]

def main():
    print("=" * 70)
    print("  HỆ THỐNG THỰC THI TOÀN BỘ QUY TRÌNH KHOA HỌC DỮ LIỆU SINH VIÊN CSE")
    print("=" * 70)
    start_total = time.time()

    py_exe = sys.executable

    for idx, (title, script_path) in enumerate(steps, 1):
        print(f"\n[{idx}/{len(steps)}] BẮT ĐẦU: {title}")
        print(f"       File: {script_path}")
        start_step = time.time()
        
        result = subprocess.run([py_exe, script_path], capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            elapsed = time.time() - start_step
            print(f"       >>> HOÀN TẤT trong {elapsed:.2f} giây.")
            # Print brief stdout preview
            lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
            for l in lines[-3:]:
                print(f"           | {l}")
        else:
            print(f"       [!] LỖI THỰC THI ở {script_path}:")
            print(result.stderr)
            sys.exit(1)

    total_time = time.time() - start_total
    print("\n" + "=" * 70)
    print(f"  TẤT CẢ CÁC BƯỚC ĐÃ ĐƯỢC THỰC THI THÀNH CÔNG! (Tổng thời gian: {total_time:.2f}s)")
    print("  * Dữ liệu đã xử lý: data/processed_students_performance.csv")
    print("  * Toàn bộ biểu đồ  : reports/figures/ (11 biểu đồ 300 DPI)")
    print("  * Báo cáo Thống kê : reports/statistical_test_results.json")
    print("  * Báo cáo Học máy  : reports/model_evaluation_results.json")
    print("=" * 70)

if __name__ == "__main__":
    main()
