// using code of cs50x tehran , mr.Aref Tavasoli & me ;
// love you cs50 and other person from Harvard university :) ;

// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *jadval[N];
int dictandaze = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int meghdar_hash = hash(word);
    node *n = jadval[meghdar_hash];
    while (n != 0)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    long jam = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        jam += tolower(word[i]);
    }
    return jam % N;
    // a way that I found in google :

//     #include <stdio.h>
//     #include <openssl/sha.h>
//     #include <string.h>

//     int main() {
//     char input[] = "Hello, World!";
//     unsigned char hash[SHA256_DIGEST_LENGTH];

//     SHA256(input, strlen(input), hash);

//     printf("Hash value: ");
//     for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
//         printf("%02x", hash[i]);
//     }
//     printf("\n");

//     return 0;
//    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_neshane = fopen(dictionary, "r");
    if (dictionary == NULL)
    {
        printf("can not open %s\n", dictionary);
        return false;
    }
    char next_word[LENGTH + 1];
    while (fscanf(dict_neshane, "%s", next_word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, next_word);
        int meghdar_hash = hash(next_word);
        n->next = jadval[meghdar_hash];
        jadval[meghdar_hash] = n;
        dictandaze++;
    }
    fclose(dict_neshane);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return dictandaze;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *n = jadval[i];
        while (n != NULL)
        {
            node *temp = n;
            n = n->next;
            free(temp);
        }
        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
