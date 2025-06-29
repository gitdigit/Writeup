// fichier : example.c

#include <stdio.h>



int handler0(void) { puts("cas 0"); return 0; }

int handler1(void) { puts("cas 1"); return 1; }

int handler2(void) { puts("cas 2"); return 2; }

int handler3(void) { puts("cas 3"); return 3; }



int main(int argc, char** argv)

{

    int code = argc % 5;  // code entre 0 et 4

    switch (code) {

    case 0:

        return handler0();

    case 1:

        return handler1();

    case 2:

        return handler2();

    case 3:

        return handler3();

    default:

        puts("autre cas");

        return -1;

    }

}

