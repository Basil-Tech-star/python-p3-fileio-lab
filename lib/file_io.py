def write_file(file_name, file_content):
    if not str(file_name).endswith('txt'):
        file_name = file_name.with_suffix('.txt')
    with open (file_name , 'w', encoding = 'utf-8') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    if not str(file_name).endswith ('txt'):
        file_name = file_name.with_suffix('.txt')
    with open(file_name, 'a', encoding= 'utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    if not str(file_name).endswith('.txt'):
        file_name = file_name.with_suffix('.txt')
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
