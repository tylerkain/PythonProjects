import random

import discord
import requests
import json
from bot_alive import keep_alive
from Turtle_Racer import turtle_race


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


def dog_facts():
    response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
    json_data = json.loads(response.text)
    dog_fact = json_data[0]["fact"]
    return dog_fact


def race():
    turtle_race()
    return turtle_race()

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
    if msg.startswith("$dog"):
        dog_fact = dog_facts()
        await message.channel.send(dog_fact)
    if msg.startswith("$race"):
        race_turtle = race()
        await message.channel.send(race_turtle)


keep_alive()
client.run("ODI5ODkxNzgzODg1NTg2NDQy.YG-u8w.6OV-SIqNmW4qz68KrlKiLmz1vUI")
