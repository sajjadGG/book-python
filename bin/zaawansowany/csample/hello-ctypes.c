#include <stdio.h>

void ehlo() {
	printf("Ehlo World");
}

void greeting(char *name) {
	printf("Ehlo %s!\n", name);
}

void number(int num) {
	printf("My number %d\n", num);
}

int myint(int num) {
	return num;
}

