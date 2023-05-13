#include <stdio.h>
#include <cstdlib>

int main(int argc, char *argv[]) {
    unsigned int seed = 2185163185; // Hardcoded value based on the output of the Python script. I know.
    unsigned int size_until_fmi = 852105; // Same as above.
    srand(seed);

    FILE *input_file = fopen("c19cf21d23c2a054462451047b202711", "r");
    FILE *output_file = fopen("decrypted_reversed", "w");

    if (input_file == NULL || output_file == NULL) {
        printf("Error: Unable to open file.\n");
        return 1;
    }
    fseek(input_file, 0, SEEK_END);
    unsigned int file_size = ftell(input_file);

    fseek(input_file, 0, SEEK_SET);
    char buf;
    for (int i = 0; i <= size_until_fmi; i++) {
        fread(&buf, 1, 1, input_file);
        unsigned int r = rand();
        buf -= r;
        fwrite(&buf, 1, 1, output_file);
    }
    fclose(output_file);

    char old_name[100];
    fseek(input_file, 13, SEEK_CUR); // Skip "fmi_re_course"
    unsigned file_name_length = file_size - size_until_fmi - 13;
    for (int i = 0; i < file_name_length; i ++) {
        fread(&buf, 1, 1, input_file);
        unsigned int r = rand();
        buf -= r;
        old_name[i] = buf;
    }
    old_name[file_name_length] = 0;
    fclose(input_file);

    printf("File processed successfully.\n");
    printf("Original file name: %s\n", old_name);

    return 0;
}
