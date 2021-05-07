"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents

# print(open_and_read_file("our_text.txt"))



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    words.append(None)
    
    #list_of_values = []

    for i in range(len(words) - 2):

        key = (words[i], words[i + 1])

        value = words[i + 2]

        if key not in chains:
            chains[key] = []
        # chains[i] = (words[i], words[i + 1])
        #list_of_values.append(chains[words][i + 2])
        #(chains[words][i], chains[words][i + 1]) 
        # chains.get((words[i], words[i + 1]), words[i + 2])
        chains[key].append(value)
        
        
    return chains

# print(make_chains(open_and_read_file("our_text.txt")))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    random_key = choice(list(chains.keys()))
    words = [random_key[0], random_key[1]]
    random_value = choice(chains[random_key])

    # while key exists 
    # do this: take random_key[1] and random_value and make a new key
    # use that key to pick a new value, add to list, lather, rinse, repeat
    while random_value is not None:
        random_key = (random_key[1], random_value)
        words.append(random_value)
        random_value = choice(chains[random_key])

    return ' '.join(words)

input_path = sys.argv[1]
#'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# somehow I need to get random slices from the generated text 

# print(open_and_read_file(make_chains(make_text("green-eggs.txt"))))

import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Connected! Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # if "lorandroid" in message.content:
    if message.content.startswith("lorandroid"):
        await message.channel.send(make_text(chains)[:150])

client.run(os.environ["DISCORD_TOKEN"])

# bot-party channel ID 763526659764256798