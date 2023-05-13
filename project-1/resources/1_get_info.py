import sys
import math

def get_seed(filename: str) -> int:
    n = len(filename)
    generated_number_str = ''
    for i in range(n-2, -1, -2):
        generated_number_str += filename[i:i+2]
    
    generated_number = int(generated_number_str, 16)
    seed = math.sqrt(math.sqrt(generated_number))
    assert seed.is_integer(), 'The filename is not valid. This file was not encrypted by this ransomware.'
    return int(seed)


def get_fmi_position(filename: str) -> int:
    with open(filename, 'r', encoding="cp437") as encrypted_file:
        file_contents = encrypted_file.read()
        print(file_contents)
        return file_contents.find('fmi_re_course')


def main():
    assert len(sys.argv) == 2, 'The name of the file should be given as argument.'
    filename = sys.argv[1]
    filename = filename.removeprefix('./').removeprefix('.\\')
    
    print('seed:', get_seed(filename))
    print('fmi position:', get_fmi_position(filename))


if __name__ == '__main__':
    main()