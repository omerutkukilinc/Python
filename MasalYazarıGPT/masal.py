import openai
from tkinter import messagebox
import tkinter as tk
from config import API_KEY

# API yapılandırması
client = openai.OpenAI(api_key=API_KEY)  # ← Kendi API anahtarını buraya yaz

def masal_yaz(baslik_entry, karakter_entry, tur_entry, cikti_text):
    baslik = baslik_entry.get()
    karakter = karakter_entry.get()
    tur = tur_entry.get()

    if not baslik or not karakter or not tur:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    prompt = f"Bir {tur} masalı yaz. Başlığı: '{baslik}', Ana karakter: '{karakter}'. 10-15 cümle uzunluğunda olsun, çocuklara uygun ve eğlenceli olsun."

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[ 
                {"role": "system", "content": "Sen yaratıcı bir masal anlatıcısın."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.9
        )
        masal = response.choices[0].message.content
        cikti_text.delete(1.0, tk.END)
        cikti_text.insert(tk.END, masal)

    except Exception as e:
        messagebox.showerror("Hata", f"Masal alınırken hata oluştu:\n{str(e)}")
