import discord
import requests
import json
import random
from Bot_Alive import keep_alive

client = discord.Client()

sad_words = ["Tearful", "Crushed", "Humiliated"
                                   "Sorrowful", "Tormented", "Terrified", "Pained", "Deprived", "Nervous", "Grief",
             "Tortured", "Scared",
             "Anguish", "Dejected", "Worried",
             "Desolate", "Rejected", "Frightened",
             "Desperate", "Injured", "Restless",
             "Pessimistic", "Offended", "Upset",
             "Unhappy", "Afflicted", "Incapable",
             "Lonely", "Aching", "Alone", "Grieved", "Victimized", "Paralyzed", "Misgiving", "Indecisive", "Sad"
             ]
starter_encouragement = ["The only person you are destined to become is the person you decide to be.",
                         "Start where you are. Use what you have. Do what you can."
                         ]



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word.lower() in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragement))

keep_alive()
client.run('TOKEN')


