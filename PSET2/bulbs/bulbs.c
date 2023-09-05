#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string m = get_string("text: ");
    int n = strlen(m);
    for (int i = 0; i < n; i++)
    {
        int b[] = {0, 0, 0, 0, 0, 0, 0, 0};
        int d = m[i];
        int j = 0;
        while (d > 0)
        {
            b[j] = d % 2;
            d = d / 2;
            j++;
        }
        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            print_bulb(b[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
