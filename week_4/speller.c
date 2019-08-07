// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // TODO tttttttttttttttttttttttttttttttttttttttttttttt
        node *newWord = malloc(sizeof(node));
        if (newWord == NULL)
        {
            unload();
            return false;
        }
        else
        {
            strcpy(newWord->word, word);

            newWord->next = hash;
            hash = newWord;
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO tttttttttttttttttttttttttttttttttttttttttttttttttttttt
    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO ttttttttttttttttttttttttttttttttttttttttttttttttttttttt
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO ttttttttttttttttttttttttttttttttttttttttttttttttttttttt
    return false;
}
