def custom_write(file_name, strings):
    
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    for i in strings:
        file.write(i + '\n')
        start_byte = file.tell()
        string_positions[(strings.index(i), start_byte)] = i
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)