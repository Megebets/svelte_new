import os

def print_tree(path, indent='', exclude_dirs=['__pycache__', 'migrations', 'node_modules', 'venv', '.git']):
    """
    Функция для рекурсивного вывода древовидной структуры каталога.

    Args:
        path: Путь к каталогу.
        indent: Отступ для текущего уровня вложенности.
        exclude_dirs: Список каталогов, которые не будут выводиться.
    """

    # Проверяем существует ли путь
    if not os.path.exists(path):
        print(f"Указанный путь {path} не существует.")
        return

    for root, dirs, files in os.walk(path, followlinks=True):
        # Удаляем каталоги, которые нужно исключить из обхода
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # Выводим текущую директорию
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(indent + os.path.basename(root))  # Выводим имя каталога

        # Выводим файлы в текущей директории
        for f in files:
            print(indent + '    ' + f)  # Выводим имя файла с отступом


# Путь к вашему проекту (измените на ваш актуальный путь)
path = r'C:\Users\Sh\Desktop\svelte'

# Проверяем, что путь существует
if os.path.exists(path):
    print_tree(path)
else:
    print(f"Путь {path} не существует.")
