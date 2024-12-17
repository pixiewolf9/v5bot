import discord
from discord.ui import Button, View
import os # default module
from dotenv import load_dotenv
from discord.ext import commands
import os

from clans_str import *
load_dotenv() # load all the variables from the env file
bot = discord.Bot()
@bot.event
async def on_ready():
    print("I am ready I am ready") 

with open("token") as file:
    token=file.read() 
bot.load_extension('cogs.clan')
bot.run(token)
    

