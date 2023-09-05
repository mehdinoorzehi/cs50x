#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("text: ");

    float length = 0;
    float word = 0;
    int n = strlen(text);
    float Sentence = 0;
    for (int i = 0; i < n; i++)
    {
        if (isalpha(text[i]) != 0)
        {
            length++;
        }
        if (text[i] == 32)
        {
            word++;
        }
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            Sentence++;
        }

        // if ((text[i] >= '97' && text[i] <= '122') || (text[i] >= '65' && text[i] <= '90'))
        // {
        //     l++;
        // }
    }

    float L = 100 * (length / word);
    float S = 100 * (Sentence / word);

    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}