import os
from PIL import Image, ImageEnhance, ImageOps

# Giriş ve çıkış klasörleri
input_folder = "yeşil"         # Orijinal görsellerin bulunduğu klasör
output_folder = input_folder + "_son"       # Sonuçların kaydedileceği klasör
os.makedirs(output_folder, exist_ok=True)

# Geçerli uzantılar ve hedef boyut
valid_exts = (".jpg", ".jpeg", ".png")
target_size = (128, 128)
counter = 1

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_exts):
        try:
            img_path = os.path.join(input_folder, filename)
            img_original = Image.open(img_path).convert("RGB")

            # Orijinal görselin işlenmesi (dolgu + boyutlandırma)
            img_padded = ImageOps.pad(img_original, target_size, color=(255, 255, 255))
            new_filename_original = f"{input_folder}_{counter}.jpg"
            img_padded.save(os.path.join(output_folder, new_filename_original))
            print(f"{new_filename_original} kaydedildi.")
            counter += 1

            # Parlaklığı azaltılmış görselin işlenmesi
            enhancer = ImageEnhance.Brightness(img_original)
            img_darker = enhancer.enhance(0.7)
            img_darker_padded = ImageOps.pad(img_darker, target_size, color=(255, 255, 255))
            new_filename_darker = f"{input_folder}_{counter}.jpg"
            img_darker_padded.save(os.path.join(output_folder, new_filename_darker))
            print(f"{new_filename_darker} kaydedildi.")
            counter += 1

        except Exception as e:
            print(f"Hata ({filename}): {e}")
            
