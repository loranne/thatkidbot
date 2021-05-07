"""Generate Markov text from text files."""

import os
import discord

client = discord.Client()

original_responses = {
    ("quantum", "metaphysic", "formalism", "dialectic", "question", "game theory") : "So this is less of a question and more of a comment, but I think we’re not really considering all the relative outcomes in relationship to their eventual logical conclusions. There was this great article posted on Reason a few months ago, you might’ve seen it pop up on Reddit yesterday, examining how dialectical readings of history don’t take into account modern quantum flux research on both uncertainty and relative states. Now, I obviously don’t want to accuse one of the central figures of Western thought of being pure formalism as obviously his writings have, if nothing else, sparked ideas in so many other brilliant men. But looking at this work from the quantum and dare I say even metaphysical lense, though I know metaphysics aren’t really en vogue these days, we see that there’s isn’t really a there there beneath a certain shallow or even sophomoric understanding of the human condition. Without diverting too far into game theory, it’s fairly clear, to me anyway, that the observations here don’t really answer either the authors stated intent, which is still unclear even with the addition of their second introduction, or significantly add to the discourse in and of itself. Quantum theory as well as even the most rudimentary quantitative analysis easily shows his understanding only appears to theorize about how man acts but doesn’t take into account how men act, if you understand the difference. Quantum theory shows how the more phenomenological elements are almost entirely ahistorical, which as Strauss pointed out in his dissection of Xenophon, renders most of the remaining text epistemologically useless and his critiques even when still valid, tipid enough to not actually address the issues at hand. Furthermore, if we instead use the neologisms present in the later writings of Foucoult as our starting off point, it's almost immediately obvious in my opinion that the overall work presents merely a simulacrum and therefore misses completely the true answers."
}

# remember that iterating through dict gets you keys
# this is generating pointers to original dict, not actually new data
responses = {}
for tuple_key in original_responses.keys():
    value = original_responses[tuple_key]
    for key in tuple_key:
        responses[key] = value


@client.event
async def on_ready():
    print(f"Connected! Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # if "lorandroid" in message.content:
    success = False

    for key in responses:
        if key in message.content.lower():
            response = responses[key]
            if len(response) >= 2000:
                response = response[:1996] + "..."
            await message.channel.send(response)
            success = True

    if not success:
        await message.channel.send("Who died and left Aristotle in charge of ethics?")

client.run(os.environ["DISCORD_TOKEN"])