#include <stdio.h>
#include <time.h>

int main() {
    time_t seconds = time(NULL);
    unsigned int seed = seconds ^ 0xDEADBEEF;
    unsigned int generated_number = seed * seed * seed * seed;

    printf("seconds: %llu\n", seconds);
    printf("seed: %llu\n", seed);
    printf("generated_number: %llu\n", generated_number);
    printf("generated_number as HEX: 0x%llx\n", generated_number);

    char new_name[50];
    new_name[0] = '/';
    int i = 1;
    while ( generated_number != 0 )
    {
        sprintf((char *)&new_name + i, "%02x", (unsigned __int8)generated_number);
        // printf("added to new_name: %20x\n", (unsigned __int8)generated_number);

        generated_number >>= 8;
        // printf("generated_number: %llx\n", generated_number);

        i += 2;   
    }

    new_name[i] = '\0';
    printf("new_name: %s", new_name);

    return 0;
}