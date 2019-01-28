#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    int quarter;
    int dime;
    int nickel;
    int penny;
    float  changeIn;
    int changeOut = 0;

    do{
      changeIn = get_float("Change owed: ");
    }
    while (changeIn < 0);

    int cents = round(changeIn * 100);
    for (quarter = 1; cents >= 25; quarter++){
        cents -= 25;
        changeOut += 1;
    }

    for (dime = 1; cents >= 10; dime++){
        cents -= 10;
        changeOut += 1;
    }

    for (nickel = 1; cents >= 5; nickel++){
        cents -= 5;
        changeOut += 1;
    }

    for (penny = 1; cents >= 1; penny++){
        cents -= 1;
        changeOut += 1;
    }

    printf("%i\n", changeOut);


}