"""
🧹 Data Cleaning Tool - Abu Azab
© 2024 Abdelrahman Adel Alazab. All rights reserved.

Developer: Abdelrahman Adel Alazab
📧 Email: abdelrahmanalazab4@gmail.com
📞 Phone: 0573532943
📍 Location: Riyadh, Saudi Arabia

🎯 "Building tomorrow's solutions with today's technology"

---
🧹 برنامج تنظيف البيانات - أبو عزب
© 2024 Abdelrahman Adel Alazab. جميع الحقوق محفوظة.

مطور بواسطة: Abdelrahman Adel Alazab
📧 البريد الإلكتروني: abdelrahmanalazab4@gmail.com
📞 الهاتف: 0573532943
📍 الموقع: الرياض، المملكة العربية السعودية

🎯 "بناء حلول الغد بتقنية اليوم"
"""

import pandas as pd
import csv
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def detect_delimiter(file_path, sample_size=2048):
    """اكتشاف الفاصل تلقائياً"""
    with open(file_path, "r", encoding="utf-8") as file:
        sample = file.read(sample_size)
        sniffer = csv.Sniffer()
        try:
            dialect = sniffer.sniff(sample, delimiters=[",", ";", "\t", " "])
            return dialect.delimiter
        except csv.Error:
            return ","  # افتراضي: فاصلة

def clean_dataframe(df):
    """تنظيف البيانات + تحويل الأرقام والتواريخ"""
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore", dayfirst=True, infer_datetime_format=True)
            except Exception:
                pass

    df.replace(["", " ", "NULL", "NaN", "nan", "N/A", "n/a"], np.nan, inplace=True)
    df.dropna(how="all", inplace=True)

    return df

def process_file():
    # اختيار ملف TXT
    txt_file = filedialog.askopenfilename(
        title="اختر ملف TXT",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not txt_file:
        return

    delimiter = detect_delimiter(txt_file)

    try:
        df = pd.read_csv(
            txt_file,
            delimiter=delimiter,
            engine="python",
            skip_blank_lines=True,
            on_bad_lines="skip"
        )
    except Exception as e:
        messagebox.showerror("خطأ", f"تعذر قراءة الملف: {e}")
        return

    if df.columns.tolist()[0].startswith("Unnamed"):
        df.columns = [f"عمود{i+1}" for i in range(len(df.columns))]

    df = clean_dataframe(df)

    # تجهيز أسماء الملفات (بنفس اسم الملف الأصلي)
    base_name = os.path.splitext(os.path.basename(txt_file))[0]
    excel_file = os.path.join(os.path.dirname(txt_file), f"{base_name}_clean.xlsx")
    csv_file = os.path.join(os.path.dirname(txt_file), f"{base_name}_clean.csv")

    # حفظ الملفات
    df.to_excel(excel_file, index=False, engine="openpyxl")
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")

    messagebox.showinfo("نجاح", f"📂 تم حفظ الملفات:\n{excel_file}\n{csv_file}")

# ====== واجهة ترحيبية ======
def main_ui():
    root = tk.Tk()
    root.title("🧹 برنامج تنظيف البيانات - أبو عزب")
    root.geometry("400x200")
    root.resizable(False, False)

    # رسالة ترحيبية
    label = tk.Label(root, text="مرحباً بك في برنامج تنظيف البيانات 👋", font=("Arial", 14))
    label.pack(pady=30)

    # زر اختيار الملف
    btn = tk.Button(root, text="📂 اختر ملف TXT للمعالجة", font=("Arial", 12), bg="#4CAF50", fg="white",
                    command=process_file)
    btn.pack(pady=20)

    root.mainloop()

# تشغيل الواجهة
if __name__ == "__main__":
    main_ui()
