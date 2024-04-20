"""
Программа, переводящая вертикальную колонку слов
в горизонтальную через запятую
входной файл input.txt
выходной файл output.txt
"""

INPUT = 'input.txt'
OUTPUT = 'output.txt'
AVOIDED = 'avoided.txt'


def column_to_comma_string(input_file, output_file, avoided_file=None):
    avoided = avoided_file.readlines()
    for line in input_file:
        if line not in avoided:
            output_file.write(line[:-1] + ', ')


if __name__ == '__main__':
    input_file = open(INPUT, 'r', encoding='utf-8')
    # input_string = input_file.readlines()
    # Интерпретатор запоминает положение курсора считывания после этого
    # действия

    avoided_file = open(AVOIDED, 'r', encoding='utf-8')

    output_file = open(OUTPUT, 'w', encoding='utf-8')

    column_to_comma_string(input_file, output_file, avoided_file)

    output_file.close()
    input_file.close()
    avoided_file.close()
