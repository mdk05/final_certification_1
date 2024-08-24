import os
import sys
from datetime import datetime

path = "/"  # Используется корневой каталог, если переменная закомментирована

def get_top_files(directory, top_n=10):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath) / 1024  # Размер в Кб
                files.append((filename, size))
            except OSError:
                continue
    
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:top_n]

def main(name):
    print(f"Привет, {name}! Текущее время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    total_files = sum([len(files) for r, d, files in os.walk(path)])
    print(f"Общее количество файлов в директории '{path}': {total_files}")
    
    # Топ-10 файлов по размеру
    top_files = get_top_files(path)
    print("Топ-10 файлов по размеру:")
    for filename, size in top_files:
        print(f"{filename}: {size:.2f} Кб")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Пользователь"
    main(name)
