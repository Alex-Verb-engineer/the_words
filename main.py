input_file = open('input.txt', 'r', encoding='utf-8')
# input_string = input_file.readlines()
# Интерпретатор запоминает положение курсора считывания после этого действия

output_file = open('output.txt', 'w', encoding='utf-8')

for line in input_file:
    output_file.write(line[:-1] + ', ')

output_file.close()
input_file.close()
