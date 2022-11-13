import json

import discord
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("Moe is in " + str(guild_count) + " guilds.")


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]



@bot.event
async def on_message(message):
    if message.content == "moe":
        await message.channel.send("https://cdn.discordapp.com/attachments/398670520083808258/954971950525055017/Tyler_The_Creator_Crying__Eating_Mayonnaise.mp4");

    if message.author == bot.user:
        return

    if message.content == "hello":
        msg = 'Fuck off, and sam ur short lmao https://cdn.discordapp.com/attachments/398670520083808258/954975576471519302/mrfrog.png'
        await message.channel.send(msg)
        await message.channel.send("poopoo eater")



bot.run(DISCORD_TOKEN)
