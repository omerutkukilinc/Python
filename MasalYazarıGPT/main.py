import tkinter as tk
from tkinter import messagebox, scrolledtext
from masal import masal_yaz

pencere = tk.Tk()
pencere.title("Masal Yazarı GPT")

tk.Label(pencere, text="Masal Başlığı:").pack()
baslik_entry = tk.Entry(pencere, width=50)
baslik_entry.pack()

tk.Label(pencere, text="Ana Karakter:").pack()
karakter_entry = tk.Entry(pencere, width=50)
karakter_entry.pack()

tk.Label(pencere, text="Masal Türü (örn: macera, komedi):").pack()
tur_entry = tk.Entry(pencere, width=50)
tur_entry.pack()

tk.Button(pencere, text="Masalı Yaz!", command=lambda: masal_yaz(baslik_entry, karakter_entry, tur_entry, cikti_text)).pack(pady=10)

cikti_text = scrolledtext.ScrolledText(pencere, width=60, height=30)
cikti_text.pack()

pencere.mainloop()
