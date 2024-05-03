"""
Программа, переводящая вертикальную колонку слов
в горизонтальную через запятую
входной файл input.txt
выходной файл output.txt
Опционально - файл с использованными словами avoided.txt
"""

INPUT = 'input.txt'
OUTPUT = 'output.txt'
AVOIDED = 'avoided.txt'


def column_to_comma_string(input_file, output_file, avoided_file=None):
    if avoided_file:
        avoided = avoided_file.readlines()
    else:
        avoided = []
    avoided = set(avoided)

    words = input_file.readlines()
    words = set(words)

    words = words.difference(avoided)

    for word in words:
        output_file.write(word[:-1] + ', ')


if __name__ == '__main__':
    input_file = open(INPUT, 'r', encoding='utf-8')
    # input_string = input_file.readlines()
    # Интерпретатор запоминает положение курсора считывания после этого
    # действия
    avoided_file = None

    try:
        avoided_file = open(AVOIDED, 'r', encoding='utf-8')
    except FileNotFoundError:
        pass

    output_file = open(OUTPUT, 'w', encoding='utf-8')

    column_to_comma_string(input_file, output_file, avoided_file)

    output_file.close()
    input_file.close()

    if avoided_file:
        avoided_file.close()
