import os


def merge_files(input_folder, output_file, file_names):
    """
    input_folder: Путь к папке с исходными файлами.
    output_file: Имя результирующего файла.
    file_names: Список имен файлов для объединения.
    """
    files_with_line_counts = []

    # Получаем количество строк в каждом файле
    for file_name in file_names:
        file_path = os.path.join(input_folder, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                line_count = len(lines)
                files_with_line_counts.append((file_name, line_count, lines))
        except FileNotFoundError:
            print(f"Файл {file_name} не найден в папке {input_folder}. Пропускаем.")
        except Exception as e:
            print(f"Ошибка при обработке файла {file_name}: {e}. Пропускаем.")

    # Сортируем файлы по количеству строк
    files_sorted = sorted(files_with_line_counts, key=lambda x: x[1])

    # Записываем в результирующий файл
    with open(os.path.join(input_folder, output_file), 'w', encoding='utf-8') as out_f:
        for file_info in files_sorted:
            file_name, line_count, lines = file_info
            out_f.write(f"{file_name}\n")
            out_f.write(f"{line_count}\n")
            for line in lines:
                out_f.write(line)
            out_f.write("\n")  # Добавляем пустую строку между файлами для разделения

    print(f"Файлы успешно объединены в {output_file}.")


# Пример использования:
if __name__ == "__main__":
    input_folder = 'files'  # Папка с исходными файлами
    output_file = 'result.txt'  # Имя результирующего файла
    file_names = ['1.txt', '2.txt', '3.txt']  # Список имен файлов для объединения

    merge_files(input_folder, output_file, file_names)