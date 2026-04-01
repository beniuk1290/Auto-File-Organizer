import os
import time
import shutil
from datetime import datetime

WATCH_FOLDER = os.path.expanduser("~/Downloads")

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
}

def get_category(file):
    for category, exts in EXTENSIONS.items():
        if any(file.lower().endswith(ext) for ext in exts):
            return category
    return "Other"

def organize():
    for file in os.listdir(WATCH_FOLDER):
        path = os.path.join(WATCH_FOLDER, file)

        if os.path.isfile(path):
            category = get_category(file)
            target_dir = os.path.join(WATCH_FOLDER, category)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            new_name = f"{timestamp}_{file}"
            new_path = os.path.join(target_dir, new_name)

            try:
                shutil.move(path, new_path)
                print(f"[OK] {file} → {category}")
            except Exception as e:
                print(f"[ERR] {file}: {e}")

if __name__ == "__main__":
    print("Monitoring folderu Downloads...")
    while True:
        organize()
        time.sleep(5)
