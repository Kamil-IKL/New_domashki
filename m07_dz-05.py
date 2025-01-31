import os
import time

print('Текущая директория:', os.getcwd())

# указываю в переменной "directory" асболютный путь к папке
directory = r'C:\Users\Компьютер\Documents\DOMASHKA\MOD_06'

# проверяем сщуствует или нет такая папка directory
if os.path.exists(directory):  # проверяет путь к directory
    os.chdir(directory)  # изменяем рабочую директорию, т.е. входим в папку directory
else:
    os.mkdir(directory)  # создаем папку directory
    os.chdir(directory)  # изменяем рабочую директорию, т.е. входим в папку directory

print('\nПуть к папке, указанной в переменной:', os.getcwd())
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # полный путь к файлу
        filetime = os.path.getmtime(filepath)  # время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # перевожу в формат ДД.ММ.ГГГГ
        filesize = os.path.getsize(filepath)  # определяю размер файла
        parent_dir = os.path.dirname(filepath)  # определяю в какой папке находится файл
        print(f'\n {'*' * 50}')
        print(f'Обнаружен файл: {file} \nПуть: {filepath} \nРазмер: {filesize} '
              f'байт. Время изменения: {formatted_time} \nРодительская директория: {parent_dir}')
        print(f'\n {'*' * 50}')
