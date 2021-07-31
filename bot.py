# bot.py
import os
import random
import asyncio
from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    channel = client.get_channel(669701746171445252)
    if message.author == client.user:
        return
    if (message.channel == channel):
        num = random.randint(1,25)
        if (num == 1):
            bot_reply = await message.channel.send("Looks like a ring toss has started! First to react with the emoji below earns a point!")
            reactions = []
            reaction_list = ["✅", "🙂", "😋", "🤔"]
            selected_reaciton = random.choice(reaction_list)
            reactions.append(selected_reaciton)
            for emoji in reactions: 
                await bot_reply.add_reaction(emoji)
            def check(reaction, user):
                return str(reaction.emoji) in reactions and user != client.user
                
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30, check=check)
                await message.channel.send(f"Congratulations <@{user.id}> you won a point! This has been noted")
                client.dispatch("winner", user.id)
            except asyncio.TimeoutError:
                await message.channel.send("You kept me on my toes! I timed out... 😴")

@client.event
async def on_winner(user):
     channel = client.get_channel(870920756987580436)
     await channel.send(f"!raffle tickets add \"bb ringtoss\" <@{user}> 1")
     client.dispatch("update")

@client.event
async def on_update():
     channel = client.get_channel(870921362020126750)
     await channel.send(f"!raffle tickets list \"bb ringtoss\"")

client.run(TOKEN)