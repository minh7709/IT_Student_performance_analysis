"""
PIPELINE TỔNG ĐIỀU PHỐI (END-TO-END AUTOMATED PIPELINE)
Đề tài: Phân tích, trực quan hóa và rút ra ý nghĩa từ dữ liệu sinh viên CSE
"""
import sys
import json
import time
import subprocess

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

steps = [
    ("Bước 1 & 2: Tiền xử lý & Làm sạch dữ liệu", "scripts/01_data_cleaning.py"),
    ("Bước 3: Kỹ thuật đặc trưng (Feature Engineering)", "scripts/02_feature_engineering.py"),
    ("Bước 4: EDA & Trực quan hóa dữ liệu (11 Biểu đồ 300DPI)", "scripts/03_eda_visualizations.py"),
    ("Bước 5.1: Kiểm định Thống kê Giả thuyết (Shapiro-Wilk, Chi-Square, ANOVA, t-test)", "scripts/04_statistical_tests.py"),
    ("Bước 5.2: Huấn luyện Mô hình Machine Learning & Feature Importance", "scripts/05_machine_learning.py")
]

def print_ml_summary():
    """Đọc JSON kết quả ML và in bảng tóm tắt hiệu năng."""
    try:
        with open("reports/model_evaluation_results.json", encoding="utf-8") as f:
            ml = json.load(f)
        print("\n  📊 MODEL PERFORMANCE SUMMARY (5-Fold Stratified CV):")
        print(f"  {'Model':22s} | {'Accuracy':>8s} | {'F1-Macro':>8s} | {'F1-Weighted':>11s}")
        print("  " + "-" * 60)
        for model, scores in ml["cross_validation_results"].items():
            marker = " ◄ BEST" if model == ml.get("best_model_selected") else ""
            print(f"  {model:22s} | {scores['accuracy_mean']:>7.1%} | {scores['f1_macro_mean']:>8.4f} | {scores['f1_weighted_mean']:>11.4f}{marker}")
        best = ml.get("best_model_selected", "N/A")
        test_acc = ml["test_set_evaluation"]["accuracy"]
        test_f1 = ml["test_set_evaluation"]["f1_macro"]
        print(f"\n  ✅ Best model: [{best}] | Test Accuracy: {test_acc:.1%} | Test F1-Macro: {test_f1:.4f}")
    except FileNotFoundError:
        pass

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
    print("  * Dữ liệu đã xử lý : data/processed_students_performance.csv")
    print("  * Biểu đồ EDA       : reports/figures/ (11 biểu đồ 300 DPI)")
    print("  * Thống kê mô tả    : reports/descriptive_statistics.txt")
    print("  * Báo cáo Thống kê  : reports/statistical_test_results.json")
    print("  * Báo cáo Học máy   : reports/model_evaluation_results.json")
    print_ml_summary()
    print("=" * 70)

if __name__ == "__main__":
    main()
