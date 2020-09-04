def get_file_content(path):
    return open(path, 'rb')


def append_file_to_another(f1, f2, new_file):
    with open(new_file, 'wb') as f:
        f.write(f1.read())
        f.write(f2.read())


if __name__ == '__main__':
    fi1 = get_file_content('1.exe')
    fi2 = get_file_content('2.exe')
    append_file_to_another(fi1, fi2, '3.exe')
    fi1.close()
    fi2.close()
