import discord
from discord.ext import commands
from discord import app_commands
import clans
from clans import *
arg="dfg"
arg2="sd"
bot =commands.Bot(command_prefix="/",intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("I am ready I am ready") 

with open("token") as file:
    token=file.read()   




@bot.command()

async def clan(ctx,arg="fgh",arg2="a"):
    arg=arg.lower()
    arg2=arg2.lower()

    if arg=="ls":
        lsclans_embed=discord.Embed(title="clans",description=lsclans,color=discord.Color.blue())
        await ctx.send(embed=lsclans_embed)
    elif arg=="banu_haqim":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Banu_Haqim_all_embed=discord.Embed(title="Banu Haqim",description=Banu_Haqim_info+"\n \n"+Banu_Haqim_Disciplines+"\n \n" +Banu_Haqim_Bane+"\n \n"+Banu_Haqim_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Banu_Haqim_embed=discord.Embed(title="Banu Haqim ",description=Banu_Haqim_info,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Banu_Haqim_Disciplines_embed=discord.Embed(title="Banu Haqim Disciplines",description=Banu_Haqim_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Banu_Haqim_Bane_embed=discord.Embed(title="Banu Haqim Bane",description=Banu_Haqim_Bane,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Banu_Haqim_Compulsion_embed=discord.Embed(title="Banu Haqim compulsion",description=Banu_Haqim_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif arg=="brujah":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Brujah_all_embed=discord.Embed(title="Brujah",description=Brujah_info+"\n \n"+Brujah_Disciplines+"\n \n" +Brujahm_Bane+"\n \n"+Brujah_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Brujah_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Brujah_embed=discord.Embed(title="Brujah",description=Brujah_info,color=discord.Color.blue())
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
    else:
        error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
        await ctx.send(embed=error_embed)

'''
 elif arg=="b":
        _embed=discord.Embed(title="",description=,color=discord.Color.blue())
        await ctx.send(embed=_embed)
'''


bot.run(token)
