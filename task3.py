import os
from pathlib import Path

def get_file(file_path):
    file_name = os.path.basename(file_path)
    result = ''
    with open(file_path, encoding='utf-8') as file:
        file_content = file.read()
        lines_count = file_content.count('\n') + 1
        res = f'{file_name}\n{lines_count}\n{file_content}\n'
    return res

def merge_file(dir, result_file):
    files = Path(dir).glob('*.txt')
    files_content = []
    for file in files:
        files_content.append(get_file(file))
    files_content.sort(key=lambda item: item.count('\n'))

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write("".join(files_content))

merge_file('./files', './result.txt')