import discord
from discord.ui import Button, View
import os # default module
from dotenv import load_dotenv
from discord.ext import command
import os
import asyncio
load_dotenv() # load all the variables from the env file
bot = discord.Bot()
@bot.event
async def on_ready():
    await client.tree.sync()
    print("I am ready I am ready") 

with open("token") as file:
    token=file.read()   
@bot.event
async def on_ready():
    
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="clan", description="Say hello to the bot")

async def load():
    for filename in os.listdir("./files"):
        if filename.endswith(".py"):
            await client.load_extension(f"files.{filename[:-3]}")

    

bot.run(token) # run the bot with the token