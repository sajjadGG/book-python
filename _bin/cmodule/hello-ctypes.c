#include <stdio.h>
#include <time.h>

void say_hello(char* name) {
	printf("Hello %s!\n", name);
}

void what_time() {
	time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    char s[64];
    strftime(s, sizeof(s), "%c", tm);
    printf("%s\n", s);
}

