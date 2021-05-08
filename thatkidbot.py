"""Generate Markov text from text files."""

import os
import discord

client = discord.Client()

original_responses = {
    ("quantum", "metaphysic", "formalism", "dialectic", "question", "game theory") : "So this is less of a question and more of a comment, but I think we’re not really considering all the relative outcomes in relationship to their eventual logical conclusions. There was this great article posted on Reason a few months ago, you might’ve seen it pop up on Reddit yesterday, examining how dialectical readings of history don’t take into account modern quantum flux research on both uncertainty and relative states. Now, I obviously don’t want to accuse one of the central figures of Western thought of being pure formalism as obviously his writings have, if nothing else, sparked ideas in so many other brilliant men. But looking at this work from the quantum and dare I say even metaphysical lense, though I know metaphysics aren’t really en vogue these days, we see that there’s isn’t really a there there beneath a certain shallow or even sophomoric understanding of the human condition. Without diverting too far into game theory, it’s fairly clear, to me anyway, that the observations here don’t really answer either the authors stated intent, which is still unclear even with the addition of their second introduction, or significantly add to the discourse in and of itself. Quantum theory as well as even the most rudimentary quantitative analysis easily shows his understanding only appears to theorize about how man acts but doesn’t take into account how men act, if you understand the difference. Quantum theory shows how the more phenomenological elements are almost entirely ahistorical, which as Strauss pointed out in his dissection of Xenophon, renders most of the remaining text epistemologically useless and his critiques even when still valid, tipid enough to not actually address the issues at hand. Furthermore, if we instead use the neologisms present in the later writings of Foucoult as our starting off point, it's almost immediately obvious in my opinion that the overall work presents merely a simulacrum and therefore misses completely the true answers.",
    ("bother", "hate scav", "like scav", "how do you feel about scav", "think about scav") : "SCAV bothers me. I'm fine with nerds having fun in an overindulgent nerdfest. What really bothers me is the amount of importance this university puts on such a meaningless endeavor. People pretend like this is some celebration of creativity and intellectual originality. No. Wake up. You are not doing anything more significant than those weird geeks with Japanese fetishes who show up at anime conventions in droves having paid hundreds of dollars to create the most accurate Chun Li costume. When you are at a rich private school that gentrified an entire community of low-income African Americans and eradicated an entire culture of jazz and arts under the name of urban renewal, when that school is currently celebrating a swanky new art center that purports to engage a variety of cultures while cutting its trauma program so that all the gunshot victims in the South Side die on the ambulance ride to Northwestern, you have an obligation to do something meaningful and relevant. UChicago not only is an Ivory Tower and a sheltered and privileged bubble; it celebrates being one. There is a reason this school has so many Nobel laureates and yet very little social relevance. You want to do something creative? While I was at Harvard I saw student-produced theater that had incredible depth, social relevance and insight, and thoughtful creativity. Your student performances at Logan fall far short of that standard. Start there. Instead of bashing Harvard students for not being intellectual enough, why don't you realize that you need some proper training from real performing artists, people who understand humanity with more breadth and nuance? You want to do something intellectual? Why not start some conversations about our real world, instead of indulging yourselves in weird abstract geekery that has zero social impact? You bash Harvard for having grade inflation, and you think your Core is oh-so-profound because everyone has to read works by Durkheim, but the average quality of talks, panels, and classroom discussions I've seen here is far lower than that at Harvard, intellectually as well as in social relevance. The real world doesn't exist in an abstraction. The real world is complicated and doesn't quite fit neatly into intellectual arguments, broad or specific. Producing t-shirts that ask 'That's all well and good in practice, but how does it work in theory?' is not helpful. So I guess the real reason SCAV bothers me so much is that it's emblematic of the whole self-indulgent, self-congratulating University of Chicago culture that is completely unaware of its privilege and so detached from reality. You have been given such blessings and resources that many students around the world can only dream of having. There are so many talented teenagers I have met working with under-resourced school districts that would probably look at your scavenger hunt and see the same thing we see when we look at Wall St -- an immense waste of talent and money.",
    ("tell me more", "more") : "Do your own homework."
}

# remember that iterating through dict gets you keys
# this is generating pointers to original dict, not actually new data
responses = {}
for tuple_key in original_responses.keys():
    value = original_responses[tuple_key]
    for key in tuple_key:
        responses[key] = value

bot_name = "thatscavkid"

@client.event
async def on_ready():
    print(f"Connected! Logged in as {client.user}")

@client.event
async def on_message(message):

    
    if message.author == client.user:
        return
    
    # if "lorandroid" in message.content:
    success = False

    if client.user.mentioned_in(message):
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