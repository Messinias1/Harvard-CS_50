// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"
#include <strings.h>

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table

node *hashtable[N];

int wordcount;


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
    wordcount = 0;

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // TODO
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            unload();
            return false;
        }

        strcpy(new_node->word, word);
        int hashed = hash(word);
        if (hashtable[hashed] == NULL)
        {
            hashtable[hashed] = new_node;
            new_node->next = NULL;
        }
        else
        {
            new_node->next = hashtable[hashed];
            hashtable[hashed] = new_node;
        }
        wordcount++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wordcount;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    int hashindex = hash(word);
    if (hashtable[hashindex] == NULL)
    {
        return false;
    }
    else if (hashtable[hashindex] != NULL)
    {
        node *cursor = hashtable[hashindex];
        while (cursor!= NULL)
        {
            if (strcasecmp(cursor->word, word) == 0)
            {
                return true;
            }
            cursor = cursor->next;
        }
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];
        while(cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}