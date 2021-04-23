import discord
import requests
import json
import random
from Bot_Alive import keep_alive

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return quote


def chuck_norris_facts():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    json_data = json.loads(response.text)
    fact = json_data['value']
    return fact


def daily_facts():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    json_data = json.loads(response.text)
    fact = json_data["text"]
    return fact


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('$Chuck_Norris'):
        fact = chuck_norris_facts()
        await message.channel.send(fact)

    if msg.startswith("$fact"):
        daily_fact = daily_facts()
        await message.channel.send(daily_fact)



keep_alive()
client.run("ODI5ODkxNzgzODg1NTg2NDQy.YG-u8w.lyxaALovOqg1ndgt4-jIilLjaUM")


