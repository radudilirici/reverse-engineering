import sys


def main():
    assert len(sys.argv) == 2, 'The name of the file should be given as argument.'
    filename = sys.argv[1]
    filename = filename.removeprefix('./').removeprefix('.\\')
    new_filename = filename.removesuffix('_reversed')

    with open(filename, 'r', encoding='cp437') as reversed_file:
        reversed_file_contens = reversed_file.read()
        new_file_contents = reversed_file_contens[::-1]

        with open(new_filename, 'w', encoding='cp437') as fixed_file:
            fixed_file.write(new_file_contents)
    
    


if __name__ == '__main__':
    main()