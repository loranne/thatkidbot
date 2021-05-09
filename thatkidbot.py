"""Generate Markov text from text files."""

import os
import discord

client = discord.Client()

original_responses = {
    ("math", "logic", "computer", "brain", "intelligence", "AI", "information"): "Ugh, if any of you had read Gödel, Escher, Bach this conversation would never have happened. There is no algorithm for truth, so computers will never be as smart as humans, because we can eventually solve any problem. There’s just no way for bits and circuits to emulate the hypercomplex, multilayered nature of cognition. The idea of programming a computer with knowledge is nonsense as well; brains start out fluid and develop form and structure and encode information in the relationship between many different structures in the brain. Although, even calling it “information” is a misnomer, since that’s defined by bits instead of the complicated structural relationships that really determine what our brain does."
    ("Engels", "Hegel", "Schopenhauer", "Comte", "Kierkegaard", "Nietzsche", "Husserl", "Heidegger", "Wittgenstein", "Sarte", "Bordieu", "Derrida", "Habermas", "Beauvoir", "Weil", "Nussbaum", "Arendt"): "I just found this work derivative of the intersection of Marx, Durkheim, Foucault, and Rawls. If I’ve read them, why should I have to bother with this obscurantist nonsense?"
    ("economics", "John Stuart Mill", "rational", "john stuart mill"): "John Stuart Mill is just wrong. Homo economicus is a lie. Humans aren’t rational actors! They just do whatever makes them feel good, and that changes from person to person. Humans do irrational things all the time, like both stealing and not stealing! We’ve all got this tiny voice in our head telling us to do things, and not do other things, and sure the most rational choice is to think about what that voice says and what truly brings us happiness, and change that voice. But most people don’t even bother to do that. They stick with their traditions, morals, beliefs, of their upbringing. If Mill was even close to the truth, we’d see people abandoning their cultures for better ones, and that’s just not happening. Why would I need to bother with Mill then?"
    ("Hobbes", "Nasty", "Brutish", "Short", "Locke", "Rousseau"): "Locke, Hobbes, Rousseau, what does it possibly matter. People will do whatever they want. You can’t change how people think, and there’s no point in doing so. There’s no good form of government, just however rich people choose to try to keep poor people down. It’s not like knowing any of this is really going to help when civilization collapses due to climate change anyway. We should just be putting the biggest and strongest in charge, since that’s what will happen anyway, and they can use their power to keep everyone else in line. And since, honestly, that won’t be any of us, what’s the point?"
    ("data", "statistics", "evidence"): "Not to take us in too far of a different direction, but that reminds me of my statistics class. And what I’m bothered by here is how we can really know anything? Marx, Smith, Durkheim, Freud, they’re all making these huge claims about how the world works, but where’s their evidence? Where’s their data? It seems to me that they’re engaged in a form of something called p-hacking, where they’re just trying to throw arguments at the wall and see what sticks. They’re looking for nonsense that people seem to believe in already, doing nothing but confirming their own biases, because all of their arguments are just without data. And given that I prefer to live in the real world, with real information and real conclusions, I just don’t know why I should care about any of this."
    ("Foucault", "punishment", "grades"): "Foucault would tell you that we shouldn’t even be getting grades for this class. What are grades but a kind of punishment for students, designed to standardize their thinking and eliminate opposition to ruling hegemonic forms of knowledge?"
    ("Have", "stop", "what", "modern", "adorno", "jazz", "argument", "Adorno"): "It seems to me that you like my arguments like how Adorno liked jazz. He hated it, because it was all improvisation imprisoned within an overall structure. And you just don’t like how I think about things because I”m not part of your structures. But that doesn’t make my thoughts any worse, or any better, or any less real. I’m just saying, as someone outside of your frame of reference, none of these ideas are coherent and I wish we could talk about something more interesting. Like Nietzsche."
    ("Socrates", "Socratic", "Plato", "Aristotle", "Greece", "Academy"): "Something really bugs me about Socrates. He just, like, starts talking to people, and they can’t seem to walk away from him? He just monopolizes everyone’s time and doesn’t seem to have any sense of what other people want. It’s frankly just rude, you know?? Like, have some basic courtesy, man. Stop taking up time. On the other hand, though, like, it was totally over the top of the Athenians to just cancel him like that. Totally inappropriate reaction to a minor issue. Like when you talked to me a couple classes ago, Professor, about people wanting me not to talk so much? It’s just cancel culture run amok! Have a sense of perspective, people!"
    ("onions", "belts", "baseball", "dickety", "zeppelins", "washtubs", "Kaiser", "turkey"): "We can’t rant in SOSC classes like we used to—but we have our ways. One trick is to tell them stories that don’t go anywhere like the time I caught the ferry over to Shelbyville. I needed a new heel for my shoe, so I decided to go to Morganville which is what they called Shelbyville in those days. So, I tied an onion to my belt which was the style at the time. Now, to take the ferry cost a nickel. And in those days, nickels had pictures of bumblebees on ‘em. ‘Give me five bees for a quarter,’ you’d say. Now, where were we? Oh, yeah! The important thing was that I had an onion on my belt which was the style at the time. They didn’t have white onions because of the war. The only thing you could get was those big yellow ones. You see, back in those days, rich men would ride around in zeppelins, dropping coins on people. And one day, I seen J. D. Rockefeller flyin’ by– so I run out of the house with a big washtub. I just used it that morning to wash my turkey which in those days was known as a ‘walking bird.’ We’d always have walking bird on Thanksgiving, with all the trimmings. Cranberries, ‘injun eyes,’ and yams stuffed with gunpowder. Then we’d all watch football, which in those days was called ‘baseball. Now, the rest of this story takes place in 19-dickety-2. We had to say ‘dickety,’ ‘cause the Kaiser had stolen our word ‘twenty.’ I chased that rascal to get it back but gave up after dickety-six miles. The president is the divine Miss Sarah Bernardt. And all over America, people were doing a dance called the Funky Grandpa. We had to move out of the Statue of Liberty once we’d filled the head with garbage. The end."
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
