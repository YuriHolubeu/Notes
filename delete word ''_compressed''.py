import os

def rename_compressed_pdfs():
    # Получаем текущий рабочий каталог
    current_dir = os.getcwd()
    
    # Обходим все папки и файлы внутри текущего каталога
    for root, _, files in os.walk(current_dir):
        for file in files:
            # Проверяем, заканчивается ли файл на "_compressed.pdf"
            if file.endswith("_compressed.pdf"): 
                # Определяем старый и новый путь файла
                old_path = os.path.join(root, file)
                new_name = file.replace("_compressed", "")
                new_path = os.path.join(root, new_name)
                
                # Переименовываем файл
                os.rename(old_path, new_path)
                print(f"Переименован: {old_path} -> {new_path}")

if __name__ == "__main__":
    rename_compressed_pdfs()
