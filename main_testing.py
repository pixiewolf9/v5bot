import discord
from discord import SlashCommandGroup 
import os # default module
from dotenv import load_dotenv
from clans import *
bot = discord.Bot()
@bot.event
async def on_ready():
    print("I am ready I am ready") 

with open("token") as file:
    token=file.read()   
@bot.listen()
@bot.SlashCommandGroup(name="clan",description="clans of v5")
async def clan (ctx):
    ls_embed=discord.Embed(title="all the clans",description=ls,color=discord.Color.blue())
    await ctx.send(embed=ls_embed)


@clan.slash_command(name="brujah", description="all, info , description, bane or compulsion")
async def Brujah_Data(ctx,input:str):
    if (arg2=="all") or (arg2=="a"):
        Brujah_all_embed=discord.Embed(title="Brujah",description=Brujah_Info+"\n \n"+Brujah_Disciplines+"\n \n" +Brujah_Bane+"\n \n"+Brujah_Compulsion,color=discord.Color.blue())
        await ctx.send(embed=Brujah_all_embed)
        
    elif (arg2=="info")or(arg2=="i"):
        Brujah_embed=discord.Embed(title="Brujah",description=Brujah_Info,color=discord.Color.blue())
        await ctx.send(embed=Brujah_embed)
        
    elif (arg2=="disciplines") or(arg2=="d"):
        Brujah_Disciplines_embed=discord.Embed(title="Brujah Disciplines",description=Brujah_Disciplines,color=discord.Color.blue())
        await ctx.send(embed=Brujah_Disciplines_embed)
    elif (arg2=="bane") or(arg2=="b"):
        Brujah_Bane_embed=discord.Embed(title="Brujah Bane",description=Brujah_Bane,color=discord.Color.blue())
        await ctx.send(embed=Brujah_Bane_embed)
    elif (arg2=="compulsion") or(arg2=="c"):
        Brujah_Compulsion_embed=discord.Embed(title="Brujah compulsion",description=Brujah_Compulsion,color=discord.Color.blue())
        await ctx.send(embed=Brujah_Compulsion_embed)
        
    else:
        error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
        await ctx.send(embed=error_embed)    
bot.run(token) # run the bot with the token