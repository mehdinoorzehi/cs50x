#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int redorginal, greenorginal, blueorginal;
    float grayout;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            redorginal = image[i][j].rgbtRed;
            greenorginal = image[i][j].rgbtGreen;
            blueorginal = image[i][j].rgbtBlue;

            grayout = round((redorginal + greenorginal + blueorginal) / 3.0);

            image[i][j].rgbtRed = grayout;
            image[i][j].rgbtGreen = grayout;
            image[i][j].rgbtBlue = grayout;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen, originalBlue;
    int sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;

            sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);

            sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);

            sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE rplace[width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            rplace[j] = image[i][j];
        }
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = rplace[width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = rplace[width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = rplace[width - j - 1].rgbtBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int m = 0; m < height; m++)
    {
        for (int n = 0; n < width; n++)
        {
            copy[m][n] = image[m][n];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            float redplus = 0;
            float greenplus = 0;
            float blueplus = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (!(i + k < 0 || i + k >= height || j + l < 0 || j + l >= width))
                    {
                        redplus += copy[i + k][j + l].rgbtRed;
                        greenplus += copy[i + k][j + l].rgbtGreen;
                        blueplus += copy[i + k][j + l].rgbtBlue;
                        count++;
                    }
                    else
                    {
                        continue;
                    }
                }
            }

            image[i][j].rgbtRed = (int) round(redplus / count);
            image[i][j].rgbtGreen = (int) round(greenplus / count);
            image[i][j].rgbtBlue = (int) round(blueplus / count);
        }
    }
}
